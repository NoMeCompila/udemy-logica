public class ej8{
    public static void main(String[] args) {
        int num = 12345;
        int reversedNum = 0;
        while (num > 0) {
            int digit = num % 10;
            reversedNum = reversedNum * 10 + digit;
            num /= 10;
        }
        System.out.println(reversedNum);
    }
}