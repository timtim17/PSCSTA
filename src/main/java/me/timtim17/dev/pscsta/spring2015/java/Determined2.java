package me.timtim17.dev.pscsta.spring2015.java;

import java.io.File;
import java.io.FileNotFoundException;
import java.util.ArrayList;
import java.util.Scanner;

public class Determined2 {
    public static void main(String[] args) throws Exception {
        // Get input
        Scanner input;
        try {
            // try to get USB data
            input = new Scanner(new File("X:\\" + "Determined2.dat"));
        } catch (NullPointerException | FileNotFoundException e) {
            try {
                // no USB found, try to get student data
                input = new Scanner(Determined2.class.getClassLoader().getResourceAsStream("Determined2.dat"));
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
            int matrixSize = line.length;
            String[][] strMatrix = new String[matrixSize][matrixSize];
            strMatrix[0] = line;
            for (int j = 1; j < strMatrix.length; j++) {
                strMatrix[j] = input.nextLine().split(" ");
            }

            ArrayList<ArrayList<Integer>> matrix = new ArrayList<>();
            for (int l = 0; l < strMatrix.length; l++) {
                ArrayList<Integer> j = new ArrayList<>();
                for (int k = 0; k < strMatrix[l].length; k++) {
                    j.add(Integer.valueOf(strMatrix[l][k]));
                }
                matrix.add(j);
            }
            
            System.out.println(determinant(matrix));
        }

        // Close the file
        input.close();
    }


    /*
    def find_determinant(matrix):
        if len(matrix) == 2:
            return matrix[0][0] * matrix[1][1] - matrix[0][1] * matrix[1][0]
        else:
            returns = []
            for col in range(len(matrix)):
                m = []
                for row in range(1, len(matrix)):
                    r = []
                    for char in matrix[row][:col]:
                        r.append(char)
                    for char in matrix[row][col + 1:]:
                        r.append(char)
                    m.append(r)
                returns.append(find_determinant(m) * matrix[0][col])
            determinant = 0
            for i in range(len(returns)):
                if i % 2 == 0:
                    determinant += returns[i]
                else:
                    determinant -= returns[i]
            return determinant
     */
    private static int determinant(ArrayList<ArrayList<Integer>> matrix) {
        if (matrix.size() == 2)
            return (matrix.get(0).get(0) * matrix.get(1).get(1)) - (matrix.get(0).get(1) * matrix.get(1).get(0));
        else {
            ArrayList<Integer> returns = new ArrayList<>();
            for (int col = 0; col < matrix.size(); col++) {
                ArrayList<ArrayList<Integer>> m = new ArrayList<>();
                for (int row = 1; row < matrix.size(); row++) {
                    ArrayList<Integer> r = new ArrayList<>();
                    for (int c = 0; c < col; c++) {
                        r.add(matrix.get(row).get(c));
                    }
                    for (int c = col + 1; c < matrix.size(); c++) {
                        r.add(matrix.get(row).get(c));
                    }
                    m.add(r);
                }
                returns.add(determinant(m) * matrix.get(0).get(col));
            }
            int determinant = 0;
            for (int i = 0; i < returns.size(); i++) {
                if (i % 2 == 0)
                    determinant += returns.get(i);
                else
                    determinant -= returns.get(i);
            }
            return determinant;
        }
    }
}
