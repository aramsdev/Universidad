package Menu;
import java.awt.*;
import java.awt.event.*;
import javax.swing.*;

public class radioBotones extends JFrame implements ActionListener {
    
    JPanel panel;
    
    public radioBotones(){
        super("Ejemplo de etiquetas y radiobotones");
        setSize(300,200);
        setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        panel = new JPanel();
        add(panel);
        
        JLabel etiqueta = new JLabel("Elige tu color favorito");
        panel.add(etiqueta);
        
        JRadioButton rojo = new JRadioButton("Rojo");
        JRadioButton verde = new JRadioButton("Verde");
        JRadioButton azul = new JRadioButton("Azul");
        
        // Creamos un grupo de botones para que solo se pueda seleccionar uno de ellos
        
        ButtonGroup grupo = new ButtonGroup();
        grupo.add(rojo);
        grupo.add(verde);
        grupo.add(azul);
        panel.add(rojo);
        panel.add(verde);
        panel.add(azul);
        setVisible(true);
        
        // Añadiremos un escuchador de eventos a los botones
        
        rojo.addActionListener(this);
        verde.addActionListener(this);
        azul.addActionListener(this);       
    }
    
    public static void main(String[] args) {
        new radioBotones();
    }
    
    @Override
    public void actionPerformed(ActionEvent e){
        //Obtenemos el radioboton seleccionado
        JRadioButton radioBotonSeleccionado = (JRadioButton) e.getSource();
        String color = radioBotonSeleccionado.getText();
        
        System.out.println("Genero seleccionado: " + color);
        
        switch(color){
            case "Rojo":
                panel.setBackground(Color.red);
                break;
            case "Verde":
                panel.setBackground(Color.GREEN);
                break;
            case "Azul":
                panel.setBackground(Color.BLUE);
                break;
        }
    }
    
}
