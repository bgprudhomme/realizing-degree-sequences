import java.io.File;
import java.util.ArrayList;
import java.util.Scanner;
import java.util.HashSet;
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

    // HH algorithm with pivot = node with max degree
    public static AdjMatrix hhMax(ArrayList<Integer> terms){
        AdjMatrix result = new AdjMatrix(terms.size());
        ArrayList<ArrayList<Integer>> bins = new ArrayList<ArrayList<Integer>>();
        int k, curDeg, startNode, endNode;
        HashSet<Integer> thisRound;

        while(bins.get(0).size() != terms.size()){

            thisRound = new HashSet<Integer>();
            
            k = bins.size()-1;
            while(bins.get(k).isEmpty())
                k--;

            startNode = bins.get(k).remove(0);
            bins.get(0).add(startNode);
            curDeg = k;

            for(int i=0; i<k; i++){
                // 
                while((bins.get(curDeg).isEmpty() || (thisRound.contains(bins.get(curDeg).get(0)) && bins.get(curDeg).size() == 1)) && curDeg > 0){
                    curDeg--;
                }
                // Non-graphic sequence: return null
                if(curDeg == 0)
                    return null;
                else {
                    // Don't repeat edges
                    int index = 0;
                    while(thisRound.contains(bins.get(curDeg).get(index)))
                        index++;
                    // Select end node, move it to next-lower bin
                    endNode = bins.get(curDeg).remove(index);
                    bins.get(curDeg-1).add(endNode);
                    // Ensure we don't repeat this edge
                    thisRound.add(endNode);
                    // Add edges to adjacency matrix
                    result.addEdge(startNode, endNode);
                    result.addEdge(endNode, startNode);
                    
                }
            }
        }
        return result;
    }

}