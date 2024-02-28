package practicas;

import java.awt.BorderLayout;
import java.awt.event.*;
import javax.swing.*;
import javax.swing.event.*;

public class TablaAlumnosLista extends JFrame implements ListSelectionListener, ActionListener{
    
    JList alumnos;
    JLabel inst;
    JTextField nombre;
    JButton agregar, eliminar;
    JPanel header, footer;
    JScrollPane scroll;
    DefaultListModel modelo;
    
    public TablaAlumnosLista(){
        setSize(600,400);
        getContentPane();
        setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        componentes();
        setVisible(true);
    }
    
    public void componentes(){
        header = new JPanel();
        footer = new JPanel();
        
        inst = new JLabel("Inserta Nombre:");
        nombre = new JTextField(10);
        
        agregar = new JButton("Agregar");
        agregar.addActionListener(this);
        
        eliminar = new JButton("Eliminar");
        eliminar.addActionListener(this);
        
        modelo = new DefaultListModel();
        alumnos = new JList(modelo);
        scroll = new JScrollPane(alumnos);
        
        header.add(inst);
        header.add(nombre);
        header.add(agregar);
        
        footer.add(eliminar);
        
        add(header, BorderLayout.NORTH);
        add(scroll, BorderLayout.CENTER);
        add(footer, BorderLayout.SOUTH);
    }

    @Override
    public void valueChanged(ListSelectionEvent e) {
    }

    @Override
    public void actionPerformed(ActionEvent e){
        if(e.getSource() == agregar){
            modelo.addElement(nombre.getText());
        } else if (e.getSource() == eliminar){
            int i = alumnos.getSelectedIndex();
            if(i != -1){
                modelo.remove(i);
            } else {
                JOptionPane.showMessageDialog(this, "Selecciona un alumno para eliminar", "Error", JOptionPane.ERROR_MESSAGE);
            }
        }
    }
    
    public static void main(String[] args) {
        new TablaAlumnosLista();
    }
    
}
