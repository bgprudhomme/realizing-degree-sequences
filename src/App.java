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
        
        // System.out.println(maxHH(terms));
        // System.out.println(minHH(terms));
    }

    public static AdjMatrix maxHH(ArrayList<Integer> terms){
        AdjMatrix result = new AdjMatrix(terms.size());
        
        ArrayList<TreeSet<Integer>> bins = new ArrayList<TreeSet<Integer>>();
        
        int k, curDeg, pivotNode, neighborNode;
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

            pivotNode = bins.get(k).pollFirst();
            bins.get(0).add(pivotNode);
            curDeg = k;

            System.out.println("Pivot node: " + pivotNode);
            System.out.println(bins);

            // neighborNode = 0;

            for(int i=0; i<k; i++){
                // while(bins.get(0).contains(neighborNode))
                //     neighborNode++;
                while((bins.get(curDeg).isEmpty() || (movedNodes.keySet().contains(bins.get(curDeg).first()) && bins.get(curDeg).size() == 1)) && curDeg > 0){
                    curDeg--;
                }
                if(curDeg == 0)
                    return null;
                else {
                    neighborNode = bins.get(curDeg).pollFirst();
                    movedNodes.put(neighborNode, curDeg-1);
                    // bins.get(curDeg-1).add(neighborNode);
                    result.addEdge(pivotNode, neighborNode);
                    result.addEdge(neighborNode, pivotNode);
                    System.out.println("Added edge: (" + pivotNode + ", " + neighborNode + ")");
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

    public static AdjMatrix minHH(ArrayList<Integer> terms){
        AdjMatrix result = new AdjMatrix(terms.size());
        
        ArrayList<TreeSet<Integer>> bins = new ArrayList<TreeSet<Integer>>();
        
        int k, curDeg, pivotNode, neighborNode;
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
            
            k = 1;
            while(bins.get(k).isEmpty())
                k++;

            pivotNode = bins.get(k).pollFirst();
            bins.get(0).add(pivotNode);
            curDeg = terms.size()-1;

            System.out.println("Pivot node: " + pivotNode);
            System.out.println(bins);

            // neighborNode = 0;

            for(int i=0; i<k; i++){
                // while(bins.get(0).contains(neighborNode))
                //     neighborNode++;
                while((bins.get(curDeg).isEmpty() || (movedNodes.keySet().contains(bins.get(curDeg).first()) && bins.get(curDeg).size() == 1)) && curDeg > 0){
                    curDeg--;
                }
                if(curDeg == 0)
                    return null;
                else {
                    neighborNode = bins.get(curDeg).pollFirst();
                    movedNodes.put(neighborNode, curDeg-1);
                    // bins.get(curDeg-1).add(neighborNode);
                    result.addEdge(pivotNode, neighborNode);
                    result.addEdge(neighborNode, pivotNode);
                    System.out.println("Added edge: (" + pivotNode + ", " + neighborNode + ")");
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