package src;

import java.io.BufferedWriter;
import java.io.File;
import java.util.ArrayList;
import java.util.Scanner;
import java.io.FileNotFoundException;
import java.io.FileWriter;
import java.io.IOException;
import java.lang.Math;
import java.util.Arrays;
import java.util.Collections;

public class App {
    public static void main(String[] args){

        // takeInputFromTerminal();

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
        


    }

    public static boolean isSeqGraphic(ArrayList<Integer> terms){
        if(terms.get(0) == 0)
            return true;
        else if(terms.get(0) >= terms.size() || terms.get(terms.get(0)+1) == 0)
            return false;
        else
            return isSeqGraphic(hhTransformation(terms));
    }

    public static ArrayList<Integer> hhTransformation(ArrayList<Integer> terms){
        ArrayList<Integer> result = new ArrayList<Integer>();
        int pivotIndex = terms.get(0);
        for(int i=1; i<terms.size(); i++){
            int next = terms.get(i);
            if(i < pivotIndex)
                result.add(next-1);
            else
                result.add(next);
        }

        Collections.sort(hhTransformation(terms), Collections.reverseOrder());

        return result;
    }

}