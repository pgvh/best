package com.imnavot.objects;




public class Vector3D
{
	private double x;
	private double y;
	private double z;
	
	public double getX()
	{
		return x;
	}
	public void setX(double x)
	{
		this.x = x;
	}
	public double getY()
	{
		return y;
	}
	public void setY(double y)
	{
		this.y = y;
	}
	public double getZ()
	{
		return z;
	}
	public void setZ(double z)
	{
		this.z = z;
	}



	public Vector3D(double x, double y, double z)
	{
		super();
		this.x = x;
		this.y = y;
		this.z = z;
	}
	
	public static Vector3D cross( Vector3D v1, Vector3D v2 )
	{
		Vector3D vec = new Vector3D(v1.getY() * v2.getZ() - v1.getZ() * v2.getY(), v1.getZ() * v2.getX() - v1.getX() * v2.getZ(), v1.getX() * v2.getY() - v1.getY() * v2.getX());
		
		return vec;
	}
}
