import java.io.*;
import java.util.*;

public class Translator {
  public static void main(String[] args) {
    Translator translator = new Translator();
    translator.process();

  }

  private Scanner fileIn;
  private List<String> lines;
  private int lineIndex;

  private void process() {
    if (init()) {
      return;
    }
    Scanner prompt = new Scanner(System.in);
    for (int idx = lineIndex; idx < lines.size(); idx++) {
      System.out.println("Data at line " + (idx + 1) + ":");
      printData(lines.get(idx));
      System.out.print("Continue ... (Y/N): ");
      char command = prompt.next().charAt(0);
      if (command == 'N' || command == 'n') // stop printing 
        return;
    }
  }

  private boolean init() {
    Scanner sysIn = new Scanner(System.in);
    System.out.print("Data filename: ");
    String filename = sysIn.next();

    // open file 
    fileIn = null;
    try {
      fileIn = new Scanner(new FileReader(filename));
    } catch (IOException e) {
      System.err.println("Data file not found!");
      return true;
    }
    
    // reading file
    lines = new ArrayList<String>();
    while (fileIn.hasNext()) {
      lines.add(fileIn.nextLine());
    }

    // read current index
    System.out.print("Translate from line (based-1): ");
    lineIndex = sysIn.nextInt() - 1;
    return false;
  }

  private void printData(String data) {
    StringTokenizer st = new StringTokenizer(data);
    // agent's position
    int row = Integer.parseInt(st.nextToken());
    int col = Integer.parseInt(st.nextToken());
    System.out.printf("- Agent position is at (%d, %d)\n", row, col);

    // agent's current moving direction
    int currentDir = Integer.parseInt(st.nextToken());
    String direction = "$";
    switch (currentDir) {
      case 0:
        direction = "upward";
        break;
      case 1:
        direction = "downward";
        break;
      case 2:
        direction = "left";
        break;
      default:
        direction = "right";
    }
    System.out.printf("- Current moving direction: %s\n\n", direction);

    // enemy distance
    int enemyAbove = Integer.parseInt(st.nextToken());
    int enemyBelow = Integer.parseInt(st.nextToken());
    int enemyLeft = Integer.parseInt(st.nextToken());
    int enemyRight = Integer.parseInt(st.nextToken());
    System.out.println("- Enemy info:");
    System.out.printf("   Distance above: %d\n", enemyAbove);
    System.out.printf("   Distance below: %d\n", enemyBelow);
    System.out.printf("   Distance left: %d\n", enemyLeft);
    System.out.printf("   Distance right: %d\n\n", enemyRight);

    // bullet distance
    int bulletAbove = Integer.parseInt(st.nextToken());
    int bulletBelow = Integer.parseInt(st.nextToken());
    int bulletLeft = Integer.parseInt(st.nextToken());
    int bulletRight = Integer.parseInt(st.nextToken());
    System.out.println("- Bullet info:");
    System.out.printf("   Distance above: %d\n", bulletAbove);
    System.out.printf("   Distance below: %d\n", bulletBelow);
    System.out.printf("   Distance left: %d\n", bulletLeft);
    System.out.printf("   Distance right: %d\n\n", bulletRight);

    // available movement
    int canMoveUp = Integer.parseInt(st.nextToken());
    int canMoveDown = Integer.parseInt(st.nextToken());
    int canMoveLeft = Integer.parseInt(st.nextToken());
    int canMoveRight = Integer.parseInt(st.nextToken());
    if (canMoveUp == 0 && canMoveRight == 0 && canMoveLeft == 0 
          && canMoveRight == 0) {
      System.out.println("Cannot move! Bad data :(");
    }
    System.out.println("Can move: ");
    if (canMoveUp == 1) {
      System.out.println("  up");
    }
    if (canMoveDown == 1) {
      System.out.println("  down");
    }
    if (canMoveLeft == 1) {
      System.out.println("  left");
    }
    if (canMoveRight == 1) {
      System.out.println("  right");
    }
    System.out.println("\n");

    // base information
    System.out.println("Base info:");
    int baseLeft = Integer.parseInt(st.nextToken());
    int baseAbove = Integer.parseInt(st.nextToken());
    int baseRight = Integer.parseInt(st.nextToken());
    if (baseLeft == 0 && baseRight == 0 && baseAbove == 0) {
      System.out.println("Base is safe");
    }
    if (baseLeft == 1) System.out.println("Base left is broken");
    if (baseAbove == 1) System.out.println("Base above is broken");
    if (baseRight == 1) System.out.println("Base right is broken");
    System.out.println("\n\n");
  }
}
