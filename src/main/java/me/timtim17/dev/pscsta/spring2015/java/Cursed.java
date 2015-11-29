package me.timtim17.dev.pscsta.spring2015.java;

import java.io.File;
import java.io.FileNotFoundException;
import java.util.HashMap;
import java.util.Objects;
import java.util.Scanner;

public class Cursed {
    public static void main(String[] args) throws Exception {
        // Get input
        Scanner input;
        try {
            // try to get USB data
            input = new Scanner(new File("X:\\" + "Cursed.dat"));
        } catch (NullPointerException | FileNotFoundException e) {
            try {
                // no USB found, try to get student data
                input = new Scanner(Cursed.class.getClassLoader().getResourceAsStream("Cursed.dat"));
            } catch (NullPointerException er) {
                // neither could be found, throw an exception
                throw new Exception("Couldn't get data: check your file paths!");
            }
        }

        HashMap<String, Integer> months = new HashMap<>();
        months.put("January", 1);
        months.put("February", 2);
        months.put("March", 3);
        months.put("April", 4);
        months.put("May", 5);
        months.put("June", 6);
        months.put("July", 7);
        months.put("August", 8);
        months.put("September", 9);
        months.put("October", 10);
        months.put("November", 11);
        months.put("December", 12);

        // Parse the data
        while (input.hasNext()) {
            String[] date = input.nextLine().split(" ");
            String month = pad(String.valueOf(months.get(date[0])), 2);
            String day = pad(date[1].substring(0, date[1].length() - 1), 2);
            String year = pad(date[2], 4);
            String dateString = month + day + year;
            System.out.print(dateString + ": ");
            if (dateString.equals(reverse(dateString)))
                System.out.println("DON'T TRAVEL");
            else
                System.out.println("OK TO TRAVEL");
        }

        // Close the file
        input.close();
    }

    private static String pad(String input, int maxLength) {
        StringBuilder newString = new StringBuilder();
        int i = input.length();
        while (i < maxLength) {
            newString.append("0");
            i++;
        }
        newString.append(input);
        return newString.toString();
    }

    private static String reverse(String original) {
        char[] arr = original.toCharArray();
        StringBuilder newString = new StringBuilder();
        for (int i = arr.length - 1; i >= 0; i--) {
            newString.append(arr[i]);
        }
        return newString.toString();
    }
}
