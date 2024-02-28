package GUI;

import java.awt.BorderLayout;
import java.awt.Color;
import java.awt.FlowLayout;
import java.awt.GridLayout;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;
import javax.swing.*;

public class CalculadoraIMC extends JFrame{
    JButton calculaIMC = new JButton("Calcula IMC");
    JLabel peso = new JLabel("Peso");
    JLabel titulo;
    JTextField peso_field = new JTextField(4);
    JLabel estatura = new JLabel("Estatura");
    JTextField estatura_field = new JTextField(4);
    JLabel resultado = new JLabel();
    JPanel PanelTitulo,p2,p3, p4, panelres;
    
    public CalculadoraIMC(String t){
        super(t);
        setLayout(new BorderLayout());
        this.getContentPane();
        setSize(500,300);
        setVisible(true);
        setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        creaComponentes();
        colocar();
    }
    
    private void creaComponentes(){
        PanelTitulo=new JPanel();    //Se crean los paneles
        p2=new JPanel();
        p3=new JPanel();
        p4=new JPanel();
        panelres=new JPanel();
        titulo = new JLabel("Introduce los datos solicitados");
        titulo.setForeground(Color.WHITE);
        PanelTitulo.setBackground(Color.BLUE);   //Se le asignan colores SOLO a los paneles
    }
    
    private void colocar(){        
        setLayout(new GridLayout(5,1));
        PanelTitulo.add(titulo);
        p2.add(peso);
        p2.add(peso_field);
        p3.add(estatura);
        p3.add(estatura_field);
        p4.add(calculaIMC);
        panelres.add(resultado);
        
        add(PanelTitulo);
        add(p2);
        add(p3);
        add(p4);
        add(panelres);
        
        ActionListener escuchador = new calcularIMC(peso_field,estatura_field, resultado);
        calculaIMC.addActionListener(escuchador);
    }
    
    public static void main(String[] args) {
        CalculadoraIMC ventana = new CalculadoraIMC("Calculadora IMC");
    }
}

    
