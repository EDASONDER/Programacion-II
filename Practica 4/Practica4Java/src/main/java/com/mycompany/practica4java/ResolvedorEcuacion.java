/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Classes/Class.java to edit this template
 */
package com.mycompany.practica4java;

/**
 *
 * @author Usuario
 */
public class ResolvedorEcuacion {
    private EcuacionCuadratica ecuacion;

    
    public ResolvedorEcuacion(EcuacionCuadratica ecuacion) {
        this.ecuacion = ecuacion;
    }

    
    public void resolver() {
        double discriminante = ecuacion.getDiscriminante();

        if (discriminante > 0) {
            double r1 = ecuacion.getRaiz1();
            double r2 = ecuacion.getRaiz2();
            System.out.printf("La ecuación tiene dos raices: %.5f y %.5f%n", r1, r2);
        } else if (discriminante == 0) {
            double r1 = ecuacion.getRaiz1();
            System.out.printf("La ecuación tiene una raiz: %.5f%n", r1);
        } else {
            System.out.println("La ecuación no tiene raices reales");
        }
    }
}