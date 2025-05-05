/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Classes/Class.java to edit this template
 */
package com.mycompany.practica3java;

/**
 *
 * @author Usuario
 */
public class Pila {
    private long[] arreglo;
    private int top;
    private int n;

    public Pila(int n) {
        this.n = n;
        this.arreglo = new long[n];
        this.top = -1;  
    }

    public void push(long e) {
        if (!isFull()) {
            top++;
            arreglo[top] = e;
        } else {
            System.out.println("Error: Pila llena (Overflow)");
        }
    }

    public long pop() {
        if (!isEmpty()) {
            long elemento = arreglo[top];
            top--;
            return elemento;
        } else {
            System.out.println("Error: Pila vacía (Underflow)");
            return -1;  
        }
    }

    public long peek() {
        if (!isEmpty()) {
            return arreglo[top];
        } else {
            System.out.println("Error: Pila vacía");
            return -1;  
        }
    }

    public boolean isEmpty() {
        return top == -1;
    }

    public boolean isFull() {
        return top == n - 1;
    }
}