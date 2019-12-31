package MysteryDungeon;

import java.awt.Graphics2D;
import java.util.List;
import java.util.Random;
import java.util.concurrent.ThreadLocalRandom;

import me.jjfoley.gfx.IntPoint;

/**
 * @author sophiahager
 * Extended from https://github.com/jjfiv/CSC212FishGrid by @author jfoley
 * A WorldObject is an abstract "item" in the game. 
 * All movement is defined in this class.
 */
public abstract class WorldObject {
	/**
	 * Random in case you want random numbers!
	 */
	Random rand = ThreadLocalRandom.current();
	/**
	 * Where am I? x-tile in the grid.
	 */
	private int x;
	/**
	 * Where am I? y-tile in the grid.
	 */
	private int y;
	/**
	 * What world do I belong to?
	 */
	protected World world;
	/**
	 * what was the last move? Used for sprite purposes.
	 */
	public String lastMove = "down";

	/**
	 * is it a wall?
	 */
	boolean isWall = false;

	/**
	 * Create a new WorldObject -- this is the call to super(world) in Fish.
	 * 
	 * @param world the world filled with other objects.
	 */

	public WorldObject(World world) {
		this.world = world;
	}

	/**
	 * Remove this WorldObject from its world.
	 */
	public void remove() {
		this.world.remove(this);
		this.world = null;
	}

	/**
	 * Move this object to a given position (ignoring rules).
	 * 
	 * @param x the x-coordinate.
	 * @param y the y-coordinate.
	 */
	public void setPosition(int x, int y) {
		this.x = x;
		this.y = y;
	}

	/**
	 * Check if a WorldObject is a wall.
	 * 
	 * @return true if it's a wall.
	 */
	public boolean checkIfWall() {
		return isWall;
	}

	/**
	 * Move this object to a given position (ignoring rules).
	 * 
	 * @param pt The (x,y) pair as an IntPoint.
	 */
	public void setPosition(IntPoint pt) {
		this.setPosition(pt.x, pt.y);
	}

	/**
	 * Move this object up if possible. updates lastMove
	 * 
	 * @return true if it moved!
	 */
	public boolean moveUp() {
		if (world.canSwim(this, x, y - 1)) {
			this.y -= 1;
			this.lastMove = "up";
			return true;
		}
		return false;
	}

	/**
	 * Is this a pokemon?
	 * 
	 * @return true if this is a Pokemon
	 */
	public boolean isPokemon() {
		return this instanceof Pokemon;
	}

	/**
	 * Is this the player?
	 * 
	 * @return true if this is a Pokemon that is the player.
	 */
	public boolean isPlayer() {
		return isPokemon() && ((Pokemon) this).player;
	}

	/**
	 * Is this an Ally?
	 * 
	 * @return true if this is a Pokemon that is an ally.
	 */
	public boolean isAlly() {
		return isPokemon() && ((Pokemon) this).ally;
	}

	/**
	 * Move this object down if possible. updates lastMove
	 * 
	 * @return true if it moved!
	 */
	public boolean moveDown() {
		if (world.canSwim(this, x, y + 1)) {
			this.y += 1;
			this.lastMove = "down";
			return true;
		}
		return false;
	}

	/**
	 * Move this object left if possible. updates lastMove
	 * 
	 * @return true if it moved!
	 */
	public boolean moveLeft() {
		if (world.canSwim(this, x - 1, y)) {
			this.x -= 1;
			this.lastMove = "left";
			return true;
		}
		return false;
	}

	/**
	 * Move this object right if possible. updates lastMove
	 * 
	 * @return true if it moved!
	 */
	public boolean moveRight() {
		if (world.canSwim(this, x + 1, y)) {
			this.x += 1;
			this.lastMove = "right";
			return true;
		}
		return false;
	}

	/**
	 * Move randomly!
	 */

	public void moveRandomly() {
		// Can we move right, left, down, or up?
		boolean canMove = world.canSwim(this, x + 1, y) || world.canSwim(this, x - 1, y)
				|| world.canSwim(this, x, y + 1) || world.canSwim(this, x, y - 1);

		// If not, don't try to pick one.
		if (!canMove) {
			// "this" is stuck, and can't go anywhere!
			return;
		}

		// Pick one at random (that works):
		while (true) {

			// Choose a direction at random.
			int direction = ThreadLocalRandom.current().nextInt(4);

			boolean success = false;
			if (direction == 0) {
				success = moveUp();
			} else if (direction == 1) {
				success = moveDown();
			} else if (direction == 2) {
				success = moveRight();
			} else {
				success = moveLeft();
			}

			// Did the direction we picked work?
			if (success) {
				// If so, exit this method now.
				break;
			}
			// Otherwise go pick another.
		}
	}

	/**
	 * Part of my position!
	 * 
	 * @return the x-coordinate.
	 */
	public int getX() {
		return this.x;
	}

	/**
	 * Part of my position!
	 * 
	 * @return the y-coordinate.
	 */
	public int getY() {
		return this.y;
	}

	/**
	 * Get the position
	 * 
	 * @returns this objects IntPoint position.
	 */
	public IntPoint getPosition() {
		return new IntPoint(this.x, this.y);
	}

	/**
	 * I'm a world object! I exist in the world somewhere! This method tests that!
	 */
	public void checkFindMyself() {
		if (!findSameCell().contains(this)) {
			throw new AssertionError("Couldn't find myself! Check World.register still works!");
		}
	}

	/**
	 * Find all the items at the same position as me!
	 * 
	 * @return a list of WorldObject.
	 */
	public List<WorldObject> findSameCell() {
		return world.find(this.x, this.y);
	}

	/**
	 * Check whether this object is in the same spot as another.
	 * 
	 * @param other the other WorldObject.
	 * @return true if their x and y coordinates are the same.
	 */
	public boolean inSameSpot(WorldObject other) {
		return this.x == other.getX() && this.y == other.getY();
	}

	/**
	 * Draw this WorldObject!
	 * 
	 * Abstract so that subclasses MUST implement.
	 * 
	 * @param g Graphics2D API.
	 */
	public abstract void draw(Graphics2D g);

	/**
	 * Step this WorldObject!
	 * 
	 * Abstract subclasses MUST implement!
	 */
	public abstract void step();

}