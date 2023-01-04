import java.util.ArrayList;

public class ej24 {
    public static void main(String[] args) {
        ArrayList<Integer> l1 = new ArrayList<>();
        ArrayList<Integer> l2 = new ArrayList<>();

        l1.add(1);
        l1.add(2);
        l1.add(3);
        l1.add(4);
        l1.add(5);

        l2.add(1);
        l2.add(2);
        l2.add(3);
        l2.add(5);

        int n = 5;

        System.out.println(isPermutation(l1, n));
        System.out.println(isPermutation(l2, n));
    }

    public static boolean isPermutation(ArrayList<Integer> lista, int num){

        ArrayList<Integer> l3 = new ArrayList<>();
        //boolean isPErmu = true;

        for (int i = 0; i <= num; i++) {
            l3.add(i);
        }

        if(lista.size() != l3.size()){
            return  false;
        }

        for (int i = 0; i <= num; i++) {
            if(lista.get(i) != l3.get(i)){
                return  false;
            }
        }

        return true;
    }
}
