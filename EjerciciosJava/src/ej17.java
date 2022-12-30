public class ej17 {
    public static void main(String[] args) {
        int num = 20;
        String f = "Fizz";
        String b = "Buzz";

        for (int i = 0; i <= num; i++) {
            if(i%3 == 0 && i%5 == 0){
                System.out.println(f+b);
            }else if(i%3 == 0){
                System.out.println(f);
            }else if(i%5 == 0){
                System.out.println(f);
            }else{
                System.out.println(i);
            }
        }
    }
}
