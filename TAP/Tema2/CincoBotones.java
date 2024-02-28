package Botones;
import java.awt.BorderLayout;
import java.awt.Color;
import java.awt.Container;
import javax.swing.JButton;
import javax.swing.JFrame;

public class CincoBotones extends JFrame {
    // se declara una instancia de la clase JButton
    
    private final JButton botonNorte;
    private final JButton botonSur;
    private final JButton botonCentro;
    private final JButton botonOeste;
    private final JButton botonEste;

    private final Container c;
    
    public CincoBotones(String titulo){
        super(titulo);
        setSize(600,300);
        c = getContentPane();
        c.setBackground(Color.CYAN);
        
        // se crean objetos de tipo JButton
        botonNorte = new JButton("Soy Boton Norte");
        botonSur = new JButton("Soy Boton Sur");
        botonCentro = new JButton("Soy Boton Centro");
        botonOeste = new JButton("Soy Boton Oeste");
        botonEste = new JButton("Soy Boton Este");
        
        c.add(botonNorte, BorderLayout.NORTH);
        c.add(botonSur, BorderLayout.SOUTH);
       // c.add(botonCentro, BorderLayout.CENTER);
        c.add(botonOeste, BorderLayout.WEST);
        c.add(botonEste, BorderLayout.EAST);
        
        
        // se llama al metodo add que recibe como parámetro una componente
        setVisible(true);
        setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
    }
    
    public static void main(String[] args) {
        CincoBotones ventana = new CincoBotones("Distribuyendo componentes en JFrame");
    }
    
}
