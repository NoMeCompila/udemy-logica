public class ej26 {
    public static void main(String[] args) {
        int p1 = 0;
        int p2 = 1;
        int n = 10;

        for (int i = 0; i <= n; i++) {
             int aux = p2;
             p2 += p1;
             p1 = aux;
             System.out.println(p2);
        }
    }
}