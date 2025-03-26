/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Classes/Class.java to edit this template
 */
package com.mycompany.practica5java;


public class EcuacionCuadratica {
    private double a;
    private double b;
    private double c;

    // Constructor
    public EcuacionCuadratica(double a, double b, double c) {
        this.a = a;
        this.b = b;
        this.c = c;
    }

    
    public double getDiscriminante() {
        return b * b - 4 * a * c;
    }

    
    public double getRaiz1() {
        double discriminante = getDiscriminante();
        return (-b + Math.sqrt(discriminante)) / (2 * a);
    }

    
    public double getRaiz2() {
        double discriminante = getDiscriminante();
        return (-b - Math.sqrt(discriminante)) / (2 * a);
    }
}