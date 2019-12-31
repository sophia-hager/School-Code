package MysteryDungeon;

import java.util.ArrayList;
import java.util.Collections;
import java.util.List;
import java.util.Map;
import java.util.Random;

/**
 * @author sophiahager
 * Extended from https://github.com/jjfiv/CSC212FishGrid by @author jfoley
 * This class manages our model of gameplay.
 */
public class PokemonGame {
	/**
	 * This is the world in which the fish are missing. (It's mostly a List!).
	 */
	World world;
	/**
	 * The player goes seeking the stairs
	 */
	Pokemon player;
	/**
	 * The stairs location.
	 */
	Stairs stairs;
	/**
	 * Your ally follows you around. This is a list of allies.
	 */
	List<Pokemon> ally;

	/**
	 * Pokemon enemies.
	 */
	List<Pokemon> foes;
	/**
	 * berries in world.
	 */
	List<OranBerry> berries;

	/**
	 * Number of steps!
	 */
	int stepsTaken;
	/**
	 * number of foes in the world
	 */
	int pokemonInWorld;
	/**
	 * the last x and y of the player
	 */
	int lastX;
	int lastY;

	/**
	 * the max and min number of rooms.
	 */
	final int max = 8;
	final int min = 5;
	/**
	 * number of rooms in a level
	 */
	int num_rooms;
	/**
	 * which floor are you on?
	 */
	int floorCounter;
	/**
	 * tracks if the game is lost (if player or ally faints)
	 */
	boolean lostGame = false;

	/**
	 * Create a PokemonGame of a particular size.
	 * 
	 * @param w     how wide is the grid?
	 * @param h     how tall is the grid?
	 * @param floor what floor is it on?
	 */

	public PokemonGame(int w, int h, int floor) {

		floorCounter = floor;
		world = new World(w, h);
		Random rand = new Random();
		int num_rooms = rand.nextInt(max - min) + min;
		ally = new ArrayList<Pokemon>();
		foes = new ArrayList<Pokemon>();
		berries = new ArrayList<OranBerry>();
		// fills the whole world with walls.

		for (int i = 0; i < 900; i++) {
			Wall wall = new Wall(world);
			world.insertRandomly(wall);
		}
		// spacesToClear tracks rooms to clear
		ArrayList<Tile> spacesToClear = new ArrayList();
		// paths tracks tiles at the center of rooms
		ArrayList<Tile> paths = new ArrayList();
		// pathways tracks tiles to clear to create pathways.
		ArrayList<Tile> pathways = new ArrayList();
		for (int i = 0; i <= num_rooms; i++) {
			Tile tile = new Tile(rand.nextInt(25) + 3, rand.nextInt(25) + 3);
			// I found that the maps are more interesting if you force them to be more
			// spread out,
			// So there's two rooms that will mostly always be in the same place.
			if (i == 0) {
				tile = new Tile(rand.nextInt(6) + 3, rand.nextInt(6) + 3);
			}
			if (i == 1) {
				tile = new Tile(rand.nextInt(6) + 20, rand.nextInt(6) + 20);
			}

			paths.add(tile);
			// creates a room and adds it to spaces to clear

			// sometimes, rooms/paths merge! I'm okay with that, since it generates some
			// rooms that are more interesting.
			// in fact, it generates some rooms that look suspiciously similar to PMD
			// red/blue rooms.
			// really makes you think.
			ArrayList<Tile> clearSpaces = tile.sizeThree();
			spacesToClear.addAll(clearSpaces);

			// remove tiles in spaces to clear.
			for (Tile t : spacesToClear) {
				int tileX = t.x;
				int tileY = t.y;
				List<WorldObject> removethese = world.find(tileX, tileY);
				for (WorldObject thing : removethese) {
					world.remove(thing);

				}
			}

		}
		// shuffle the center tiles.
		Collections.shuffle(paths);
		// generate a binary tree out of the tiles.
		TileTree gameMap = new TileTree(paths);
		// get the list of tiles to create paths.
		pathways.addAll(gameMap.returnMap());
		// connect two random rooms.
		Tile tile1 = paths.get(rand.nextInt(paths.size()));
		Tile tile2 = paths.get(rand.nextInt(paths.size()));
		pathways.addAll(tile1.clearPath(tile2));
		// insert stairs.
		stairs = world.insertStairs();
		// Make the player out of the 0th sprite.
		player = new Pokemon(0, world);
		// Start the player randomly.
		world.insertRandomly(player);
		player.markAsPlayer();
		// add some berries!
		int num_berries = rand.nextInt(1) + 1;
		for (int i = 0; i < num_berries; i++) {
			OranBerry berry = new OranBerry(world);
			world.insertRandomly(berry);
			berries.add(berry);
		}
		// note the players current predictions
		this.lastX = player.getX();
		this.lastY = player.getY();
		world.register(player);
		// make an ally.
		Pokemon friend = world.insertPokemonRandomly(1);
		// remove any objects from above the player and move the ally there.
		List<WorldObject> things = world.find(player.getX(), player.getY() - 1);
		for (WorldObject thing : things) {
			if (thing.isWall) {
				world.remove(thing);
			}
		}
		friend.setPosition(player.getX(), player.getY() - 1);
		ally.add(friend);
		friend.markAsAlly();

		// Generate some random foes
		this.pokemonInWorld = rand.nextInt(3) + 1;
		for (int ft = 0; ft < pokemonInWorld + 1; ft++) {
			int id = rand.nextInt(4) + 2;
			Pokemon foe = world.insertPokemonRandomly(id);
			foes.add(foe);
		}

		// now that everything important is created in rooms, clear some paths.
		for (Tile t : pathways) {
			int tileX = t.x;
			int tileY = t.y;
			List<WorldObject> removethese = world.find(tileX, tileY);
			for (WorldObject thing : removethese) {
				if (thing.isWall) {
					world.remove(thing);
				}
			}
		}
		// hide the map
		for (int x = 0; x < 30; x++) {
			for (int y = 0; y < 30; y++) {
				VisibilitySquare dark = new VisibilitySquare(world, false);
				dark.setPosition(x, y);
				world.register(dark);
			}
		}
		// step once to clear the players visibility
		world.stepAll();
	}

