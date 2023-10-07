import java.io.File;
import java.util.ArrayList;
import java.util.Scanner;
import java.util.TreeSet;
import java.util.HashMap;
import java.io.FileNotFoundException;

public class App {
    public static void main(String[] args){

        takeInputFromTerminal();

        // takeInputFromFile(new File("../test/16x16/1.txt"));

    }

    public static void takeInputFromTerminal(){
        System.out.println("Input:");
        run(new Scanner(System.in));
    }

    public static void takeInputFromFile(File f){
        try {
            run(new Scanner(f));
        } catch(FileNotFoundException e ){e.printStackTrace();}

    }

    public static void run(Scanner in){
        int numTerms = in.nextInt();
        ArrayList<Integer> terms = new ArrayList<Integer>();

        for(int i=0; i<numTerms; i++)
            terms.add(in.nextInt());
        
        System.out.println(hhMax(terms));

    }

    public static AdjMatrix hhMax(ArrayList<Integer> terms){
        AdjMatrix result = new AdjMatrix(terms.size());
        
        ArrayList<TreeSet<Integer>> bins = new ArrayList<TreeSet<Integer>>();
        
        int k, curDeg, startNode, endNode;
        HashMap<Integer, Integer> movedNodes;

        for(int i=0; i<terms.size(); i++){
            bins.add(new TreeSet<Integer>());
        }
        for(int i=0; i<terms.size(); i++){
            bins.get(terms.get(i)).add(i);
        }

        System.out.println(bins);

        int rounds = 0;

        while(bins.get(0).size() != terms.size()){

            System.out.println("Round " + ++rounds);

            movedNodes = new HashMap<Integer, Integer>();
            
            k = bins.size()-1;
            while(bins.get(k).isEmpty())
                k--;

            startNode = bins.get(k).pollFirst();
            bins.get(0).add(startNode);
            curDeg = k;

            System.out.println("Pivot node: " + startNode);
            System.out.println(bins);

            // endNode = 0;

            for(int i=0; i<k; i++){
                // while(bins.get(0).contains(endNode))
                //     endNode++;
                while((bins.get(curDeg).isEmpty() || (movedNodes.keySet().contains(bins.get(curDeg).first()) && bins.get(curDeg).size() == 1)) && curDeg > 0){
                    curDeg--;
                }
                if(curDeg == 0)
                    return null;
                else {
                    endNode = bins.get(curDeg).pollFirst();
                    movedNodes.put(endNode, curDeg-1);
                    // bins.get(curDeg-1).add(endNode);
                    result.addEdge(startNode, endNode);
                    result.addEdge(endNode, startNode);
                    System.out.println("Added edge: (" + startNode + ", " + endNode + ")");
                    System.out.println(bins);
                }
            }

            for(int node : movedNodes.keySet())
                bins.get(movedNodes.get(node)).add(node);
            System.out.println("Moved nodes");
            System.out.println(bins);

        }
        return result;
    }

}