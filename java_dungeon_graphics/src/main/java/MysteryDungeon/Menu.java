package MysteryDungeon;

import java.awt.Color;
import java.awt.Graphics2D;
import java.awt.event.KeyEvent;
import java.awt.geom.Rectangle2D;
import java.util.Map;
import me.jjfoley.gfx.TextBox;
import java.awt.event.KeyEvent;
import me.jjfoley.gfx.GFX;
/**
 * @author sophiahager
 */
public class Menu extends WorldObject {
	/**
	 * items in the menu
	 */
	Map<String, Integer> inventory;
	/**
	 * box to center it in
	 */
	final Rectangle2D outer;
	/**
	 * the place to draw the items-- to improve game, add more rows (iteratively?)
	 */
	TextBox row1 = new TextBox("");

	public Menu(World world, Map<String, Integer> inventory) {
		super(world);
		// Displays the type/amount of items (right now only one item, oran berries)
		outer = new Rectangle2D.Double(-200, -200, 300, 200);
		row1.setFontSize(outer.getHeight() / 5);
		row1.setString("Oran Berry: " + inventory.get("Oran Berry"));
		this.inventory = inventory;
	}

	@Override
	public void draw(Graphics2D g) {
		Graphics2D scale = (Graphics2D) g.create();
		scale.scale(1.0 / 80.0, 1.0 / 80.0);
		scale.translate(-40, -60);
		scale.setColor(Color.white);
		scale.fill(outer);
		scale.setColor(Color.black);
		scale.draw(outer);
		row1.centerInside(outer);
		row1.setColor(Color.black);
		row1.draw(scale);
		scale.dispose();
	}

	/**
	 * returns what is being used.
	 * 
	 * @param choice - exit or use?
	 * @returns either the name of the item or null.
	 */
	public String choose(boolean choice) {
		if (choice == true && this.inventory.get("Oran Berry") > 0) {
			this.remove();
			return "Oran Berry";
		} else {
			this.remove();
			return null;
		}

	}

	@Override
	public void step() {
	}

}
