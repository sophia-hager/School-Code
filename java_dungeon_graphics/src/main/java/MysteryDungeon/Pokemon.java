package MysteryDungeon;

import java.awt.Color;
import java.awt.Graphics2D;
import java.awt.geom.Rectangle2D;
import java.awt.image.BufferedImage;
import java.io.File;
import java.io.IOException;
import java.util.HashMap;
import java.util.Map;
import javax.imageio.ImageIO;

/**
 * @author sophiahager
 * Extended from https://github.com/jjfiv/CSC212FishGrid by @author jfoley
 * Sprites taken from https://www.spriters-resource.com
 */

public class Pokemon extends WorldObject {
	/**
	 * A list of the sprites.
	 */

	static String[] SPRITELIST = { "Char-", "Bulb-", "Sun-", "Bird-", "Wurm-", "Egg-" };

	/**
	 * This is an index into the Sprite array.
	 */
	int id;
	/**
	 * The health of this pokemon.
	 */
	int health;
	/**
	 * a number that determines the amount of damage.
	 */
	int damage;
	/**
	 * the pokemon's name
	 */
	String name;
	/**
	 * the sprite name
	 */
	String sprite;
	/**
	 * which direction it's facing
	 */
	String direction;
	/**
	 * Whether or not this is the player;
	 */
	boolean player = false;
	/**
	 * Whether or not this is the ally;
	 */
	boolean ally = false;
	/**
	 * tracks if it's fainted.
	 */
	boolean fainted = false;
	/**
	 * four sprites, one for each direction
	 */
	BufferedImage up;
	BufferedImage down;
	BufferedImage left;
	BufferedImage right;

	/**
	 * A map that contains the (name of the) items and number that the player has.
	 */
	Map<String, Integer> inventory;

	/**
	 * Called only on the Pokemon that is the player!
	 */
	public void markAsPlayer() {
		this.player = true;
	}

	/**
	 * Called on the ally-- in this level only one ally, but theoretically could add
	 * more?
	 */
	public void markAsAlly() {
		this.ally = true;
	}

	/**
	 * A Pokemon knows what World it belongs to, because all WorldObjects do.
	 * 
	 * @param id    informs which pokemon it is
	 * @param world The world itself.
	 */
	public Pokemon(int id, World world) {
		super(world);
		this.inventory = new HashMap<String, Integer>();
		inventory.put("Oran Berry", 0);
		this.sprite = SPRITELIST[id];
		// initial direction is up.
		this.direction = "up";
		this.id = id;
		// loads all four sprite images

		try {
			up = ImageIO.read(new File("src/main/resources/" + this.sprite + "back.png"));
		} catch (IOException e) {
			// TODO Auto-generated catch block
			e.printStackTrace();
		}
		try {
			down = ImageIO.read(new File("src/main/resources/" + this.sprite + "front.png"));
		} catch (IOException e) {
			// TODO Auto-generated catch block
			e.printStackTrace();
		}
		try {
			left = ImageIO.read(new File("src/main/resources/" + this.sprite + "left.png"));
		} catch (IOException e) {
			// TODO Auto-generated catch block
			e.printStackTrace();
		}
		try {
			right = ImageIO.read(new File("src/main/resources/" + this.sprite + "right.png"));
		} catch (IOException e) {
			// TODO Auto-generated catch block
			e.printStackTrace();
		}

		// if it's the player or ally, it's stronger.
		if (id == 0 || id == 1) {
			this.health = 30;
			this.damage = 13;
		}
		// if it's not, it's weaker.
		if (id > 1) {
			this.health = 15;
			this.damage = 2;
		}

		// gives each one a name.
		if (id == 0) {
			this.name = "Charmander";

		}
		if (id == 1) {
			this.name = "Bulbasaur";
		}
		if (id == 2) {
			this.name = "Sunkern";
		}
		if (id == 3) {
			this.name = "Pidgey";
		}
		if (id == 4) {
			this.name = "Wurmple";
		}
		if (id == 5) {
			this.name = "Exeggcute";
		}

	}

	// draws the pokemon.
	@Override
	public void draw(Graphics2D g) {
		Graphics2D scale = (Graphics2D) g.create();
		scale.scale(1.0 / 80.0, 1.0 / 80.0);
		scale.translate(-40, -60);
		scale.setColor(Color.black);
		// if it's the player or ally, display a health bar underneath.
		if (this.id < 2) {
			Rectangle2D outer = new Rectangle2D.Double(0, 70, 80, 20);
			Rectangle2D inner = new Rectangle2D.Double(0, 70, ((80 * this.health) / 30), 20);
			scale.draw(outer);
			// the color varies by amount of health.
			Color healthColor = Color.green;

			if (this.health > 10 && this.health < 20) {
				healthColor = Color.yellow;
			} else if (this.health <= 10) {
				healthColor = Color.red;
			}
			scale.setColor(healthColor);
			scale.fill(inner);
		}
		// if it moved down, sprite faces down, etc.
		if (this.lastMove == "down") {
			scale.drawImage(down, 0, 0, null);
		} else if (this.lastMove == "up") {
			scale.drawImage(up, 0, 0, null);
		} else if (this.lastMove == "left") {
			scale.drawImage(left, 0, 0, null);
		}
		if (this.lastMove == "right") {
			scale.drawImage(right, 0, 0, null);
		}
		scale.dispose();

	}

	/**
	 * if it eats an oran berry, it gets health back!
	 */
	public void eatOranBerry() {
		// in-game, you get +100 health, but since this game has a max of 30 health,
		// it's irrelevant.
		this.health = 30;
	}

	/**
	 * method that attacks an opponent.
	 * 
	 * @param opponent- the pokemon you're attacking
	 * @returns a string that displays up top for the player.
	 */
	public String attack(Pokemon opponent) {
		int actualDamage = rand.nextInt(this.damage - 1) + 5;
		opponent.health -= actualDamage;
		if (opponent.health < 1) {
			opponent.fainted = true;
		}
		String text = opponent.name + " took " + actualDamage + " damage! ";
		if (opponent.fainted == true) {
			text = text + opponent.name + " fainted!";
		}
		// changes the pokemon's direction
		if (opponent.getX() > this.getX()) {
			this.lastMove = "right";
		} else if (opponent.getX() < this.getX()) {
			this.lastMove = "left";
		} else if (opponent.getY() > this.getY()) {
			this.lastMove = "down";
		} else {
			this.lastMove = "up";
		}
		return text;
	}

	@Override
	public void step() {
		// Fish are controlled at a higher level; see FishGame.

	}
}