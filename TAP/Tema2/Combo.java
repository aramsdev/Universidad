package Menu;
import javax.swing.*;
import java.awt.*;
import java.awt.event.ItemEvent;
import java.awt.event.ItemListener;

public class Combo extends JFrame{
    
    public static void main(String[] args) {
        JFrame frame = new JFrame("Ejemplo Combox");
        frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        
        JPanel panel = new JPanel();
        JLabel label = new JLabel("Elige una opcion");
        panel.add(label);
        panel.setBackground(Color.cyan);
        frame.add(panel, BorderLayout.NORTH);
        
        JComboBox comboBox = new JComboBox();
        comboBox.addItem("Opcion 1");
        comboBox.addItem("Opcion 2");
        comboBox.addItem("Opcion 3");
        
        frame.add(comboBox, BorderLayout.CENTER);
        comboBox.addItemListener(new ItemListener(){
            @Override
            public void itemStateChanged(ItemEvent e){
                // Obtenemos el seleccionado
                String itemSeleccionado = (String) e.getItem();
                int estado = e.getStateChange();
                if(estado == ItemEvent.SELECTED){
                    JOptionPane.showMessageDialog(null, "El item seleccionado es " + itemSeleccionado);
                }
            }
        });
        
        frame.pack();
        frame.setVisible(true);
    }
    
}
