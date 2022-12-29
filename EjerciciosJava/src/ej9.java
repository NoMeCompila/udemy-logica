import java.util.ArrayList;
public class ej9 {
    public static void main(String[] args) {
        Integer[] l1 = {1, 2, 3, 4};
        Integer[] l2 = {3, 4, 5, 6};
        ArrayList<Integer> l3 = new ArrayList<>();
        for (Integer i : l1) {
            for (Integer j : l2) {
                if(i == j){
                    l3.add(i);
                }
            }
        }
        System.out.println(l3);
    }
}