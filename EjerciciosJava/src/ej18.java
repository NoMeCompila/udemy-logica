import java.util.ArrayList;

public class ej18 {
    public static void main(String[] args) {
        int num = 10;
        ArrayList<Integer> divisors =  new ArrayList<>();

        for (int i = 1; i <= num; i++) {
            if(num%i == 0){
                divisors.add(i);
            }
        }
        
        System.out.println(divisors);
    }
}
