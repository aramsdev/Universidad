package Botones;
import java.awt.Color;
import java.awt.Container;
import javax.swing.JButton;
import javax.swing.JFrame;

public class UnBoton extends JFrame {
    // se declara una instancia de la clase JButton
    
    private final JButton boton;
    private final Container c;
    
    public UnBoton(String titulo){
        super(titulo);
        setSize(600,300);
        c = getContentPane();
        c.setBackground(Color.CYAN);
        // se crea un objeto del tipo JButton
        boton = new JButton("Soy un boton");
        // se llama al metodo add que recibe como parámetro una componente
        c.add(boton);
        setVisible(true);
        setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
    }
    
    public static void main(String[] args) {
        UnBoton ventana = new UnBoton("Distribuyendo componentes en JFrame");
    }
    
}
