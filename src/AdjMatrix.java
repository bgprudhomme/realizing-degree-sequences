package src;
import java.util.ArrayList;

public class AdjMatrix {

    private int rows, cols;
    private ArrayList<ArrayList<Boolean>> entries;

    // Constructor for rectangular matrix
    public AdjMatrix(int rows, int cols){
        this.rows = rows;
        this.cols = cols;
        entries = new ArrayList<ArrayList<Boolean>>();
        for(int i=0; i<this.rows; i++){
            entries.add(new ArrayList<Boolean>());
            for(int j=0; j<this.cols; j++){
                ((ArrayList<Boolean>) entries.get(i)).add(false);
            }
        }
    }

    public int rows(){
        return rows;
    }

    public int cols(){
        return cols;
    }

    public boolean get(int row, int col){
        return (Boolean) ((ArrayList<Boolean>) entries.get(row)).get(col);
    }

    public void addEdge(int row, int col){
        ((ArrayList<Boolean>) entries.get(row)).set(col, true);
    }

    public void removeEdge(int row, int col){
        ((ArrayList<Boolean>) entries.get(row)).set(col, false);
    }

    public boolean equals(AdjMatrix other){
        if((this.rows() != other.rows()) || (this.cols() != other.cols()))
            return false;
        for(int i=0; i<this.rows(); i++){
            for(int j=0; j<this.rows(); j++){
                if(this.get(i, j) != other.get(i, j))
                    return false;
            }
        }
        return true;
    }

    public String toString(){
        String result = "";
        for(int i=0; i<rows; i++){
            for(int j=0; j<cols; j++){
                result += ((ArrayList<Boolean>) entries.get(i)).get(j) + "\t";
            }
            result += "\n";
        }
        return result;
    }

}