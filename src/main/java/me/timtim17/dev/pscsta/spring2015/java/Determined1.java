package me.timtim17.dev.pscsta.spring2015.java;

import java.io.File;
import java.io.FileNotFoundException;
import java.util.Scanner;

public class Determined1 {
    public static void main(String[] args) throws Exception {
        // Get input
        Scanner input;
        try {
            // try to get USB data
            input = new Scanner(new File("X:\\"));
        } catch (NullPointerException | FileNotFoundException e) {
            try {
                // no USB found, try to get student data
                input = new Scanner(Determined1.class.getClassLoader().getResourceAsStream("Determined1.dat"));
            } catch (NullPointerException er) {
                // neither could be found, throw an exception
                throw new Exception("Couldn't get data: check your file paths!");
            }
        }

        // Parse the data
        int n = input.nextInt();
        input.nextLine();   // throwaway \n before data sets
        for (int i = 0; i < n; i++) {
            String[][] line = {input.nextLine().split(" "), input.nextLine().split(" ")};
            int[][] matrix = new int[2][2];
            for (int j = 0; j < line.length; j++) {
                for (int k = 0; k < line[j].length; k++) {
                    matrix[j][k] = Integer.valueOf(line[j][k]);
                }
            }
            System.out.println((matrix[0][0] * matrix[1][1]) - (matrix[0][1] * matrix[1][0]));
        }

        // Close the file
        input.close();
    }
}
