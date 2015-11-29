package me.timtim17.dev.pscsta.spring2015.java;

import java.util.Scanner;

public class PracticeProblem {
    public static void main(String[] args) {
        Scanner input = new Scanner(PracticeProblem.class.getClassLoader().getResourceAsStream("practiceproblem.dat"));
        int n = input.nextInt();
        input.nextLine();   // throwaway \n before data sets
        for (int i = 0; i < n; i++) {
            System.out.println("Let's play " + input.nextLine() + "!");
        }
        input.close();
    }
}
