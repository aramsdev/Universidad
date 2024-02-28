package Botones;

import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;
import javax.swing.JTextField;

public class BotonAccion implements ActionListener{
    JTextField bienvenida;
    
    public BotonAccion(JTextField bienvenida){
        this.bienvenida = bienvenida;
    }
    
    @Override
    public void actionPerformed(ActionEvent e) {
        bienvenida.setText("Hello, world! We are on Tec Toluca");
    }    
}
