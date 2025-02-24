/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Classes/Class.java to edit this template
 */
package com.mycompany.practica2java;

public class Punto {
    private float x, y;

    public Punto(float x, float y) {
        this.x = x;
        this.y = y;
    }

    public float getX() { return x; }
    public float getY() { return y; }

    public String coordCartesianas() {
        return "(" + x + ", " + y + ")";
    }

    public String coordPolares() {
        double r = Math.sqrt(x * x + y * y);
        double theta = Math.toDegrees(Math.atan2(y, x));
        return "r: " + r + ", θ: " + theta + "°";
    }

    @Override
    public String toString() {
        return "Punto" + coordCartesianas();
    }
}
