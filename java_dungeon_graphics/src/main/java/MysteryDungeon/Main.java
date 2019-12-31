package MysteryDungeon;

import java.awt.Color;
import java.awt.Graphics2D;
import java.awt.event.KeyEvent;
import java.awt.geom.Rectangle2D;
import java.util.List;
import java.util.Map;
import java.util.concurrent.TimeUnit;
import me.jjfoley.gfx.GFX;
import me.jjfoley.gfx.TextBox;

/**
 * @author sophiahager
 * Extended from https://github.com/jjfiv/CSC212FishGrid by @author jfoley
 */

public class Main extends GFX {
	/**
	 * Game size (visual).
	 */
	public static int VISUAL_GRID_SIZE = 720;

	/**
	 * Game size (logical).
	 */
	public static int LOGICAL_GRID_SIZE = 30;
	/**
	 * The words appear in the top part of the screen.
	 */
	public static int TOP_PART = 50;
	/**
	 * There's a border to make it look pretty (the board is inset by this much).
	 */
	public static int BORDER = 5;
	/**
	 * This is where the game logic lives.
	 */
	PokemonGame game;
	/**
	 * This TextBox wraps up making fonts and centering text.
	 */
	TextBox gameState = new TextBox("");
	/**
	 * Additional instructions
	 */
	TextBox gameState2 = new TextBox("Press X to open/close the menu. Enter selects the current menu object.");
	/**
	 * tracks what floor you're on
	 */
	TextBox floorLevel = new TextBox("");
	/**
	 * tracks the player's health
	 */
	TextBox health = new TextBox("");
	/**
	 * This is a rectangle representing the top part of the screen.
	 */
	Rectangle2D Box1;
	/**
	 * rectangle to center the floor text
	 */
	Rectangle2D floorOuter;
	/**
	 * rectangle to center the health text
	 */
	Rectangle2D healthBox;
	/**
	 * rectangle to center the tutorial text
	 */
	Rectangle2D T2Box;

	/**
	 * what floor of the dungeon are you on?
	 */
	int floorCount;

	/**
	 * Starts everything as if facing down.
	 */
	String lastPress = "down";
	/**
	 * first thing the top displays is the controls.
	 */

	String importantInfo = "Navigate to the stairs using the arrow keys, attack foes using the space bar. ";
	/**
	 * Is it waiting for input on a menu?
	 */
	boolean menuState = false;
	/**
	 * what menu is it looking at? (usually none.)
	 */
	Menu selection = null;

	/**
	 * Construct a new floor
	 */

	public Main() {
		super(VISUAL_GRID_SIZE + BORDER * 2, VISUAL_GRID_SIZE + BORDER * 2 + TOP_PART);
		floorCount = 1;
		game = new PokemonGame(LOGICAL_GRID_SIZE, LOGICAL_GRID_SIZE, 1);
		gameState.color = Color.WHITE;
		gameState.setFont(TextBox.BOLD_FONT);
		gameState.setFontSize((getWidth() * 2) / importantInfo.length());
		gameState2.color = Color.WHITE;
		gameState2.setFont(TextBox.BOLD_FONT);
		gameState2.setFontSize((getWidth() * 2) / importantInfo.length());
		floorLevel.setColor(Color.WHITE);
		floorLevel.setFont(TextBox.BOLD_FONT);
		floorLevel.setFontSize(TOP_PART / 5.0);
		health.setColor(Color.WHITE);
		health.setFont(TextBox.BOLD_FONT);
		health.setFontSize(TOP_PART / 5.0);
		Box1 = new Rectangle2D.Double(0, 0, getWidth(), TOP_PART);
		T2Box = new Rectangle2D.Double(0, 20, getWidth(), TOP_PART);
		floorOuter = new Rectangle2D.Double(0, 20, 50, 50);
		healthBox = new Rectangle2D.Double(450, 20, 500, 50);
	}

	/**
	 * How big is a tile?
	 * 
	 * @return this returns the tile width.
	 */
	private int getTileW() {
		return VISUAL_GRID_SIZE / game.world.getWidth();
	}

