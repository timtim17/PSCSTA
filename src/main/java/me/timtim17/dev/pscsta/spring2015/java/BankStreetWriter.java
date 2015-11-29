package me.timtim17.dev.pscsta.spring2015.java;

import java.io.File;
import java.io.FileNotFoundException;
import java.util.Scanner;

public class BankStreetWriter {
    public static void main(String[] args) throws Exception {
        // Get input
        Scanner input;
        try {
            // try to get USB data
            input = new Scanner(new File("X:\\bank.dat"));
        } catch (NullPointerException | FileNotFoundException e) {
            try {
                // no USB found, try to get student data
                input = new Scanner(BankStreetWriter.class.getClassLoader().getResourceAsStream("bank.dat"));
            } catch (NullPointerException er) {
                // neither could be found, throw an exception
                throw new Exception("Couldn't get data: check your file paths!");
            }
        }

        // Parse the data
        int n = input.nextInt();
        input.nextLine();   // throwaway \n before data sets
        for (int i = 0; i < n; i++) {
            String originalString = input.nextLine();
            int commands = input.nextInt();
            input.nextLine();   // throwaway \n before commands
            for (int j = 0; j < commands; j++) {
                String[] c = input.nextLine().split(" ");
                switch (c[0]) {
                    case "SEARCH":
                        char searchChar = c[2].charAt(0);
                        boolean found = false;
                        for (int k = Integer.valueOf(c[1]) - 1; k < originalString.length(); k++) {
                            if (originalString.charAt(k) == searchChar) {
                                System.out.println(k + 1);
                                found = true;
                                break;
                            }
                        }
                        if (!found) System.out.println("-1");
                        break;
                    case "DELETE":
                        int a = Integer.valueOf(c[1]) - 1, b = Integer.valueOf(c[2]);
                        System.out.println(originalString.substring(0, a) + originalString.substring(a + b));
                        break;
                    case "REPLACE":
                        int d = Integer.valueOf(c[1]) - 1;
                        System.out.println(originalString.substring(0, d) + c[2] + originalString.substring(d + 1));
                        break;
                    case "INSERT":
                        int e = Integer.valueOf(c[1]) - 1;
                        String z = c[2];
                        if (c.length > 3) {
                            for (int y = 3; y < c.length; y++) {
                                z += " " + c[y];
                            }
                        }
                        System.out.println(originalString.substring(0, e) + z + " " + originalString.substring(e));
                        originalString = originalString.substring(0, e) + z + " " + originalString.substring(e);
                }
            }
        }

        // Close the file
        input.close();
    }
}