	/**
	 * creates a menu with the player's inventory
	 * 
	 * @returns the menu
	 */
	public Menu makeMenu() {
		Map inventory = player.inventory;
		Menu menu = new Menu(world, player.inventory);
		menu.setPosition(player.getX(), player.getY());
		world.register(menu);
		return menu;

	}

	/**
	 * Choose the object!
	 * 
	 * @param menu-   what are you selecting from?
	 * @param Choice- are you using it or exiting?
	 * @returns the name of the item used, if any.
	 */
	public void chooseMenu(Menu menu, boolean Choice) {
		String object = menu.choose(Choice);
		if (object != null) {
			player.inventory.put(object, player.inventory.get(object) - 1);
			player.eatOranBerry();
		}
	}

	/**
	 * This method is how the Main app tells whether we're done.
	 * 
	 * @return true if the player has reached the stairs.
	 */
	public boolean gameOver() {
		return player.inSameSpot(stairs);
	}

	/**
	 * I wanted a better game winning screen, so this is a method to make a prettier
	 * game over screen for winning. Confetti! Maybe be careful if flashing images
	 * are bad for you though.
	 */
	public void gameWon() {
		// remove previous squares (so when it repeatedly runs, you don't keep adding
		// more and more)
		ArrayList<WorldObject> toRemove = new ArrayList<>();
		for (WorldObject item : world.viewItems()) {
			if (item instanceof VisibilitySquare) {
				toRemove.add(item);
			}
		}
		world.removeAll(toRemove);
		// makes a white screen with some colored squares.
		for (int x = 0; x < 30; x++) {
			for (int y = 0; y < 30; y++) {
				VisibilitySquare confetti = new VisibilitySquare(world, true);
				confetti.setPosition(x, y);
				world.register(confetti);
			}
		}
	}

	/**
	 * Update positions of everything (the user has just pressed a button).
	 */
	public void step() {
		ArrayList<WorldObject> goneBerries = new ArrayList<>();
		// picks up berries in the same spot as the player or ally.
		for (OranBerry berry : berries) {
			if (berry.inSameSpot(this.player) || berry.inSameSpot(this.ally.get(0))) {
				goneBerries.add(berry);
				this.player.inventory.put("Oran Berry", this.player.inventory.get("Oran Berry") + 1);
			}
		}
		world.removeAll(goneBerries);
		this.stepsTaken += 1;
		// every five turns, the player and ally heal.
		if (this.stepsTaken % 5 == 0 && this.player.health < 30) {
			this.player.health++;

		}
		if (this.ally.get(0).health < 30 && this.stepsTaken % 5 == 0) {
			this.ally.get(0).health++;
		}
		// make the ally face the player.

		if (this.player.getX() > this.ally.get(0).getX()) {
			this.ally.get(0).lastMove = "right";
		} else if (this.player.getX() < this.ally.get(0).getX()) {
			this.ally.get(0).lastMove = "left";
		} else if (this.player.getY() > this.ally.get(0).getY()) {
			this.ally.get(0).lastMove = "down";
		} else if (this.player.getY() < this.ally.get(0).getY()) {
			this.ally.get(0).lastMove = "up";
		}

		// let the other pokemon make moves.
		otherTurns();
		// every seven turns, there's a chance that a fallen pokemon will return.
		if (pokemonInWorld < 1 && this.stepsTaken % 7 == 0) {
			Random rand = new Random();
			double check = rand.nextDouble();
			if (check < .2) {
				int id = rand.nextInt(4) + 2;
				Pokemon foe = world.insertPokemonRandomly(id);
				foes.add(foe);
				pokemonInWorld++;
			}
		}
		world.stepAll();
	}

