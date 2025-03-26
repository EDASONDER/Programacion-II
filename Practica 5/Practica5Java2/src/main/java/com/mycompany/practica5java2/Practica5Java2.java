/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 */

package com.mycompany.practica5java2;

public class Practica5Java2 {

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
