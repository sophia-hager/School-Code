package MysteryDungeon;

import java.awt.Graphics2D;
import java.awt.image.BufferedImage;
import java.io.File;
import java.io.IOException;

import javax.imageio.ImageIO;
/**
 * @author sophiahager
 */
public class OranBerry extends WorldObject {
	/**
	 * What it looks like
	 */
	BufferedImage sprite;

	public OranBerry(World world) {
		super(world);
		try {
			sprite = ImageIO.read(new File("src/main/resources/Oran.png"));
		} catch (IOException e) {
			// TODO Auto-generated catch block
			e.printStackTrace();
		}

	}

	/**
	 * draw the berry.
	 */
	@Override
	public void draw(Graphics2D g) {
		Graphics2D scale = (Graphics2D) g.create();
		scale.scale(1.0 / 25, 1.0 / 25);
		scale.translate(-12, -8);
		scale.drawImage(sprite, 0, 0, null);
		scale.dispose();
	}

	@Override
	public void step() {
	}
}
