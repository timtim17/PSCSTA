package me.timtim17.dev.pscsta.spring2015.java;

import java.io.File;
import java.io.FileNotFoundException;
import java.util.Scanner;

public class SineUp {
    public static void main(String[] args) throws Exception {
        // Get input
        Scanner input;
        try {
            // try to get USB data
            input = new Scanner(new File("X:\\" + "SineUp.dat"));
        } catch (NullPointerException | FileNotFoundException e) {
            try {
                // no USB found, try to get student data
                input = new Scanner(SineUp.class.getClassLoader().getResourceAsStream("SineUp.dat"));
            } catch (NullPointerException er) {
                // neither could be found, throw an exception
                throw new Exception("Couldn't get data: check your file paths!");
            }
        }

        // Parse the data
        while (input.hasNext()) {
            String[] line = input.nextLine().split(" ");
            int[] nums = new int[3];
            for (int i = 0; i < line.length; i++) {
                nums[i] = Integer.valueOf(line[i]);
            }
            int diameter = nums[0];
            int angleADeg = nums[1], angleBDeg = nums[2], angleCDeg = 180 - angleADeg - angleBDeg;
            double angleARad = Math.toRadians(angleADeg), angleBRad = Math.toRadians(angleBDeg), angleCRad = Math.toRadians(angleCDeg);
            int sideA = (int) Math.round(diameter * Math.sin(angleARad)), sideB = (int) Math.round(diameter * Math.sin(angleBRad)), sideC = (int) Math.round(diameter * Math.sin(angleCRad));

            System.out.println("Circumcircle diameter = " + diameter);
            System.out.println("Angles are " + angleADeg + ", " + angleBDeg + " and " + angleCDeg);
            System.out.println("Corresponding sides are " + sideA + ", " + sideB + " and " + sideC);
        }

        // Close the file
        input.close();
    }
}
