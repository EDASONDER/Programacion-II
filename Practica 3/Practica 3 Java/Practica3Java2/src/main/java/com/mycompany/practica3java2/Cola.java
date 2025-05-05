/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Classes/Class.java to edit this template
 */
package com.mycompany.practica3java2;

/**
 *
 * @author Usuario
 */
public class Cola {
    private long[] arreglo;
    private int inicio;
    private int fin;
    private int n;
    private int contador;  // Para rastrear elementos

    public Cola(int n) {
        this.n = n;
        this.arreglo = new long[n];
        this.inicio = 0;
        this.fin = -1;  // Inicialmente vacía
        this.contador = 0;
    }

    public void insert(long e) {
        if (!isFull()) {
            fin = (fin + 1) % n;  // Avance circular
            arreglo[fin] = e;
            contador++;
        } else {
            System.out.println("Error: Cola llena (Overflow)");
        }
    }

    public long remove() {
        if (!isEmpty()) {
            long elemento = arreglo[inicio];
            inicio = (inicio + 1) % n;  // Avance circular
            contador--;
            return elemento;
        } else {
            System.out.println("Error: Cola vacía (Underflow)");
            return -1;
        }
    }

    public long peek() {
        if (!isEmpty()) {
            return arreglo[inicio];
        } else {
            System.out.println("Error: Cola vacía");
            return -1;
        }
    }

    public boolean isEmpty() {
        return contador == 0;
    }

    public boolean isFull() {
        return contador == n;
    }

    public int size() {
        return contador;
    }
}