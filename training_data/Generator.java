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
    List<DataSet> data = new ArrayList<DataSet>();
    for (int i = 0; i < ntest; i++) {
      data.add(printVector(nrows, ncols, inf));
    }
    Collections.sort(data);
    for (DataSet record : data) {
      record.print(output);
    }
    output.close();
  }

  private DataSet printVector(int nrows, int ncols, int inf) {
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
    
    DataSet record = new DataSet();
    record.row = row;
    record.col = col; // position
    record.currentDirection = currentDirection; // current direction
    record.enemyUp = enemyUp;
    record.enemyDown = enemyDown;
    record.enemyLeft = enemyLeft;
    record.enemyRight = enemyRight; // enemy position
    record.bulletUp = bulletUp;
    record.bulletDown = bulletDown;
    record.bulletLeft = bulletLeft;
    record.bulletRight = bulletRight; // bullet position
    for (int i = 0; i < directions.length; i++) { // movement direction
      record.directions[i] = directions[i];
    }
    for (int i = 0; i < bases.length; i++) {
      record.bases[i] = bases[i];
    }
    return record;
  }

  private class DataSet implements Comparable<DataSet> {
    private int row;
    private int col;
    private int currentDirection;
    private int enemyUp;
    private int enemyDown;
    private int enemyLeft;
    private int enemyRight;
    private int bulletUp;
    private int bulletDown;
    private int bulletLeft;
    private int bulletRight;
    private int[] directions;
    private int[] bases;

    private DataSet() {
      directions = new int[4];
      bases = new int[3];
    }

    @Override public int compareTo(DataSet other) { // checking value by value
      if (row != other.row) {
        return row - other.row;
      }
      if (col != other.col) {
        return col - other.col;
      }
      if (currentDirection != other.currentDirection) {
        return currentDirection - other.currentDirection;
      }
      if (enemyUp != other.enemyUp) {
        return enemyUp - other.enemyUp;
      }
      if (enemyDown != other.enemyDown) {
        return enemyDown - other.enemyDown;
      }
      if (enemyLeft != other.enemyLeft) {
        return enemyLeft - other.enemyLeft;
      }
      if (enemyRight != other.enemyRight) {
        return enemyRight - other.enemyRight;
      }
      if (bulletUp != other.bulletUp) {
        return bulletUp - other.bulletUp;
      }
      if (bulletDown != other.bulletDown) {
        return bulletDown - other.bulletDown;
      }
      if (bulletLeft != other.bulletLeft) {
        return bulletLeft - other.bulletLeft;
      }
      if (bulletRight != other.bulletRight) {
        return bulletRight - other.bulletRight;
      }
      for (int i = 0; i < 4; i++) {
        if (directions[i] != other.directions[i]) {
          return directions[i] - other.directions[i];
        }
      }
      for (int i = 0; i < bases.length; i++) {
        if (bases[i] != other.bases[i]) {
          return bases[i] - other.bases[i];
        }
      }
      return 0; // otherwise 2 record are the same
    }

    private void print(PrintWriter out) {
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
}
