package GUI;

import Control.CalculaIMC; //Clase que proviene del package control para hacer el cálculo del IMC
import javax.swing.JFrame;
import java.awt.*;
import javax.swing.JButton;
import javax.swing.JLabel;
import javax.swing.JPanel;
import javax.swing.JTextField;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;
import java.text.DecimalFormat;

public class CalculadoraIMCFuncional extends JFrame{

    
    //Declaracion de componentes
    JButton btnCalcular;      
    JLabel lblTit,lblPeso,lblEstat, lblIMCResultado;
    JTextField txtPeso,txtEstatura;
    JPanel n1,n2,n3, s1,s2;
    
    public CalculadoraIMCFuncional(String t){  //Constructor para LA VENTANA
        
        super(t);
        setSize(400,200);
        setLocation(300,300);
        setVisible(true);
        setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE); //CIERRA LA VENTANA Y TERMINA EL PROGRAMA al clickear la X
        creaComponentes();
        colocaComponentes();
        setVisible(true);
    }
    
    
    public void creaComponentes(){
        n1=new JPanel();    //Se crean los paneles
        n2=new JPanel();
        n3=new JPanel();
        s1=new JPanel();
        s2=new JPanel();
        lblTit= new JLabel("Introduce los datos solicitados");
        lblTit.setForeground(Color.WHITE);
        lblPeso=new JLabel("Peso");
        lblEstat=new JLabel("Estatura");                        //Se "llenan" los componentes
        txtPeso=new JTextField(5);
        txtEstatura=new JTextField(5);
        btnCalcular=new JButton("Calcular IMC");
        lblIMCResultado = new JLabel();
        lblIMCResultado.setForeground(Color.BLUE);
        n1.setBackground(Color.BLUE);   //Se le asignan colores SOLO a los paneles
        
    }
    
    
    private void colocaComponentes(){
       // Implementa el ActionListener en la clase controlaBoton
        ActionListener controlaBoton = new ControlaBoton();
        
        setLayout(new GridLayout(5,1)); //Se coloca el gridLayout de 5 filas y 1 columna
        n1.add(lblTit); //se añade etiqueta al panel
        n2.add(lblPeso);//se añade etiqueta al panel
        n2.add(txtPeso);//se añade cajatexto al panel
        n3.add(lblEstat);//se añade etiqueta al panel
        n3.add(txtEstatura);//se añade cajatexto al panel
        s1.add(btnCalcular);//se añade boton al panel
        s2.add(lblIMCResultado);//se añade etiqueta al panel
        
        add(n1);    //Se añaden paneles a la Grid (tabla) de 5x1
        add(n2);
        add(n3);
        add(s1);
        add(s2);
        setVisible(true);
        
        // Asocia el ActionListener al botón
        btnCalcular.addActionListener(controlaBoton);
        
    }
    
    
    // Clase interna para controlar el evento del botón
    private class ControlaBoton implements ActionListener {

        @Override
        public void actionPerformed(ActionEvent e) {
            // Se ejecuta cuando se hace clic en el botón
            
            lblIMCResultado.setForeground(Color.white);
            CalculaIMC calc = new CalculaIMC(); //Objeto de la clase Calcula IMC

            double imc = calc.calculaIMC(txtPeso.getText(), txtEstatura.getText()); //asigna y llama el metodo que calcula el IMC en clase CalculaIMC
            String msg = null;
            DecimalFormat df = new DecimalFormat("#.0"); //Agrega el formato decimal para manejar un solo decimal
            
            if (imc < 18.5) {
                
                msg = "El IMC es: "+df.format(imc) + "; por lo tanto el peso es bajo";
                s2.setBackground(new Color(133, 192, 233));
                
            }else if ((imc >= 18.5) && (imc < 25) ) {
                
                msg = "El IMC es: "+df.format(imc) + "; por lo tanto el peso es normal";
                s2.setBackground(new Color(88, 214, 141));
                
            }else if ((imc >= 25) && (imc < 30) ) {
                
                lblIMCResultado.setForeground(Color.BLUE);
                msg = "El imc es: "+df.format(imc) + "; por lo tanto el peso es sobrepeso";
                s2.setBackground(new Color(249, 231, 159));
                
            }else if ((imc >= 30) && (imc < 35) ) {
                
                msg = "El IMC es: "+df.format(imc) + "; por lo tanto el peso es obesidad tipo 1";
                s2.setBackground(new Color(211, 84, 0));
                
            }else if ((imc >= 35) && (imc < 40) ) {
                
                msg = "El imc es: "+df.format(imc) + "; por lo tanto el peso es obesidad tipo 2";
                s2.setBackground(new Color(203, 67, 53));
                
            }else if (imc >40) {
                msg = "El IMC es: "+df.format(imc) + "; por lo tanto el peso es obesidad tipo 3";
                s2.setBackground(new Color(176, 58, 46));
            }
            lblIMCResultado.setText(msg);  //Aiigna el resultado a la etiqueta de resultado            
         }
        
    }
    
    public static void main(String[] args) {
         
        new CalculadoraIMCFuncional("Calculadora de IMC");
        
    }
}