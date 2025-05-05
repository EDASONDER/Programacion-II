/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 */

package com.mycompany.practica3java2;

/**
 *
 * @author Usuario
 */
public class Practica3Java2 {

    public static void main(String[] args) {
        Cola cola = new Cola(3);
        cola.insert(10);
        cola.insert(20);
        cola.insert(30);
        System.out.println("Frente actual: " + cola.peek());  
        System.out.println("Elemento removido: " + cola.remove()); 
        System.out.println("Nuevo frente: " + cola.peek());  
        System.out.println("Tamaño actual: " + cola.size());
    }
}