	/**
	 * How big is a tile?
	 * 
	 * @return this returns the tile height.
	 */
	private int getTileH() {
		return VISUAL_GRID_SIZE / game.world.getWidth();
	}

	/**
	 * picked it to be as close to the game as possible
	 */
	public static Color PATH_COLOR = new Color(227, 221, 72);
	/**
	 * slightly lighter.
	 */
	public static Color GRID_COLOR = new Color(210, 200, 50);

	/**
	 * Draw the game state.
	 */
	@Override
	public void draw(Graphics2D g) {
		// Background of window is dark-dark blue.
		g.setColor(Color.blue.darker().darker());
		g.fillRect(0, 0, getWidth(), getHeight());

		// Get a a reference to the game world to draw.
		World world = game.world;

		// Draw the main TextBox.
		this.gameState.centerInside(this.Box1);
		this.gameState.draw(g);
		// Draw floor level text box
		this.floorLevel.centerInside(this.floorOuter);
		this.floorLevel.draw(g);
		// Draw health text box
		this.health.centerInside(this.healthBox);
		this.health.draw(g);
		// Draw instructions.
		this.gameState2.centerInside(this.T2Box);
		this.gameState2.draw(g);

		// Slide the world down, and into the box.
		// This makes our rendering of the board easier.
		g.translate(BORDER, BORDER + TOP_PART);

		// Use the tile-sizes.
		int tw = getTileW();
		int th = getTileH();

		// Draw the ocean (not the whole screen).
		g.setColor(PATH_COLOR);
		g.fillRect(0, 0, tw * world.getWidth(), th * world.getHeight());
		// Draw a grid to better picture how the game works.
		g.setColor(GRID_COLOR);
		for (int x = 0; x < world.getWidth(); x++) {
			for (int y = 0; y < world.getHeight(); y++) {
				g.drawRect(x * tw, y * th, tw, th);
			}
		}

		// For everything in our world:
		for (WorldObject wo : world.viewItems()) {
			// Draw it with a 1x1 graphical world, with the center right in the middle of
			// the tile.
			// I fiddled with this translate to get pixel-perfect. Maybe there's a nicer
			// way, but it works for now.

			Graphics2D forWo = (Graphics2D) g.create();
			forWo.translate((int) ((wo.getX() + 0.5) * tw) + 1, (int) ((wo.getY() + 0.5) * th) + 1);
			forWo.scale(tw, th);
			wo.draw(forWo);
			forWo.dispose();
		}
	}

