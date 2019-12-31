package MysteryDungeon;

import java.util.ArrayList;

/**
 * @author sophiahager
 */

public class TileTree {
	/**
	 * size of the list to generate a tree
	 */
	int size;
	/**
	 * the root of the tree
	 */
	Node root;
	/**
	 * list of tiles to construct tree from
	 */
	ArrayList<Tile> tiles;

	public TileTree(ArrayList<Tile> tiles) {
		this.size = tiles.size() - 1;
		this.tiles = tiles;
		// generates the tree recursively
		this.root = treeFromList(this.tiles, 0, this.size);
	}

	/**
	 * recursive method to generate a tree. I looked at
	 * https://www.geeksforgeeks.org/sorted-array-to-balanced-bst/ when I got stuck
	 * on the base case
	 * 
	 * @param things- the list you construct it from
	 * @param start-  index you want to start at
	 * @param end-    index you want to end at
	 * @returns the tree (or rather, the root node of the tree)
	 */
	public Node treeFromList(ArrayList<Tile> things, int start, int end) {
		if (start > end) {
			return null;
		}
		int middle = (start + end) / 2;
		Tile rootTile = things.get(middle);
		Node root = new Node(rootTile, treeFromList(things, start, middle - 1), treeFromList(things, middle + 1, end));
		return root;
	}

	/**
	 * generates a list of tiles to form paths based on the root
	 * 
	 * @returns the list of tiles in the paths
	 */
	public ArrayList<Tile> returnMap() {
		return clearPathTree(this.root);
	}

	/**
	 * recursively generates a list of all tiles in paths
	 * 
	 * @param n - the node you're looking at
	 * @returns the list of path tiles
	 */
	public ArrayList<Tile> clearPathTree(Node n) {
		ArrayList<Tile> clearTheseTiles = new ArrayList<>();
		if (n.left != null) {
			Tile tile1 = n.value;
			Tile tile2 = n.left.value;
			clearTheseTiles.addAll(tile1.clearPath(tile2));
			clearTheseTiles.addAll(clearPathTree(n.left));
		}
		if (n.right != null) {
			Tile tile1 = n.value;
			Tile tile2 = n.right.value;
			clearTheseTiles.addAll(tile1.clearPath(tile2));
			clearTheseTiles.addAll(clearPathTree(n.right));
		}
		return clearTheseTiles;
	}

	/**
	 * Basic node-- don't really care about the parent
	 */
	private static class Node {
		public Node left;
		public Node right;
		public Tile value;

		public Node(Tile value, Node left, Node right) {
			this.value = value;
			this.left = left;
			this.right = right;
		}
	}
}
