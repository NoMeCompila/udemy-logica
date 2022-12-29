import java.util.Scanner;

import javafx.scene.input.InputEvent;;

public class ej2 {


    public static String reverseString(String str) {
        StringBuilder sb = new StringBuilder();
    
        for (int i = str.length() - 1; i >= 0; i--) {
          sb.append(str.charAt(i));
        }
    
        return sb.toString();
      }

    public static void main(String[] args) {
        Scanner inpuScanner =  new Scanner(System.in);

        System.out.println("Ingrese una palabra: ");
        String word =  inpuScanner.nextLine();
        //System.out.println(word);

        

        if(reverseString(word).equals(word)){
            System.out.println("Es un palíndromo");
        }else{
            System.out.println("No es palíndromo");
        }
    }
}
