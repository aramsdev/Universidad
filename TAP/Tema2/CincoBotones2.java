    package Botones;
import java.awt.BorderLayout;
import java.awt.Color;
import java.awt.Container;
import java.awt.GridLayout;
import javax.swing.JButton;
import javax.swing.JFrame;

public class CincoBotones2 extends JFrame {
    // se declara una instancia de la clase JButton
    
    private final JButton botonNorte = new JButton("Soy Boton Norte");
    private final JButton botonSur = new JButton("Soy Boton Sur");
    private final JButton botonCentro = new JButton("Soy Boton Centro");
    private final JButton botonOeste = new JButton("Soy Boton Oeste");
    private final JButton botonEste = new JButton("Soy Boton Este");
    
    public CincoBotones2(String titulo){
        super(titulo);
        setSize(600,300);
        this.getContentPane().setBackground(Color.CYAN);
        setVisible(true);
        setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
    }
    
    public void colocarComponentes(){
        setLayout(new GridLayout(3,3));
        add(botonNorte);
        add(botonSur);
        add(botonCentro);
        add(botonOeste);
        add(botonEste);
    }
    
    public static void init(){
        CincoBotones2 ventana = new CincoBotones2("Mi Ventana");
        ventana.colocarComponentes();
    }
    
    public static void main(String[] args) {
        init();
    }
    
}
