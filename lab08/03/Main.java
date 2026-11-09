import java.util.List;
import java.util.ArrayList;
import java.util.Scanner;

public class Main {
    private static Boolean findFirstZeroInArray(int[][] matrix) {
        Boolean found = false;
        
        outerLoop:
        for (int[] row : matrix) {
            for (int j : row) {
                if (j == 0) {
                    found = true;
                    break outerLoop;
                }
            }
        }

        return found;
    }

    public static void main(String[] args) {
        int[][] testMatrix = {{1, 2, 3}, {-1, -2, -3}, {0, 99, 55}};

        System.out.println(findFirstZeroInArray(testMatrix));
    }
}