public class Pelicula {
    private String titulo;
    private boolean visto;

    public Pelicula(String titulo, boolean visto) {
        this.titulo = titulo;
        this.visto = visto;
    }

    public void setVisto(boolean p_visto) {
        this.visto = p_visto;
    }

    public void setTitulo(String p_titulo){
        this.titulo = p_titulo;
    }

    public String getTittulo(){
        return this.titulo;
    }

    public boolean getVisto(){
        return this.visto;
    }

    public void wasViwed(){
        if(this.getVisto()){
            System.out.println("Usted ya vió " + this.getTittulo());
        }else{
            System.out.println("Usted no vió " + this.getTittulo());
        }
    }
}
