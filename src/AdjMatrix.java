import java.util.ArrayList;

public class AdjMatrix {

    private int size;
    private ArrayList<ArrayList<Boolean>> entries;

    // Constructor for rectangular matrix
    public AdjMatrix(int size){
        this.size = size;
        entries = new ArrayList<ArrayList<Boolean>>();
        for(int i=0; i<this.size; i++){
            entries.add(new ArrayList<Boolean>());
            for(int j=0; j<this.size; j++){
                ((ArrayList<Boolean>) entries.get(i)).add(false);
            }
        }
    }

    public int size(){
        return size;
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
        if((this.size() != other.size()))
            return false;
        for(int i=0; i<this.size(); i++){
            for(int j=0; j<this.size(); j++){
                if(this.get(i, j) != other.get(i, j))
                    return false;
            }
        }
        return true;
    }

    public String toString(){
        String result = "";
        for(int i=0; i<size; i++){
            for(int j=0; j<size; j++){
                if(entries.get(i).get(j))
                    result += "1 ";
                else
                    result += "0 ";
            }
            result += "\n";
        }
        return result;
    }

}