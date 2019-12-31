package MysteryDungeon;

import java.awt.Color;
import java.awt.Graphics2D;
import java.awt.geom.Rectangle2D;
/**
 * @author sophiahager
 */
public class VisibilitySquare extends WorldObject {

	/**
	 * it's just a generic black square. I use it to hide whats going on in the
	 * world you haven't found. Otherwise it sits there.
	 */
	Color color;
	/**
	 * At the end, it multipurposes as an end screen though! Here are some confetti
	 * colors:
	 */
	Color[] COLORS = { Color.RED, Color.BLUE, Color.CYAN, Color.GREEN, Color.PINK, Color.MAGENTA, Color.YELLOW,
			Color.ORANGE };

	public VisibilitySquare(World world, boolean won) {
		super(world);
		// if you haven't won, the color is black.
		if (won == false) {
			this.color = color.BLACK;
		}
		// if you have, 90% are white, and the rest are multicolored.
		else {
			this.color = color.white;
			double chance = rand.nextDouble();
			if (chance < .1) {
				this.color = COLORS[rand.nextInt(COLORS.length)];
			}
		}

	}

	@Override
	public void draw(Graphics2D g) {
		Rectangle2D square = new Rectangle2D.Double(-.5, -.5, 1, 1);
		g.setColor(this.color);
		g.fill(square);
	}

	@Override
	public void step() {
	}

}