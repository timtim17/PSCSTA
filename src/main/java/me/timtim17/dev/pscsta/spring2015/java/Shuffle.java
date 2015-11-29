package me.timtim17.dev.pscsta.spring2015.java;

import java.io.File;
import java.io.FileNotFoundException;
import java.util.ArrayList;
import java.util.Collections;
import java.util.Scanner;

public class Shuffle {
    public static void main(String[] args) throws Exception {
        // Get input
        Scanner input;
        try {
            // try to get USB data
            input = new Scanner(new File("X:\\" + "Shuffle.dat"));
        } catch (NullPointerException | FileNotFoundException e) {
            try {
                // no USB found, try to get student data
                input = new Scanner(Shuffle.class.getClassLoader().getResourceAsStream("Shuffle.dat"));
            } catch (NullPointerException er) {
                // neither could be found, throw an exception
                throw new Exception("Couldn't get data: check your file paths!");
            }
        }

        // Parse the data
        while (input.hasNext()) {
            String[] line = input.nextLine().split(" ");
            ArrayList<String> words = new ArrayList<>();
            for (String word : line) {
                if (!words.contains(word)) {
                    words.add(word);
                }
            }
            Collections.sort(words);
            for (String word : words) {
                System.out.print(word + " ");
            }
            System.out.println();
        }

        // Close the file
        input.close();
    }
}
