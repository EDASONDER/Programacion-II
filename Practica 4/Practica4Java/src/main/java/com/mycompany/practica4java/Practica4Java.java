

package com.mycompany.practica4java;

import java.util.Scanner;
public class Practica4Java {

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        
        System.out.println("Ingrese los valores de a, b y c:");
        double a = scanner.nextDouble();
        double b = scanner.nextDouble();
        double c = scanner.nextDouble();

        
        EcuacionCuadratica ecuacion = new EcuacionCuadratica(a, b, c);

        
        ResolvedorEcuacion resolvedor = new ResolvedorEcuacion(ecuacion);
        resolvedor.resolver();
    }
}
