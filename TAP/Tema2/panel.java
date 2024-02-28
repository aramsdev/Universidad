package Botones;
import java.awt.BorderLayout;
import java.awt.Color;
import javax.swing.JButton;
import javax.swing.JFrame;
import javax.swing.JPanel;

public class panel extends JFrame {
   
    private final JButton botonNorte = new JButton("Soy Boton Norte");
    private final JButton botonSur = new JButton("Soy Boton Sur");
    private final JButton botonCentro = new JButton("Soy Boton Centro");
    private final JButton botonOeste = new JButton("Soy Boton Oeste");
    private final JButton botonEste = new JButton("Soy Boton Este");
    
    public panel(String titulo){
        super(titulo);
        setSize(600,400);
        this.getContentPane().setBackground(Color.CYAN);
        setVisible(true);
        setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
    }
    
    public void colocarComponentes(){      
        JPanel p = new JPanel();
        p.setBackground(Color.ORANGE);
        add(p);
        p.add(botonNorte);
        p.add(botonSur);
        p.add(botonCentro);
        p.add(botonOeste);
        p.add(botonEste);
    }
    
    public static void init(){
        panel ventana = new panel("Mi Ventana");
        ventana.colocarComponentes();
    }
    
    public static void main(String[] args) {
        init();
    }
    
}
