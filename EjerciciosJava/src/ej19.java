import java.util.ArrayList;

import org.jcp.xml.dsig.internal.MacOutputStream;
public class ej19 {
    public static void main(String[] args) {
        Pelicula p1 = new Pelicula("Venom", true);
        Pelicula p2 = new Pelicula("Merlina", false);
        Pelicula p3 = new Pelicula("Top Gun", true);
        //Pelicula p4 = new Pelicula("Venom", true);
        
        ArrayList<Pelicula> pelis = new ArrayList<>();
        pelis.add(p1);
        pelis.add(p2);
        pelis.add(p3);

        // for (Pelicula pelicula : pelis) {
        //     System.out.println(pelicula.getTittulo());
        // }

        mostrar(pelis, "Venom");
        mostrar(pelis, "Merlina");
        mostrar(pelis, "asd");
    }

    public static void busqueda(ArrayList<Pelicula> peliculas, String titulo){
        for (Pelicula peli : peliculas) {
            if(peli.getTittulo() == titulo){
                peli.wasViwed();
            }
        }
    }

    public static void mostrar(ArrayList<Pelicula> peliculas, String titulo){
        ArrayList<String> titulos = new ArrayList<>();
        for (Pelicula peli : peliculas) {
            titulos.add(peli.getTittulo());
        }

        if(titulos.contains(titulo)){
            busqueda(peliculas, titulo);
        }else{
            System.out.println("LA pelicula no se encuentra en la lista");
        }
    }
}
