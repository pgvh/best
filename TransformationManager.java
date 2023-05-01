package com.imnavot.managers;

import java.util.ArrayList;

import com.imnavot.objects.*;

public class TransformationManager {
	
	public class ScaleFactor
	{
		public double x;
		public double y;
		public double z;
		
		public ScaleFactor()
		{
			this(1,1,1);
		}
		
		public ScaleFactor(double _x, double _y, double _z)
		{
			x = _x;
			y = _y;
			z = _z;
		}
	}
	
	public enum rotateAbout {
		rotateAboutX, rotateAboutY, rotateAboutZ
	};
	
	public ArrayList<Point3D> scale(ArrayList<Point3D> points, ScaleFactor factor)
	{
		ArrayList<Point3D> newPoints = new ArrayList<Point3D>();
		Point3D newPoint = null;
		for (Point3D p : points)
        {
            newPoint = new Point3D(p.x*factor.x, p.y*factor.y, p.z*factor.z);
            newPoints.add(newPoint);
        }
		
		return newPoints;
	}
	
	public ArrayList<Point3D> rotate(ArrayList<Point3D> points, double theta, rotateAbout direction)
	{
		double cos = Math.cos(Math.PI / 180 * theta);
		double sin = Math.sin(Math.PI / 180 * theta);
		ArrayList<Point3D> newPoints = new ArrayList<Point3D>();
		double x=0;
		double y=0;
		double z=0;
		
		for (Point3D p : points)
		{
			switch (direction)
			{
			case rotateAboutX:
				y = (p.y * cos) - (p.z * sin);
				z = (p.y * sin) + (p.z * cos);
				newPoints.add(new Point3D(p.x, y, z));
				break;
			case rotateAboutY:
				x = (p.x * cos) - (p.z * sin);
				z = (p.x * sin) + (p.z * cos);
				newPoints.add(new Point3D(x, p.y, z));
				break;
			case rotateAboutZ:
				x = (p.x * cos) - (p.y * sin);
				y = (p.x * sin) + (p.y * cos);
				newPoints.add(new Point3D(x, y, p.z));
				break;
			}
		}
		return newPoints;
	}
}
