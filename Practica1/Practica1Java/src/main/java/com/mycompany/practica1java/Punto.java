package com.mycompany.practica1java;

public class Punto {
    private float x;
    private float y;

    public Punto(float x, float y) {
        this.x = x;
        this.y = y;
    }

    public float[] coord_cartesianas() {
        return new float[]{x, y};
    }

    public float[] coord_polares() {
        float r = (float) Math.sqrt(x * x + y * y);
        float theta = (float) Math.atan2(y, x);
        return new float[]{r, theta};
    }

    @Override
    public String toString() {
        return "Punto(" + x + ", " + y + ")";
    }
}
