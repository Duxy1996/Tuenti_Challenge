import java.util.*;
import java.io.*;
public class Clener
{
    public static void main (String [] args)throws Exception{
        muestraContenido("testInput.txt");        
    }
    public static void muestraContenido(String archivo) throws Exception {
      String cadena;
      FileReader f = new FileReader(archivo);
      BufferedReader b = new BufferedReader(f);
      while((cadena = b.readLine())!=null) {
          System.out.println(cadena);
      }
      b.close();
    }
}
