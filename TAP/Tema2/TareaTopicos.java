package Botones;

import java.awt.Color;
import java.awt.Container;
import java.awt.Font;
import javax.swing.JButton;
import javax.swing.JFrame;
import javax.swing.JTextField;

public class TareaTopicos extends JFrame{
    
    JButton boton = new JButton("Dar clic");;
    JTextField bienvenida = new JTextField(30);;
    Container c;
    
    
    public TareaTopicos(){
        super("Tarea Topicos");
        c = getContentPane();
        setLayout(null);
        
        colocaComponentes();
        setSize(700,250);
        setLocationRelativeTo(null);
        setVisible(true);
        setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
    }

    private void colocaComponentes() {
        bienvenida.setBounds(220, 100, 250, 20);
        bienvenida.setForeground(Color.BLUE);
        bienvenida.setBackground(Color.YELLOW);
        c.add(bienvenida);
        boton.setBounds(280, 50, 150, 40);
        c.add(boton);
        BotonAccion escuchador = new BotonAccion(bienvenida);
        boton.addActionListener(escuchador);
    }
    
    public static void main(String[] args) {
        TareaTopicos ventana = new TareaTopicos();
    }

    
}
