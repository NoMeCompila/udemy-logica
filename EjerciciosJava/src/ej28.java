public class ej28 {
    public static void main(String[] args) {
        int n = 5;
        System.out.println(getFactorial(n));

    }

    public static int getFactorial(int num){
        if(num == 1 || num == 0){
            return 1;
        }else{
            return getFactorial(num-1) * num;
        }
    }
}
