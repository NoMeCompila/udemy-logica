public class ej4 {
    public static void main(String[] args) {
        String word = "Fernando";
        char[] chars = word.toCharArray();
        String reverse = "";

        for(int i = chars.length -1; i >= 0; i--){
            reverse += chars[i];
        }
            
        System.out.println(reverse);
    }
}
