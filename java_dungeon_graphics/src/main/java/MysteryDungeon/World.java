package MysteryDungeon;

import java.util.*;
import java.util.concurrent.ThreadLocalRandom;

import me.jjfoley.gfx.IntPoint;

/**
 * @author sophiahager
 * Extended from https://github.com/jjfiv/CSC212FishGrid by @author jfoley
 * A World is a 2d grid, represented as a width, a height, and a list of
 * WorldObjects in that world.
 */
public class World {
	/**
	 * The size of the grid (x-tiles).
	 */
	private int width;
	/**
	 * variable checks if you've lost the game (useful to not remove the darkness at
	 * the end if you lose the game)
	 */
	boolean lost = false;
	/**
	 * The size of the grid (y-tiles).
	 */
	private int height;
	/**
	 * A list of objects in the world (Fish, Snail, Rock, etc.).
	 */
	private List<WorldObject> items;
	/**
	 * A reference to a random object, so we can randomize placement of objects in
	 * this world.
	 */
	private Random rand = ThreadLocalRandom.current();

	/**
	 * Create a new world of a given width and height.
	 * 
	 * @param w - width of the world.
	 * @param h - height of the world.
	 */
	public World(int w, int h) {
		items = new ArrayList<>();
		width = w;
		height = h;
	}

	/**
	 * What is under this point?
	 * 
	 * @param x - the tile-x.
	 * @param y - the tile-y.
	 * @return a list of objects!
	 */
	public List<WorldObject> find(int x, int y) {
		List<WorldObject> found = new ArrayList<>();

		// Check out every object in the world to find the ones at a particular point.
		for (WorldObject w : this.items) {
			// But only the ones that match are "found".
			if (x == w.getX() && y == w.getY()) {
				found.add(w);
			}
		}

		// Give back the list, even if empty.
		return found;
	}

	/**
	 * This is used by PlayGame to draw all our items!
	 * 
	 * @return the list of items.
	 */
	public List<WorldObject> viewItems() {
		// Don't let anybody add to this list!
		// Make them use "register" and "remove".

		// This is kind of an advanced-Java trick to return a list where add/remove
		// crash instead of working.
		return Collections.unmodifiableList(items);
	}

	/**
	 * Add an item to this World.
	 * 
	 * @param item - the Fish, Rock, Snail, or other WorldObject.
	 */
	public void register(WorldObject item) {
		// Print out what we've added, for our sanity.
		// System.out.println("register: "+item.getClass().getSimpleName());
		items.add(item);
	}

	/**
	 * This is the opposite of register. It removes an item (like a fish) from the
	 * World.
	 * 
	 * @param item - the item to remove.
	 */
	public void remove(WorldObject item) {
		items.remove(item);
	}

	/**
	 * Want to remove a lot of objects at once?
	 * 
	 * @param objects- list to remove
	 */
	public void removeAll(ArrayList<WorldObject> objects) {
		items.removeAll(objects);
	}

	/**
	 * How big is the world we model?
	 * 
	 * @return the width.
	 */
	public int getWidth() {
		return width;
	}

	/**
	 * How big is the world we model?
	 * 
	 * @return the height.
	 */
	public int getHeight() {
		return height;
	}

	/**
	 * Try to find an unused part of the World for a new object!
	 * 
	 * @return a point (x,y) that has nothing else in the grid.
	 */
	public IntPoint pickUnusedSpace() {
		// Build a set of all available spaces:
		Set<IntPoint> available = new HashSet<>();
		for (int x = 0; x < getWidth(); x++) {
			for (int y = 0; y < getHeight(); y++) {
				available.add(new IntPoint(x, y));
			}
		}
		// Remove any spaces that are in use:
		for (WorldObject item : this.items) {
			available.remove(item.getPosition());
		}

		// If we get here, we have too much stuff.
		// Let's crash our Java program!
		if (available.size() == 0) {
			throw new IllegalStateException(
					"The world is too small! Trying to pick an unused space but there's nothing left.");
		}

		// Return an unused space at random: Need to copy to a list since sets do not
		// have orders.
		List<IntPoint> unused = new ArrayList<>(available);
		int which = rand.nextInt(unused.size());
		return unused.get(which);
	}

	/**
	 * Insert an item randomly into the grid.
	 * 
	 * @param item - the rock, fish, snail or other WorldObject.
	 */
	public void insertRandomly(WorldObject item) {
		item.setPosition(pickUnusedSpace());
		this.register(item);
		item.checkFindMyself();
	}

	/**
	 * Insert a new Wall into the world at random.
	 * 
	 * @return the Wall
	 */
	public Wall insertWallRandomly() {
		Wall r = new Wall(this);
		insertRandomly(r);
		return r;
	}

	/**
	 * Insert a new Pokemon into the world at random of a specific color.
	 * 
	 * @param id determines features of the Pokemon.
	 * @return the new pokemon itself.
	 */
	public Pokemon insertPokemonRandomly(int id) {
		Pokemon f = new Pokemon(id, this);
		insertRandomly(f);
		return f;
	}

	/**
	 * Adds stairs
	 * 
	 * @returns stairs
	 */
	public Stairs insertStairs() {
		Stairs stairs = new Stairs(this);
		insertRandomly(stairs);
		return stairs;
	}

	/**
	 * Determine if a WorldObject can swim to a particular point.
	 * 
	 * @param whoIsAsking - the object (not just the player!)
	 * @param x           - the x-tile.
	 * @param y           - the y-tile.
	 * @return true if they can move there.
	 */
	public boolean canSwim(WorldObject whoIsAsking, int x, int y) {
		if (x < 0 || x >= width || y < 0 || y >= height) {
			return false;
		}

		// This will be important.
		boolean isPlayer = whoIsAsking.isPlayer();

		// We will need to look at who all is in the spot to determine if we can move
		// there.
		List<WorldObject> inSpot = this.find(x, y);

		for (WorldObject it : inSpot) {
			boolean isAlly = it.isAlly();
			if (it instanceof Wall) {
				return false;
			}
			// players can move over their allies.
			else if (it instanceof Pokemon && isAlly == true && whoIsAsking.isPlayer() == true) {
				return true;
			}
			// otherwise pokemon cant intersect.
			else if (it instanceof Pokemon) {
				return false;
			}
		}

		// If we didn't see an obstacle, we can move there!
		return true;
	}

	/**
	 * Basically removes visibility squares.
	 */
	public void stepAll() {
		Pokemon player = null;
		// finds the player
		for (WorldObject it : this.items) {
			if (it instanceof Pokemon && it.isPlayer() == true) {
				player = (Pokemon) it;
			}
		}
		// gets its x and y
		int playerX = player.getX();
		int playerY = player.getY();
		// lists all visibility squares in a radius of the player.
		ArrayList<VisibilitySquare> toRemove = new ArrayList<>();
		for (WorldObject it : this.items) {
			it.step();
			if (it instanceof VisibilitySquare) {
				if (Math.abs(it.getX() - playerX) < 4 && Math.abs(it.getY() - playerY) < 4) {
					toRemove.add((VisibilitySquare) it);
				}
			}
		}
		// if the game isn't lost, removes those squares.
		if (lost == false) {
			for (VisibilitySquare item : toRemove) {
				item.remove();
			}
		}
	}

}
