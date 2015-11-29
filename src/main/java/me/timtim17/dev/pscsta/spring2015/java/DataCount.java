package me.timtim17.dev.pscsta.spring2015.java;

import java.io.File;
import java.io.FileNotFoundException;
import java.util.Scanner;

public class DataCount {
    public static void main(String[] args) throws Exception {
        // Parse the data
        String[] fileNames = {"accounting", "bank", "buoyancy", "cross", "cursed", "determined1", "determined2", "drought", "histonum", "shuffle", "sineup", "splatter"};
        int numLines = 0;
        for (String name : fileNames) {
            Scanner input = loadFile(name);
            while (input.hasNext()) {
                input.nextLine();
                numLines++;
            }
            input.close();
        }
        System.out.println("THERE ARE " + numLines + " LINES OF DATA FOR THIS PACKET");
    }

    public static Scanner loadFile(String name) throws Exception {
        // Get input
        Scanner input;
        try {
            // try to get USB data
            input = new Scanner(new File("X:\\" + name + ".dat"));
        } catch (NullPointerException | FileNotFoundException e) {
            try {
                // no USB found, try to get student data
                input = new Scanner(DataCount.class.getClassLoader().getResourceAsStream(name + ".dat"));
            } catch (NullPointerException er) {
                // neither could be found, throw an exception
                throw new Exception("Couldn't get data: check your file paths!");
            }
        }
        return input;
    }
}
