package com.imnavot.objects;

import java.awt.Color;
import java.awt.Graphics;
import java.awt.Point;
import java.util.ArrayList;
//import java.util.Comparator;
import java.util.Random;

public class Polygon /*implements Comparator<Polygon>*/ {
	public ArrayList<Point> points;
	public boolean isVisible;
	Random rand;
	
	public Polygon()
	{
		this(new ArrayList<Point>());
	}
	
	public Polygon(ArrayList<Point> _points)
	{
		points = new ArrayList<Point>(_points);
		rand = new Random();
	}
	
//	private double getMaxZ()
//	{
//		double maxZ = 0;
//		
//		for (Point3D point : points) {
//			maxZ = Math.max(maxZ, point.z);
//		}
//		
//		return maxZ;
//	}
	
	public void draw(Graphics g)
	{
		
		
		if (isVisible)
		{
			int[] xPoints = new int[points.size()];
			int[] yPoints = new int[points.size()];
			
			for (int i=0; i<points.size() ; i++)
			{
				xPoints[i] = (int) points.get(i).x;
				yPoints[i] = (int) points.get(i).y;
			}
			
			float r = rand.nextFloat();
			float green = rand.nextFloat();
			float b = rand.nextFloat();
			
			g.setColor(new Color(r,green,b));
			g.fillPolygon(xPoints, yPoints, points.size());
		}
	}
	
	public void isVisible()
	{
		Vector3D v1 = new Vector3D(points.get(1).x - points.get(0).x, points.get(1).y - points.get(0).y, 0);
		Vector3D v2 = new Vector3D(points.get(2).x - points.get(1).x, points.get(2).y - points.get(1).y, 0);
		
		Vector3D vec = Vector3D.cross(v1, v2);
		
		if (vec.getZ() < 0)
			isVisible = true;
        else
        	isVisible = false;
	}
	
//	@Override
//    public int compare(Polygon p1, Polygon p2) {
//        if(p1.getMaxZ() > p2.getMaxZ())
//        	return 1;
//        else if (p1.getMaxZ() < p2.getMaxZ())
//        	return -1;
//        else
//        	return 0;
//        			
//    }
}
