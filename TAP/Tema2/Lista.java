package Listas;


import java.awt.GridLayout;
import javax.swing.DefaultListModel;
import javax.swing.JFrame;
import javax.swing.JList;
import javax.swing.JOptionPane;
import javax.swing.JScrollPane;
import javax.swing.event.ListSelectionEvent;
import javax.swing.event.ListSelectionListener;

public class Lista extends JFrame implements ListSelectionListener{
    JList lista;
        JList list;
    JScrollPane pane;
    
    public Lista(){
        super("Ejemplo de JList");
        setLayout(new GridLayout(2,1));
        list = new JList();
        pane = new JScrollPane(list);
        String elementos[]= {"uno", "dos", "tres"};
        lista = new JList(elementos);
        DefaultListModel model = new DefaultListModel();
        model.addElement("Opcion 1");
        model.addElement("Opcion 2");
        model.addElement("Opcion 3");
        list.setModel(model);
        getContentPane().add(pane);
        getContentPane().add(lista);
        list.addListSelectionListener(this);
        lista.addListSelectionListener(this);
        pack();
        setLocationRelativeTo(null);
        setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        setVisible(true);
    }
    
    public static void main(String[] args) {
        new Lista();
    }
    
    @Override
    public void valueChanged(ListSelectionEvent e){
        if(e.getSource() == list){
            JOptionPane.showMessageDialog(this, "La opcion seleccionada es " + list.getSelectedValue());
        } else {
            JOptionPane.showMessageDialog(this, "La opcion seleccionada es: " + lista.getSelectedValue());
        }
    }
}
