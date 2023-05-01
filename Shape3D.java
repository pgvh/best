package com.imnavot.objects;

import java.awt.Graphics;
import java.util.ArrayList;



public abstract class Shape3D {
	public ArrayList<Polygon> polygons;
	
	public abstract void draw(Graphics g);
	
	public Shape3D(ArrayList<Polygon> _polygons)
	{
		polygons = new ArrayList<Polygon>(_polygons);
	}
}
