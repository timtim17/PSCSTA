package me.timtim17.dev.pscsta.spring2015.java;

import java.io.File;
import java.io.FileNotFoundException;
import java.util.ArrayList;
import java.util.Scanner;

public class Accounting {
    public static void main(String[] args) throws Exception {
        // Get input
        Scanner input;
        try {
            // try to get USB data
            input = new Scanner(new File("X:\\" + "Accounting.dat"));
        } catch (NullPointerException | FileNotFoundException e) {
            try {
                // no USB found, try to get student data
                input = new Scanner(Accounting.class.getClassLoader().getResourceAsStream("Accounting.dat"));
            } catch (NullPointerException er) {
                // neither could be found, throw an exception
                throw new Exception("Couldn't get data: check your file paths!");
            }
        }

        // Parse the data
        printHeader();

        ArrayList<Double> amounts = new ArrayList<>();
        while (input.hasNext()) {
            String amount = String.join("", input.nextLine().replace(',', ' ').split(" "));
            double a;
            if (amount.charAt(1) == '(') {
                a = -1 * Double.valueOf(amount.substring(2, amount.length() - 1));
            } else {
                a = Double.valueOf(amount.substring(1));
            }
            amounts.add(a);
        }

        System.out.println("       Transaction : Balance");

        double balance = 0;
        for (double amount : amounts) {
            balance += amount;
            String amountVal = format(amount);
            for (int i = 0; i < -(amountVal.length() - 11) + 7; i++) {
                System.out.print(" ");
            }
            System.out.println(amountVal + " : " + format(balance));
        }

        printHeader();

        // Close the file
        input.close();
    }

    /*
    def format(cost):
        if cost < 0:
            return "$(%s)" % comma(-cost)
        else:
            return "$%s" % comma(cost)
    def comma(cost):
        cost = str(cost)
        pennies = cost[cost.index("."):]
        if len(pennies) == 2:
            pennies += "0"
        cost = cost[:cost.index(".")]
        if len(cost) <= 3:
            return cost + pennies
        else:
            for i in range(len(cost) - 3, 0, -3):
                cost = cost[:i] + "," + cost[i:]
            return cost + pennies
    for price in costs:
        balance += price
        print "%18s : %-20s" % (format(price), format(balance))

     */

    private static String format(double amount) {
        if (amount < 0) {
            return "$(" + comma(-amount) + ")";
        } else {
            return "$" + comma(amount);
        }
    }

    private static String comma(double amount) {
        String cost = String.valueOf(amount);
        String pennies = "." + (Math.round(Double.valueOf(cost.substring(cost.indexOf("."))) * 100));
        if (pennies.length() == 2)
                pennies += "0";
        cost = cost.substring(0, cost.indexOf("."));
        if (cost.length() > 3) {
            for (int i = cost.length() - 3; i >= 0; i -= 3) {
                cost = cost.substring(0, i) + "," + cost.substring(i);
            }
        }
        return cost + pennies;
    }

    private static void printHeader() {
        for (int i = 0 ; i < 8; i++) {
            System.out.print("****.");
        }
        System.out.println();
    }
}
