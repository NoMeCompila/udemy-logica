public class ej27 {
    public static void main(String[] args) {
        int n = 920;
        getDates(n);
    }

    public static void getDates(int d){
        int años = Math.floorDiv(d, 365);
        //System.out.println(años);
        int dias_restantes = d % 365;
        int meses = Math.floorDiv(dias_restantes, 30);
        int dias = dias_restantes % 30;
        System.out.println("años: " +años+ " meses: " +meses+ " días: " +dias);
    } 

}
