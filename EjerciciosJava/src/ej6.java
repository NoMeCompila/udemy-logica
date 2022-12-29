public class ej6 {
    public static void main(String[] args) {
        square(4);
    }

    public static String horizon(int n){
        String stars = "";
        for(int i = 0; i < n; i++){
            stars+="*";
        }
        return stars;
    }

    public static String vert(int n){
        String stars = "";
        //int count = -1;
        for(int i = 0; i <= n-2; i++){
            //count++;
            if(i == 0){
                stars+="*";
            }
            if(i == n-2){
                stars+="*";
            }
            stars+=" ";
        }
        return stars;
    }

    public static void square(int n){
        System.out.println(horizon(n));
        for(int i = 0; i < n-2; i++){
            System.out.println(vert(n));
        }
        System.out.println(horizon(n));
    }
}
