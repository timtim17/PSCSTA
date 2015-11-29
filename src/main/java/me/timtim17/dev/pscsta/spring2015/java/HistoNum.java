package me.timtim17.dev.pscsta.spring2015.java;

import java.io.File;
import java.io.FileNotFoundException;
import java.util.HashMap;
import java.util.Scanner;

public class HistoNum {
    public static void main(String[] args) throws Exception {
        // Get input
        Scanner input;
        try {
            // try to get USB data
            input = new Scanner(new File("X:\\" + "HistoNum.dat"));
        } catch (NullPointerException | FileNotFoundException e) {
            try {
                // no USB found, try to get student data
                input = new Scanner(HistoNum.class.getClassLoader().getResourceAsStream("HistoNum.dat"));
            } catch (NullPointerException er) {
                // neither could be found, throw an exception
                throw new Exception("Couldn't get data: check your file paths!");
            }
        }

        // Parse the data
        HashMap<Integer, Integer> numbers = new HashMap<>();
        for (int i = 0; i < 10; i++) {
            numbers.put(i, 0);
        }

        while (input.hasNext()) {
            char[] line = input.nextLine().toCharArray();
            for (char c : line) {
                int n = Integer.valueOf(((Character) c).toString());
                numbers.replace(n, numbers.get(n) + 1);
            }
        }

        for (int i = 0; i < 10; i++) {
            int occ = numbers.get(i);
            if (occ > 0) {
                System.out.print(i + "|");
                for (int j = 0; j < occ; j++)
                    System.out.print("*");
                System.out.println(" {" + occ + "}");
            }
        }

        // Close the file
        input.close();
    }
}
