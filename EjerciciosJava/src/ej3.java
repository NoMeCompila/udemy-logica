public class ej3 {
    public static void main(String[] args) {
        String parragraph = "soy la palabra en una frase llena de PALABRA";
        String word = "palabra";
        int ocurrencias = 0;
        String[] lista = parragraph.split("\\s+");
        
        for (String elem : lista) {
            //System.out.println(elem);
            if(elem.equalsIgnoreCase(word)){
                ocurrencias++;
            }
        }
        
        System.out.println(ocurrencias);
    }
}
