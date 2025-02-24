/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Classes/Class.java to edit this template
 */
package com.mycompany.practica2java;

public class Circulo {
    private Punto centro;
    private float radio;

    public Circulo(Punto centro, float radio) {
        this.centro = centro;
        this.radio = radio;
    }

    public Punto getCentro() { return centro; }
    public float getRadio() { return radio; }

    @Override
    public String toString() {
        return "Círculo con centro " + centro + " y radio " + radio;
    }
}
