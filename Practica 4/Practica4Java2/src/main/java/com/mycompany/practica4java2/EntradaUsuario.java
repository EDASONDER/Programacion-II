/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Classes/Class.java to edit this template
 */
package com.mycompany.practica4java2;

import java.util.Scanner;

public class EntradaUsuario {
    private static final int CANTIDAD_NUMEROS = 10;

    
    public double[] obtenerNumeros() {
        Scanner scanner = new Scanner(System.in);
        double[] numeros = new double[CANTIDAD_NUMEROS];

        System.out.println("Ingrese " + CANTIDAD_NUMEROS + " números:");
        for (int i = 0; i < CANTIDAD_NUMEROS; i++) {
            while (true) {
                System.out.print("Número " + (i + 1) + ": ");
                if (scanner.hasNextDouble()) {
                    numeros[i] = scanner.nextDouble();
                    break; 
                } else {
                    System.out.println("Error: Ingrese un número válido.");
                    scanner.next();
                }
            }
        }

        return numeros;
    }
}