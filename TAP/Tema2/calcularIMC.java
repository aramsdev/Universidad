package GUI;

import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;
import javax.swing.JLabel;
import javax.swing.JTextField;

public class calcularIMC implements ActionListener{
    private JLabel resultado;
    private float estatura;
    private float peso;
    
    public calcularIMC(JTextField peso, JTextField estatura, JLabel resultado){
        this.peso = Float.parseFloat(peso.getText());
        this.estatura = Float.parseFloat(estatura.getText());
        this.resultado = resultado;
    }
    
    @Override
    public void actionPerformed(ActionEvent e) {
        float imc = peso / (estatura*estatura);
        if(imc  < 18.5){
            resultado.setText("Su IMC es de " + imc + ", por lo tanto es bajo.");
        } else if(imc > 18.5 && imc <= 24.9){
            resultado.setText("Su IMC es de " + imc + ", por lo tanto es normal.");
        } else if(imc >= 25 && imc <= 29.9){
            resultado.setText("Su IMC es de " + imc + ", por lo tanto tiene sobrepeso.");
        } else if(imc >= 30 && imc <= 34.9){
            resultado.setText("Su IMC es de " + imc + ", por lo tanto tiene obesidad clase 1.");
        } else if(imc >= 35 && imc <= 39.9){
            resultado.setText("Su IMC es de " + imc + ", por lo tanto tiene obesidad clase 2.");
        } else {
            resultado.setText("Su IMC es de " + imc + ", por lo tanto tiene obesidad clase 3.");
        }
    }    
}
