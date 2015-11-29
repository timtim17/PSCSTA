package me.timtim17.dev.pscsta.spring2015.java;

import java.io.File;
import java.io.FileNotFoundException;
import java.util.Scanner;

public class Buoyancy {
    public static void main(String[] args) throws Exception {
        // Get input
        Scanner input;
        try {
            // try to get USB data
            input = new Scanner(new File("X:\\" + "Buoyancy.dat"));
        } catch (NullPointerException | FileNotFoundException e) {
            try {
                // no USB found, try to get student data
                input = new Scanner(Buoyancy.class.getClassLoader().getResourceAsStream("Buoyancy.dat"));
            } catch (NullPointerException er) {
                // neither could be found, throw an exception
                throw new Exception("Couldn't get data: check your file paths!");
            }
        }

        // Parse the data
        int n = input.nextInt();
        input.nextLine();   // throwaway \n before data sets
        for (int i = 0; i < n; i++) {
            float bLiters = input.nextFloat();
            float bNewt = bLiters * 0.011F;
            int balloons = 0;
            while (bNewt * balloons < 0.54) {
                balloons++;
            }

            System.out.println(balloons);
        }

        // Close the file
        input.close();
    }
}
