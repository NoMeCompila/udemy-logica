public class ej12 {
    public static void main(String[] args) {
        int initial = 100;

        System.out.println("Desde el " + initial + " hasta el 0");
        for(int i = initial; i >= 0; i-=8){
            System.out.println("-n° " + i);
        }
    }
}
