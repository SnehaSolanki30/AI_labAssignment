import java.util.*;

public class SudokuSolver {
    static int[][] grid = new int[9][9];

    static boolean isSafe(int row, int col, int num) {
        // Check row and column
        for (int i = 0; i < 9; i++) {
            if (grid[row][i] == num ||
                grid[i][col] == num) {
                return false;
            }
        }

        // Check 3x3 subgrid
        int startRow = (row / 3) * 3;
        int startCol = (col / 3) * 3;

        for (int i = startRow; i < startRow + 3; i++) {
            for (int j = startCol; j < startCol + 3; j++) {
                if (grid[i][j] == num) {
                    return false;
                }
            }
        }

        return true;
    }

    static boolean solve() {
        for (int row = 0; row < 9; row++) {
            for (int col = 0; col < 9; col++) {

                if (grid[row][col] == 0) {
                    for (int num = 1; num <= 9; num++) {

                        if (isSafe(row, col, num)) {
                            grid[row][col] = num;

                            if (solve())
                                return true;

                            grid[row][col] = 0;
                        }
                    }

                    return false;
                }
            }
        }

        return true;
    }

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        System.out.println(
            "Enter the Sudoku grid (use 0 for empty cells):");

        for (int i = 0; i < 9; i++) {
            for (int j = 0; j < 9; j++) {
                grid[i][j] = sc.nextInt();

                if (grid[i][j] < 0 || grid[i][j] > 9) {
                    System.out.println("Invalid digit.");
                    sc.close();
                    return;
                }
            }
        }

        if (solve()) {
            System.out.println("Solved Sudoku:");
            for (int i = 0; i < 9; i++) {
                for (int j = 0; j < 9; j++) {
                    System.out.print(grid[i][j] + " ");
                }
                System.out.println();
            }
        } else {
            System.out.println("No solution exists.");
        }

        sc.close();
    }
}
