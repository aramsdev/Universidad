    package Botones;
import java.awt.BorderLayout;
import java.awt.Color;
import java.awt.Container;
import java.awt.FlowLayout;
import javax.swing.JButton;
import javax.swing.JFrame;

public class CincoBotones1 extends JFrame {
    // se declara una instancia de la clase JButton
    
    private final JButton botonNorte;
    private final JButton botonSur;
    private final JButton botonCentro;
    private final JButton botonOeste;
    private final JButton botonEste;
    
    public CincoBotones1(String titulo){
        super(titulo);
        setSize(600,300);
        this.getContentPane().setBackground(Color.CYAN);
        // se crean objetos de tipo JButton
        botonNorte = new JButton("Soy Boton Norte");
        botonSur = new JButton("Soy Boton Sur");
        botonCentro = new JButton("Soy Boton Centro");
        botonOeste = new JButton("Soy Boton Oeste");
        botonEste = new JButton("Soy Boton Este");
        colocarComponentes();
        // se llama al metodo add que recibe como parámetro una componente
        setVisible(true);
        setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
    }
    
    public void colocarComponentes(){
        setLayout(new FlowLayout());
        add(botonNorte);
        add(botonSur);
        // add(botonCentro);
        add(botonOeste);
        add(botonEste);
    }
    
    public static void main(String[] args) {
        CincoBotones1 ventana = new CincoBotones1("Distribuyendo componentes en JFrame");
    }
    
}
