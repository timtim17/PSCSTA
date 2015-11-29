package me.timtim17.dev.pscsta.spring2015.java;

import java.io.File;
import java.io.FileNotFoundException;
import java.util.Scanner;

public class Cross {
    public static void main(String[] args) throws Exception {
        // Get input
        Scanner input;
        try {
            // try to get USB data
            input = new Scanner(new File("X:\\" + "Cross.dat"));
        } catch (NullPointerException | FileNotFoundException e) {
            try {
                // no USB found, try to get student data
                input = new Scanner(Cross.class.getClassLoader().getResourceAsStream("Cross.dat"));
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
            String hWord = line[0], vWord = line[2];
            int hIndex = 0, vIndex = 0;

            boolean done = false;
            for (int j = 0; j < hWord.length(); j++) {
                for (int k = 0; k < vWord.length(); k++) {
                    if (hWord.charAt(j) == vWord.charAt(k)) {
                        hIndex = j;
                        vIndex = k;
                        done = true;
                        break;
                    }
                }
                if (done) break;
            }

            if (done) {
                for (int j = 0; j < vWord.length(); j++) {
                    if (j == vIndex) {
                        System.out.println(hWord);
                    } else {
                        for (int k = 0; k < hIndex; k++) {
                            System.out.print(' ');
                        }
                        System.out.println(vWord.charAt(j));
                    }
                }
            } else {
                System.out.println("none");
            }

            System.out.println();
        }

        // Close the file
        input.close();
    }
}
