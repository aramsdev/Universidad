package Botones;

import java.awt.BorderLayout;
import java.awt.Color;
import java.awt.Container;
import java.awt.FlowLayout;
import java.awt.GridLayout;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;
import javax.swing.*;

public class CalculadoraIMCEnClase extends JFrame{
    JButton calculaIMC;
    JLabel peso, estatura,titulo,imcResultado;
    JTextField pesoField, estaturaField;
  
    public CalculadoraIMCEnClase(String t){
        super(t);
        setLayout(new BorderLayout());
        this.getContentPane();
        setSize(400,200);
        setVisible(true);
        setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
    }
    
    public static void init(){
        CalculadoraIMCEnClase ventana = new CalculadoraIMCEnClase("Calculadora IMC");
        ventana.creaComponentes();
        ventana.establecePosiciones();
        ventana.colocaComponentes();

        // Encontré que estas dos líneas de código hacen que se 'actualice' el diseño
        ventana.revalidate();
        ventana.repaint();
    }
    
    private void creaComponentes(){
        calculaIMC = new JButton("Calcula IMC");
        peso = new JLabel("Peso");
        pesoField = new JTextField(4);
        estatura = new JLabel("Estatura");
        estaturaField = new JTextField(4);
        titulo = new JLabel("Introduce los datos solicitados");
        imcResultado = new JLabel("");
    }
    
    private void establecePosiciones(){
        titulo.setBounds(100,15,200,10);
        peso.setBounds(100,45,100,10);
        pesoField.setBounds(160,45,120,20);
        estatura.setBounds(100,70,100,10);
        estaturaField.setBounds(160,65,120,20);
        calculaIMC.setBounds(130, 100, 120, 25);
        imcResultado.setBounds(100,125,200,10);
    }
    
    private void colocaComponentes(){
        setLayout(null);
        Container c = getContentPane();
        c.add(titulo);
        c.add(peso);
        c.add(pesoField);
        c.add(estatura);
        c.add(estaturaField);
        c.add(calculaIMC);
        c.add(imcResultado);
    }

    public static void main(String[] args) {
        init();
            
    }
}
