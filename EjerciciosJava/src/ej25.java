public class ej25 {
    public static void main(String[] args) {
        String phrase1 = "Hola Como estas";
        String phrase2 = "MUCHO MAS CON MAYuscula";
        
        
        System.out.println(isUperOrLower(phrase1));
        System.out.println(isUperOrLower(phrase2));
    }

    public static String isUperOrLower(String str){
        //String[] chars = str.split("");
        int m = 0;
        int M = 0;
        for (int i = 0; i < str.length(); i++) {
            char c = str.charAt(i);
            if (Character.isUpperCase(c)) {
              M++;
            } else if (Character.isLowerCase(c)) {
              m++;
            }
        }
        if(m > M){
            String new_str = str.toLowerCase();
            return new_str;
        }else{
            String new_str = str.toUpperCase();
            return new_str;
        }
    }
}
