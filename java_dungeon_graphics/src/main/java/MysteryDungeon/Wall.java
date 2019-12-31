package MysteryDungeon;

import java.awt.Color;
import java.awt.Graphics2D;
import java.awt.geom.Rectangle2D;

/**
 *
 * @author sophiahager
 * Extended from https://github.com/jjfiv/CSC212FishGrid by @author jfoley
 * Building blocks for walls
 */
public class Wall extends WorldObject {

	/**
	 * The wall is sort of a green-yellow.
	 */
	final Color color = new Color(140, 188, 0);

	public Wall(World world) {
		super(world);
		// Walls are walls.
		this.isWall = true;
	}

	/**
	 * Draw the wall.
	 */
	@Override
	public void draw(Graphics2D g) {
		g.setColor(this.color);
		Rectangle2D wall = new Rectangle2D.Double(-.5, -.5, 1, 1);
		g.fill(wall);
	}

	@Override
	public void step() {
	}

}