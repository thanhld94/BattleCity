import java.io.*;
import java.util.*;

public class Generator {
  public static void main(String[] args) {
    Generator gen = new Generator();
    gen.generate();
  }

  private static final int[] dx = {-1, 1, 0, 0};
  private static final int[] dy = {0, 0, -1, 1};

  public void generate() {
    Scanner in = new Scanner(System.in);
    System.out.print("Output file name: ");
    String filename = in.next();
    System.out.print("Number of rows: ");
    int nrows = in.nextInt();
    System.out.print("Number of columns: ");
    int ncols = in.nextInt();
    System.out.print("Infinity value: ");
    int inf = in.nextInt();
    System.out.print("Number of tests: ");
    int ntest = in.nextInt();
    //System.out.printf("filename = %s\nNRows = %d\nNCols = %d\n", filename, nrows, ncols);
    generate(filename, nrows, ncols, inf, ntest);
  }

  private void generate(String filename, int nrows, int ncols, int inf, int ntest) {
    PrintWriter output = new PrintWriter(System.out);
    try {
      output = new PrintWriter(new FileWriter(filename));
    } catch (Exception e) {
      System.err.println("Bad input file");
      e.printStackTrace();
    }
    for (int i = 0; i < ntest; i++) {
      printVector(nrows, ncols, inf, output);
    }
    output.close();
  }

  private void printVector(int nrows, int ncols, int inf, PrintWriter out) {
    Random rand = new Random();
    // position
    int row = rand.nextInt(nrows);
    int col = rand.nextInt(ncols);

    // current direction
    int currentDirection = rand.nextInt(4);

    // distance from enemy
    // above
    int enemyUp = rand.nextInt(row + 1);
    if (enemyUp == 0) { // random a zero will means there is no enemy in that direction
      enemyUp = inf;
    }
    // below
    int enemyDown = rand.nextInt(nrows - row);
    if (enemyDown == 0) { // random a zero will means there is no enemy in that direction
      enemyDown = inf;
    }
    // left
    int enemyLeft = rand.nextInt(col + 1);
    if (enemyLeft == 0) { // random a zero will means there is no enemy in that direction
      enemyLeft = inf;
    }
    // right
    int enemyRight = rand.nextInt(ncols - col);
    if (enemyRight == 0) { // random a zero will means there is no enemy in that direction
      enemyRight = inf;
    }

    // distance from bullet
    // above
    int bulletUp = rand.nextInt(row + 1);
    if (bulletUp == 0) { // random a zero will means there is no enemy in that direction
      bulletUp = inf;
    }
    // below
    int bulletDown = rand.nextInt(nrows - row);
    if (bulletDown == 0) { // random a zero will means there is no enemy in that direction
      bulletDown = inf;
    }
    // left
    int bulletLeft = rand.nextInt(col + 1);
    if (bulletLeft == 0) { // random a zero will means there is no enemy in that direction
      bulletLeft = inf;
    }
    // right
    int bulletRight = rand.nextInt(ncols - col);
    if (bulletRight == 0) { // random a zero will means there is no enemy in that direction
      bulletRight = inf;
    }

    // generate available next move
    int[] directions = new int[4];
    for (int dir = 0; dir < dx.length; dir++) {
      int nextRow = row + dx[dir];
      int nextCol = col + dy[dir];
      if (0 <= nextRow && nextRow < nrows && 0 <= nextCol && nextCol < ncols) { // valid next move
        int coin = rand.nextInt(2);
        if (coin == 1) directions[dir] = 1; // flip success
      }
    }

    // generate base's wall details
    int[] bases = new int[3];
    for (int i = 0; i < 3; i++) {
      int coin = rand.nextInt(2);
      if (coin == 1) bases[i] = 1; // flip success;
    }
    
    // print
    out.print(row + " " + col + " "); // position
    out.print(currentDirection + " "); // current direction
    out.print(enemyUp + " " + enemyDown + " " + enemyLeft + " " + enemyRight + " "); // enemy position
    out.print(bulletUp + " " + bulletDown + " " + bulletLeft + " " + bulletRight + " "); // bullet position
    for (int i = 0; i < directions.length; i++) {
      out.print(directions[i] + " ");
    }
    for (int i = 0; i < bases.length; i++) {
      out.print(bases[i] + " ");
    }
    out.println();
  }

}
