package Botones;

import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;
import javax.swing.JLabel;
import javax.swing.JTextField;

public class implementaActionListener implements ActionListener{
    JTextField campo;
    JLabel responde;
    
    public implementaActionListener(JTextField campo, JLabel responde){
        this.campo = campo;
        this.responde = responde;
    }
    
    @Override
    public void actionPerformed(ActionEvent e) {
        StringBuilder builder = new StringBuilder(campo.getText());
        responde.setText(builder.reverse().toString());
    }
}
