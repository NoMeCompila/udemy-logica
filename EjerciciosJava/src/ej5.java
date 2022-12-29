public class ej5 {
    public static void main(String[] args) {
        int tot = 200;
        int per = 50;

        System.out.println(percent(tot, per));

    }

    public static float percent(float x, float y) {
        return (x * y)/100;
    }
}
