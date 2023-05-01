package com.imnavot.objects;

import java.awt.Graphics;
import java.util.ArrayList;

public class Pyramid extends Shape3D {

	public Pyramid(ArrayList<Polygon> _polygons)
	{
		super(_polygons);
	}

	@Override
	public void draw(Graphics g) {

		for (Polygon poly : polygons)
		{
			poly.isVisible();
			poly.draw(g);
		}
	}

}
