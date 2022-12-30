public class ej11 {
    public static void main(String[] args) {
        String parragraph = "La programación es el proceso de escribir y diseñar código informático para decirle a una"
        + "computadora qué debe hacer. Los programadores utilizan lenguajes de programación para escribir código, "
        + "que es un conjunto de instrucciones que le dicen a la computadora qué hacer. El código puede ser utilizado" 
        + "para crear programas informáticos, juegos, aplicaciones móviles, sitios web y mucho más.";
        String word = "código";
        String new_word = "-[CENSURADO]-";

        String censored = parragraph.replace(word, new_word);

        System.out.println(censored);
    }
}