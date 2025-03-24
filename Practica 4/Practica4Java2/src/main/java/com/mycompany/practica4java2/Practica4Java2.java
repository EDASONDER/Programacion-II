
package com.mycompany.practica4java2;

/**
 *
 * @author Usuario
 */
public class Practica4Java2 {

    public static void main(String[] args) {
        EntradaUsuario entrada = new EntradaUsuario();
        double[] numeros = entrada.obtenerNumeros();

        
        Estadisticas estadisticas = new Estadisticas(numeros);
        double prom = estadisticas.promedio();
        double dev = estadisticas.desviacion();

        
        System.out.printf("El promedio es %.2f%n", prom);
        System.out.printf("La desviacion estandar es %.5f%n", dev);
    }
}
