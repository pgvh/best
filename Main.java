package com.imnavot;

import java.awt.Dimension;
import java.awt.Toolkit;

import javax.swing.JFrame;

import com.imnavot.GUI.MainWindow;

public class Main {

	
	public static void main(String[] args) {
		
		Dimension screenSize = Toolkit.getDefaultToolkit().getScreenSize();
		int width = (int)screenSize.getWidth();
		int height = (int)screenSize.getHeight();
		JFrame frame = new JFrame("3D Shapes");

		MainWindow panel = new MainWindow(width, height);

		frame.add(panel);
		frame.pack();
		frame.setVisible(true);
		frame.setResizable(true);
		frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
		frame.setSize(screenSize);
	}
}
