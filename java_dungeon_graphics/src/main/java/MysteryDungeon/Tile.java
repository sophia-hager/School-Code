package MysteryDungeon;

import java.util.ArrayList;
import java.util.Collections;
import java.util.Random;

public class Tile {
	/**
	 * a tile's x
	 */
	int x;
	/**
	 * a tile's y
	 */
	int y;
	/**
	 * the neighbors of that tile that should also be cleared
	 */
	ArrayList<Tile> clear;
	/**
	 * a list of tiles that forms a path
	 */
	ArrayList<Tile> path;

	public Tile(int x, int y) {
		this.x = x;
		this.y = y;
		this.clear = new ArrayList<Tile>();
		this.path = new ArrayList<Tile>();

	}

	/**
	 * creates a list of the eight tiles surrounding a tile.
	 * 
	 * @returns that list.
	 */
	public ArrayList<Tile> nineBynine() {
		clear.add(this);

		clear.add(new Tile(x - 1, y));
		clear.add(new Tile(x + 1, y));
		clear.add(new Tile(x - 1, y - 1));
		clear.add(new Tile(x - 1, y + 1));
		clear.add(new Tile(x, y - 1));
		clear.add(new Tile(x, y + 1));
		clear.add(new Tile(x + 1, y - 1));
		clear.add(new Tile(x + 1, y + 1));
		return clear;
	}

	/**
	 * make a bigger room by running ninebynine on a neighboring tile.
	 * 
	 * @returns that room.
	 */
	public ArrayList<Tile> sizeTwo() {
		clear = this.nineBynine();
		Random rand = new Random();
		Tile thing = clear.get(rand.nextInt(clear.size()));
		while (thing.x > 28 || thing == this || thing.x < 1 || thing.y < 1 || thing.y > 28 || thing == this) {
			thing = clear.get(rand.nextInt(clear.size()));
		}
		for (Tile tile : thing.nineBynine()) {
			if (clear.contains(tile) == false) {
				clear.add(tile);
			}
		}
		return clear;
	}

	/**
	 * makes a bigger room.
	 * 
	 * @returns the list of tiles in that room.
	 */
	public ArrayList<Tile> sizeThree() {
		clear = this.sizeTwo();
		Random rand = new Random();
		Tile thing = clear.get(rand.nextInt(clear.size()));
		for (Tile tile : thing.sizeTwo()) {
			if (clear.contains(tile) == false) {
				clear.add(tile);
			}
		}
		return clear;
	}

	/**
	 * 
	 * @returns the neighbors of a tile
	 */
	public ArrayList<Tile> getNeighbors() {

		return this.clear;
	}

	/**
	 * creates a linear path to another tile
	 * 
	 * @param center-- the tile that you want to get to
	 * @returns the list of tiles in the path
	 */
	public ArrayList<Tile> clearPath(Tile center) {
		ArrayList<Tile> options = center.getNeighbors();
		Collections.shuffle(options);
		Tile destination = options.get(0);
		Tile startPoint = new Tile(this.x, this.y);
		if (destination.x > startPoint.x) {
			for (int i = startPoint.x; i <= destination.x; i++) {
				path.add(new Tile(i, this.y));
			}
			startPoint = new Tile(destination.x, startPoint.y);
		} else if (destination.x <= startPoint.x) {
			for (int i = destination.x; i < startPoint.x; i++) {
				path.add(new Tile(i, startPoint.y));
			}
			startPoint = new Tile(destination.x, startPoint.y);
		}
		if (destination.y > startPoint.y) {
			for (int i = startPoint.y; i <= destination.y; i++) {
				path.add(new Tile(startPoint.x, i));
			}
		} else if (destination.y < startPoint.y) {
			for (int i = destination.y; i <= startPoint.y; i++) {
				path.add(new Tile(startPoint.x, i));
			}
		}
		return path;
	}
}
