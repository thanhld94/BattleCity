import java.io.*;
import java.util.*;

public class DataMixer {
  public static void main(String[] args) throws IOException {
    Scanner dataIn = new Scanner(new FileReader(args[0]));
    Scanner dataOut = new Scanner(new FileReader(args[1]));

    // reading in data
    List<String> linesIn = new ArrayList<String>();
    List<String> linesOut = new ArrayList<String>();
    while (dataIn.hasNext()) {
      linesIn.add(dataIn.nextLine());
      linesOut.add(dataOut.nextLine());
    }
    dataIn.close();
    dataOut.close();

    // shuffling
    // initialize deck
    int n = linesIn.size();
    int[] deck = new int[n];
    for (int i = 0; i < n; i++) {
      deck[i] = i;
    }
    int COUNTER = 100000;
    Random rand = new Random();
    for (int i = 0; i < COUNTER; i++) {
      int first = rand.nextInt(n);
      int second = rand.nextInt(n);
      int tmp = deck[first];
      deck[first] = deck[second];
      deck[second] = tmp;
    }

    // printing output
    String inFileName = "shuffled_" + args[0];
    String outFileName = "shuffled_" + args[1];
    PrintWriter outputDataIn = new PrintWriter(new FileWriter(inFileName));
    PrintWriter outputDataOut = new PrintWriter(new FileWriter(outFileName));
    for (int i = 0; i < n; i++) {
      outputDataIn.println(linesIn.get(deck[i]));
      outputDataOut.println(linesOut.get(deck[i]));
    }
    outputDataIn.close();
    outputDataOut.close();
  }
}
