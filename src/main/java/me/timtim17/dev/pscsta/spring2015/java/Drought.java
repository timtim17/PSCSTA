package me.timtim17.dev.pscsta.spring2015.java;

import java.io.File;
import java.io.FileNotFoundException;
import java.util.Scanner;

public class Drought {
    public static void main(String[] args) throws Exception {
        // Get input
        Scanner input;
        try {
            // try to get USB data
            input = new Scanner(new File("X:\\" + "Drought.dat"));
        } catch (NullPointerException | FileNotFoundException e) {
            try {
                // no USB found, try to get student data
                input = new Scanner(Drought.class.getClassLoader().getResourceAsStream("Drought.dat"));
            } catch (NullPointerException er) {
                // neither could be found, throw an exception
                throw new Exception("Couldn't get data: check your file paths!");
            }
        }

        // Parse the data
        int n = input.nextInt();
        input.nextLine();   // throwaway \n before data sets
        for (int i = 0; i < n; i++) {
            String[] line = input.nextLine().split(" ");
            float annual = Float.valueOf(line[0]);
            float[] nums = new float[line.length - 1];
            for (int j = 1; j < line.length; j++) {
                nums[j - 1] = Float.valueOf(line[j]);
            }

            float sum1 = 0;
            for (int j = 0; j < 12; j++) {
                sum1 += nums[j];
            }

            float sum2 = 0;
            for (int j = 12; j < 24; j++) {
                sum2 += nums[j];
            }

            if (sum1 >= 2 * annual && sum2 >= 2 * annual) {
                System.out.println("drought over");
            } else if (sum1 >= annual && sum2 >= annual) {
                System.out.println("improving");
            } else {
                System.out.println("continuing");
            }
        }

        // Close the file
        input.close();
    }
}
