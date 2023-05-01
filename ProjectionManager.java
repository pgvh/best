package com.imnavot.managers;

import java.awt.Point;
import java.util.ArrayList;

import com.imnavot.objects.Point3D;

public class ProjectionManager
{
	
	public enum Projection {
		realistic, diagonal, parallel
	};
	
	int xAxis = 400;
    int yAxis = 400;       
    int zAxis = 400;
    int veiwerDistance = 200;
	
	public ArrayList<Point> realisticProjection(ArrayList<Point3D> points3D)
	{
		double factor;
		double newX;
		double newY;
		ArrayList<Point> points2D = new ArrayList<Point>();
		
		for (Point3D p3d : points3D)
		{
			factor = 1 / (1 + ((p3d.z) / (zAxis + veiwerDistance)));

			newX = (p3d.x * factor) + xAxis;
			newY = (p3d.y * factor) + yAxis;

			points2D.add(new Point((int)newX,(int)newY));
			
		} 
		
		return points2D;
	}
	
	public ArrayList<Point> DiagonalProjection(ArrayList<Point3D> points3D)
    {
        double cosA = Math.cos(Math.PI / 4);
        double sinA = Math.sin(-Math.PI / 4);
        

        ArrayList<Point> points2D = new ArrayList<Point>();
        double newX;
        double newY;

        for (Point3D p3d : points3D)
        {
            newX = (p3d.x + (0.5 * (p3d.z) * cosA)) + xAxis;
            newY = (p3d.y + (0.5 * (p3d.z) * sinA)) + yAxis;

            points2D.add(new Point((int)newX,(int)newY));
        }
        
        return points2D;
    }
	
	public ArrayList<Point> ParallelProjection(ArrayList<Point3D> points3D)
    {
		ArrayList<Point> points2D = new ArrayList<Point>();
		for (Point3D p3d : points3D)
        {   
            points2D.add(new Point((int)p3d.x + xAxis,(int)p3d.y + yAxis));
        }
		return points2D;
    }
}

