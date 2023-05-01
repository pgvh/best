package com.imnavot.objects;

public class Point3D {
	public double x;
	public double y;
	public double z;
	
	public Point3D()
	{
		this(0,0,0);
	}
	
	public Point3D(double _x, double _y, double _z)
	{
		x = _x;
		y = _y;
		z = _z;
	}
	
	public double distance(Point3D other)
	{
		double deltaX = x - other.x;
		double deltaY = y - other.y;
		double deltaZ = z - other.z;
		
		return Math.sqrt(deltaX*deltaX + deltaY*deltaY + deltaZ*deltaZ);
	}
}
