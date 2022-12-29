import java.util.ArrayList;
import java.util.stream.Stream;

public class ej7 {
    public static void main(String[] args) {
        int x = 1;
        int y = 10;
        System.out.println(getOdds(x, y));
    }

    public static ArrayList<Integer> doList(int initial, int end){
        ArrayList<Integer> l = new ArrayList<>();
        for(int i = initial; i <= end; i++){
            l.add(i);
        }
        return l;
    }

    public static int getOdds(int initial, int end){
        Stream<Integer> odds = doList(initial, end).stream().filter(x -> x%2 != 0);
        return odds.toArray().length;
    }
}
