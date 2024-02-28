package Botones;

import java.awt.Color;
import java.awt.Container;
import java.awt.Font;
import static java.awt.PageAttributes.ColorType.COLOR;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;
import javax.swing.JButton;
import javax.swing.JFrame;
import javax.swing.JLabel;
import javax.swing.JTextField;

public class BotonEtiquetaCajaTexto extends JFrame{
    JButton boton;
    JLabel eti,falsa,responde;
    JTextField campo;
    Container c;
    
    public BotonEtiquetaCajaTexto(){
        super("Ejemplo de componentes basicos y eventos");
        c = getContentPane();
        eti = new JLabel("Escribe tu nombre");
        campo = new JTextField(30);
        boton = new JButton("Verifica");
        responde = new JLabel();
        falsa = new JLabel();
        
        colocaComponentes();
        setSize(700,250);
        setLocationRelativeTo(null);
        setVisible(true);
        setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        
    }

    private void colocaComponentes() {
        eti.setBounds(20,20,200,20);
        c.add(eti);
        campo.setBounds(220,20,200,20);
        campo.setForeground(Color.BLUE);
        campo.setBackground(Color.YELLOW);
        c.add(campo);
        responde.setBounds(220,50,200,20);
        Font f = new Font("Comic", Font.BOLD,20);
        responde.setForeground(Color.red);
        responde.setFont(f);
        c.add(responde);
        boton.setBounds(300,120,80,30);
        c.add(boton);
        c.add(falsa);
        implementaActionListener escuchador = new implementaActionListener(campo,falsa);
        boton.addActionListener(escuchador);
    }
    
    public static void main(String[] args) {
        new BotonEtiquetaCajaTexto();
    }

    /* private class implementaActionListener implements ActionListener{
        @Override
        public void actionPerformed(ActionEvent e) {
            StringBuilder builder = new StringBuilder(campo.getText());
            responde.setText(builder.reverse().toString());
            System.out.println(eti.getText());
        }
    } */
}