	/**
	 * NPCs have their turns.
	 */
	private void otherTurns() {
		// any allies take their turn.
		for (Pokemon friend : ally) {
			// tracks if they use their turn to attack.
			boolean attacked = false;
			// finds the player's location
			int destX = this.player.getX();
			int destY = this.player.getY();
			// looks at each foe.
			for (Pokemon target : foes) {
				int foeX = target.getX();
				int foeY = target.getY();
				// if one is nearby and the ally hasn't switched places with the player, it
				// attacks it, marks attacked as true.
				if (((Math.abs(friend.getX() - foeX) == 1 && friend.getY() - foeY == 0)
						|| (Math.abs(friend.getY() - foeY) == 1 && friend.getX() - foeX == 0))
						&& (friend.getX() != destX || friend.getY() != destY)) {
					friend.attack(target);
					attacked = true;
					break;
				}
			}

			// if not attacked and it can't find its friend, it moves randomly.
			if ((Math.abs(friend.getX() - destX) > 5 || Math.abs(friend.getY() - destY) > 5) && attacked == false) {
				friend.moveRandomly();
			}
			// if it sees its friend, it moves towards it. if its friend moves onto its
			// space, they switch places.
			else if (attacked == false) {
				if (friend.getX() > destX) {
					friend.moveLeft();
				} else if (friend.getX() < destX) {
					friend.moveRight();
				}
				if (friend.getY() < destY) {
					friend.moveDown();
				} else if (friend.getY() > destY) {
					friend.moveUp();
				} else if (friend.getY() == destY && friend.getX() == destX) {
					friend.setPosition(this.lastX, this.lastY);
				}
			}
			// it updates the players last position.
			this.lastX = destX;
			this.lastY = destY;
		}
		ArrayList<Pokemon> gone = new ArrayList<>();
		// for every foe:
		for (Pokemon lost : foes) {
			// checks if its fainted, if so, adds to a remove list
			if (lost.fainted == true) {
				world.remove(lost);
				gone.add(lost);
				pokemonInWorld--;
				continue;
			}
			// checks if its near a player or an ally. priority is to attack the player if
			// possible.
			int destX = this.player.getX();
			int destY = this.player.getY();
			int allyX = this.ally.get(0).getX();
			int allyY = this.ally.get(0).getY();
			if ((Math.abs(lost.getX() - destX) == 1 && lost.getY() - destY == 0)
					|| (Math.abs(lost.getY() - destY) == 1 && lost.getX() - destX == 0)) {
				lost.attack(player);
				// if the player faints, game is lost.
				if (player.fainted == true) {
					lostGame = true;
					world.lost = true;
					for (int x = 0; x < 30; x++) {
						for (int y = 0; y < 30; y++) {
							VisibilitySquare dark = new VisibilitySquare(world, false);
							dark.setPosition(x, y);
							world.register(dark);
						}
					}
				}
			}
			// attacks the ally if nearby
			else if ((Math.abs(lost.getX() - allyX) == 1 && lost.getY() - allyY == 0)
					|| (Math.abs(lost.getY() - allyY) == 1 && lost.getX() - allyX == 0)) {
				lost.attack(ally.get(0));
				// if the ally faints, you also lose.
				if (ally.get(0).fainted == true) {
					lostGame = true;
					world.lost = true;
					for (int x = 0; x < 30; x++) {
						for (int y = 0; y < 30; y++) {
							VisibilitySquare dark = new VisibilitySquare(world, false);
							dark.setPosition(x, y);
							world.register(dark);
						}
					}
				}
			}
			// otherwise, it moves.
			else {
				// if it doesnt see the player or ally, randomly
				if ((Math.abs(lost.getX() - destX) > 5 || Math.abs(lost.getY() - destY) > 5)
						&& (Math.abs(lost.getX() - allyX) > 5 || Math.abs(lost.getY() - allyY) > 5)) {
					lost.moveRandomly();
				}
				// if it does, towards the player
				else if (Math.abs(lost.getX() - destX) <= 5 && Math.abs(lost.getY() - destY) <= 5) {
					if (lost.getX() > destX) {
						lost.moveLeft();
					} else if (lost.getX() < destX) {
						lost.moveRight();
					}
					if (lost.getY() < destY) {
						lost.moveDown();
					} else if (lost.getY() > destY) {
						lost.moveUp();
					}
				}
				// or after that, the ally
				else if (Math.abs(lost.getX() - allyX) <= 5 && Math.abs(lost.getY() - allyY) <= 5) {
					if (lost.getX() > allyX) {
						lost.moveLeft();
					} else if (lost.getX() < allyX) {
						lost.moveRight();
					}
					if (lost.getY() < allyY) {
						lost.moveDown();
					} else if (lost.getY() > allyY) {
						lost.moveUp();
					}
				}
			}
		}
		// remove the fainted foes.
		foes.removeAll(gone);
	}
}
