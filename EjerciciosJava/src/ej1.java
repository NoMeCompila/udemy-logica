import java.util.Scanner;

public class ej1{
    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);
        System.out.println("Ingrese un número: ");
        int num = input.nextInt();

        for(int  i = 0; i <= 10; i++){
            System.out.println(num +" * " + i + " = " + num*i );
        }
    }
}