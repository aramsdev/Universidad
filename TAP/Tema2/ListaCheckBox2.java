package Listas;


import java.awt.Container;
import java.awt.FlowLayout;
import java.awt.GridLayout;
import java.awt.event.ItemEvent;
import java.awt.event.ItemListener;
import javax.swing.DefaultListModel;
import javax.swing.JCheckBox;
import javax.swing.JFrame;
import javax.swing.JLabel;
import javax.swing.JList;
import javax.swing.JOptionPane;
import javax.swing.JScrollPane;
import javax.swing.event.ChangeEvent;
import javax.swing.event.ChangeListener;
import javax.swing.event.ListSelectionEvent;
import javax.swing.event.ListSelectionListener;

public class ListaCheckBox2 extends JFrame implements ItemListener{
    JCheckBox checkBox1, checkBox2, checkBox3;
    JLabel label;
    
    public ListaCheckBox2(){
        super("Ejemplo de etiquetas y checkbox con eventos");
        checkBox1 = new JCheckBox("Español");
        checkBox2 = new JCheckBox("Inglés");
        checkBox3 = new JCheckBox("Alemán");
        Container c = getContentPane();
        c.add(checkBox1);
        c.add(checkBox2);
        c.add(checkBox3);
        setLayout(new FlowLayout());
        label = new JLabel("idiomas seleccionados:");
        c.add(label);
        checkBox1.addItemListener(this);
        checkBox2.addItemListener(this);
        checkBox3.addItemListener(this);
        setSize(450,200);
        setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        setVisible(true);
    }
    
    @Override
    public void itemStateChanged(ItemEvent e){
        String idiomas = "";
        
        if(checkBox1.isSelected()){
            idiomas += "Español";
        }
        if(checkBox2.isSelected()){
            idiomas += "Inglés";
        }
        if(checkBox3.isSelected()){
            idiomas += "Alemán";
        }
        if(idiomas.length() == 0){
            idiomas += "Ninguno";
        }
        
        label.setText("Idiomas seleccionados: " + idiomas);
    }
    
    public static void main(String[] args) {
        new ListaCheckBox2();
    }

}