	/**
	 * We separate our "Main" game logic update here.
	 * 
	 * @param secondsSinceLastUpdate - my GFX code can tell us how long it is
	 *                               between each update, but we don't actually care
	 *                               here.
	 */
	@Override
	public void update(double secondsSinceLastUpdate) {
		// if it's not looking for menu input...
		if (this.menuState == false) {
			// If they lost the game, that's game over.
			if (game.lostGame == true) {
				this.gameState.setString("GAME OVER");
				this.gameState2.setString("");
				return;
			}
			// If they won the game, that's also game over.
			if (game.gameOver() && floorCount > 2) {
				this.gameState.setString("You win!");
				this.gameState2.setString("");
				// generate a confetti frame
				game.gameWon();
				// let's pause for several milliseconds so as not to be terrible.
				try {
					TimeUnit.MILLISECONDS.sleep(80);
				} catch (InterruptedException e) {
					// TODO Auto-generated catch block
					e.printStackTrace();
				}
				return;
			}
			// If they win a floor but it's not the end, make a new floor.
			else if (game.gameOver()) {
				floorCount++;
				// transfer the players/allys health into the new floor
				int currentHealth = game.player.health;
				int allyHealth = game.player.health;
				// transfer the player's items into the new floor
				Map<String, Integer> inventory = game.player.inventory;
				game = new PokemonGame(LOGICAL_GRID_SIZE, LOGICAL_GRID_SIZE, floorCount);
				game.player.health = currentHealth;
				game.ally.get(0).health = allyHealth;
				game.player.inventory = inventory;
			}

			// Update the text in the TextBoxes.
			this.gameState.setString(this.importantInfo);
			this.floorLevel.setString("B" + floorCount + "F");
			this.health.setString("HP: " + game.player.health + "/30");
			// Read the state of the keyboard:
			boolean up = this.processKey(KeyEvent.VK_W) || this.processKey(KeyEvent.VK_UP);
			boolean down = this.processKey(KeyEvent.VK_S) || this.processKey(KeyEvent.VK_DOWN);
			boolean left = this.processKey(KeyEvent.VK_A) || this.processKey(KeyEvent.VK_LEFT);
			boolean right = this.processKey(KeyEvent.VK_D) || this.processKey(KeyEvent.VK_RIGHT);
			boolean basicAttack = this.processKey(KeyEvent.VK_SPACE);
			boolean menu = this.processKey(KeyEvent.VK_X);
			// Move the player if we can:
			boolean moved = false;
			// tracks lastPress for. You know. Sprite reasons (and attacking), so even if
			// you don't move, it still edits the direction.
			if (up) {
				moved = this.game.player.moveUp();
				lastPress = "up";
				this.game.player.lastMove = "up";
			} else if (down) {
				moved = this.game.player.moveDown();
				lastPress = "down";
				this.game.player.lastMove = "down";
			} else if (left) {
				moved = this.game.player.moveLeft();
				lastPress = "left";
				this.game.player.lastMove = "left";
			} else if (right) {
				moved = this.game.player.moveRight();
				lastPress = "right";
				this.game.player.lastMove = "right";
			}

			// Only advance the game if the player presses something!
			if (basicAttack || moved || menu) {
				// if x is pressed, open a menu and wait for more input.
				if (menu == true) {
					this.selection = game.makeMenu();
					this.menuState = true;
					return;
				}
				// If you attack things, attack them. You can't attack allies.
				if (basicAttack == true) {
					if (lastPress == "up") {
						List<WorldObject> objects = game.world.find(this.game.player.getX(),
								this.game.player.getY() - 1);
						for (WorldObject object : objects) {
							if (object instanceof Pokemon && object.isAlly() == false) {
								this.importantInfo = this.game.player.attack((Pokemon) object);
							}
						}

					} else if (lastPress == "down") {
						List<WorldObject> objects = game.world.find(this.game.player.getX(),
								this.game.player.getY() + 1);
						for (WorldObject object : objects) {
							if (object instanceof Pokemon && object.isAlly() == false) {
								this.importantInfo = this.game.player.attack((Pokemon) object);
							}
						}

					} else if (lastPress == "left") {
						List<WorldObject> objects = game.world.find(this.game.player.getX() - 1,
								this.game.player.getY());
						for (WorldObject object : objects) {
							if (object instanceof Pokemon && object.isAlly() == false) {
								this.importantInfo = this.game.player.attack((Pokemon) object);
							}
						}

					} else if (lastPress == "right") {
						List<WorldObject> objects = game.world.find(this.game.player.getX() + 1,
								this.game.player.getY());
						for (WorldObject object : objects) {
							if (object instanceof Pokemon && object.isAlly() == false) {
								this.importantInfo = (this.game.player.attack((Pokemon) object));
							}
						}

					}

				}
				// Update game logic!
				this.game.step();
				// Update message at the top!
			}
			// check if the player wants to use the berry or exit the menu.
		} else {
			boolean exit = this.processKey(KeyEvent.VK_X);
			boolean select = this.processKey(KeyEvent.VK_ENTER);
			if (exit == true) {
				game.chooseMenu(selection, false);
				this.menuState = false;
			}
			if (select == true) {
				game.chooseMenu(selection, true);
				this.menuState = false;
				// using an item uses a turn!
				this.game.step();
			}
		}
	}

	/**
	 * Create and start the game!
	 * 
	 * @param args - not run from the command line so no args are used.
	 */
	public static void main(String[] args) {
		Main game = new Main();
		game.start();
	}

}