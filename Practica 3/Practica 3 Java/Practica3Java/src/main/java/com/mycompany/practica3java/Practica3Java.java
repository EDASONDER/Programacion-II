/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 */

package com.mycompany.practica3java;

/**
 *
 * @author Usuario
 */
public class Practica3Java {

    public static void main(String[] args) {
        Pila pila = new Pila(3);  
        pila.push(10);
        pila.push(20);
        pila.push(30);
        System.out.println("Tope actual: " + pila.peek());  
        System.out.println("Elemento eliminado: " + pila.pop());  
        System.out.println("Tope después de pop: " + pila.peek());
    }
}
