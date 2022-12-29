public class ej10 {
    public static void main(String[] args) {
        String starway = "[-]";
        int num = 4;

        for(int i = 0; i < num; i++){
            for(int j = 0; j <= i; j++){
                System.out.print(starway);
            }
            System.out.println();
        }
    }
}
