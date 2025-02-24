package com.mycompany.practica1java;

public class Practica1Java {
    public static void main(String[] args) {
        Punto p = new Punto(3, 4);
        System.out.println(p);
        float[] cartesianas = p.coord_cartesianas();
        System.out.println("Coordenadas Cartesianas: (" + cartesianas[0] + ", " + cartesianas[1] + ")");
        float[] polares = p.coord_polares();
        System.out.println("Coordenadas Polares: (r: " + polares[0] + ", theta: " + polares[1] + ")");
    }
}

