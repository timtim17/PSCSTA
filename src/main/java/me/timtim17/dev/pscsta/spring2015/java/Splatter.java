package me.timtim17.dev.pscsta.spring2015.java;

import java.io.File;
import java.io.FileNotFoundException;
import java.util.Scanner;

public class Splatter {
    private static final int[][] transformations = {{0, 0}, {1, 0}, {2, 0}, {-1, 0}, {-2, 0}, {0, 1}, {0, 2}, {0, -1}, {0, -2}, {1, 1}, {-1, 1}, {1, -1}, {-1, -1}};

    public static void main(String[] args) throws Exception {
        // Get input
        Scanner input;
        try {
            // try to get USB data
            input = new Scanner(new File("X:\\" + "Splatter.dat"));
        } catch (NullPointerException | FileNotFoundException e) {
            try {
                // no USB found, try to get student data
                input = new Scanner(Splatter.class.getClassLoader().getResourceAsStream("Splatter.dat"));
            } catch (NullPointerException er) {
                // neither could be found, throw an exception
                throw new Exception("Couldn't get data: check your file paths!");
            }
        }

        // Parse the data
        int n = input.nextInt();
        input.nextLine();   // throwaway \n before data sets
        for (int i = 0; i < n; i++) {
            String[] size_line = input.nextLine().split(" ");
            int[] size = new int[2];
            size[0] = Integer.valueOf(size_line[0]);
            size[1] = Integer.valueOf(size_line[1]);

            int num_coords = input.nextInt();
            input.nextLine();   // throwaway \n before coords

            int[][] coords = new int[num_coords][2];

            for (int j = 0; j < num_coords; j++) {
                String[] coord_line = input.nextLine().split(" ");
                int[] coord = new int[2];
                coord[0] = Integer.valueOf(coord_line[0]);
                coord[1] = Integer.valueOf(coord_line[1]);

                coords[j] = coord;
            }

            boolean[][] wall = new boolean[size[0]][size[1]];

            for (int[] coord : coords) {
                for (int[] tf : transformations) {
                    int[] new_coord = {coord[0] + tf[0], coord[1] + tf[1]};
                    if (!(new_coord[0] < 0 || new_coord[0] > size[0] - 1 || new_coord[1] < 0 || new_coord[1] > size[1] - 1))
                        wall[new_coord[0]][new_coord[1]] = true;
                }
            }

            boolean covered = true;

            for (boolean[] row : wall) {
                for (boolean z : row) {
                    if (!z) covered = false;
                }
            }

            System.out.println(covered ? "YES" : "NO");
        }

        // Close the file
        input.close();
    }
}
