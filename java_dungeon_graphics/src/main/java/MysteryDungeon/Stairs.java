package MysteryDungeon;

import java.awt.Color;
import java.awt.Graphics2D;
import java.awt.geom.Rectangle2D;

/**
 * @author sophiahager
 * Extended from https://github.com/jjfiv/CSC212FishGrid by @author jfoley
 * This class represents the stairs. Finding the stairs takes you down a level.
 */

public class Stairs extends WorldObject {
	final Rectangle2D staircase;
	final Rectangle2D stair1;
	final Rectangle2D stair2;

	public Stairs(World world) {
		super(world);
		staircase = new Rectangle2D.Double(-.5, -.49, 1, 1);
		stair1 = new Rectangle2D.Double(-.5, -.24, 1, .5);
		stair2 = new Rectangle2D.Double(-.5, .14, 1, .35);
	}

	@Override
	public void draw(Graphics2D g) {
		g.setColor(Color.black);
		g.fill(staircase);
		g.setColor(Color.DARK_GRAY);
		g.fill(stair1);
		g.setColor(Color.LIGHT_GRAY);
		g.fill(stair2);
	}

	@Override
	public void step() {
	}

}
