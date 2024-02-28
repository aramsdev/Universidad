package Menu;
import javax.swing.*;
import java.awt.*;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;
import javax.swing.event.TableModelEvent;
import javax.swing.event.TableModelListener;
import javax.swing.table.DefaultTableModel;

public class TareaAlumnosTablas extends JFrame implements TableModelListener, ActionListener{
    
    String[] columnas = {"Nombre"};
    Object[][] datos = {{"Alexis"},};
    
    JTable alumnos;
    DefaultTableModel modelo;
    JScrollPane scroll;
    Container c;
    JPanel panel,panel2;
    JButton botonInsertar, botonEliminar;
    JTextField nombre;
    JLabel insertarNombre;
    
    public TareaAlumnosTablas(){
        setTitle("Añadiendo y eliminado de una list scroll");
        setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        setSize(600,200);
        c = getContentPane();
        creaComponentes();
        colocaComponentes();
        setVisible(true);
    }
    
    private void creaComponentes(){
        modelo = new DefaultTableModel(datos, columnas);
        alumnos = new JTable(modelo);
        scroll = new JScrollPane(alumnos);
        alumnos.setDefaultEditor(Object.class, null);
        
        panel = new JPanel();
        panel2 = new JPanel();
        
        botonInsertar = new JButton("Insertar nombre");
        botonInsertar.addActionListener(this);
        botonEliminar = new JButton("Eliminar");
        botonEliminar.addActionListener(this);
        
        nombre = new JTextField(20);
        insertarNombre = new JLabel("Inserta un nombre");
    }
    
    private void colocaComponentes(){
        setLocationRelativeTo(null);
        
        panel2.add(insertarNombre);
        panel2.add(nombre);
        panel2.add(botonInsertar);
        
        c.add(panel2, BorderLayout.NORTH);
      
        alumnos.setFont(new Font("Arial", Font.PLAIN,14));      
        c.add(scroll, BorderLayout.CENTER);
        
        panel.add(botonEliminar);
        
        c.add(panel, BorderLayout.SOUTH);
        
        modelo.addTableModelListener(this);
    }
    
    
    
    @Override
    public void tableChanged(TableModelEvent e){
        int fila = e.getFirstRow();
        int columna = e.getColumn();
        
        if(fila >= 0 && columna >= 0){
            modelo.setValueAt(null, fila, columna);

            String nombreCol = modelo.getColumnName(columna);

            Object datoAnterior = datos[fila][columna];
            Object datoNvo = modelo.getValueAt(fila, columna);
        }   
    }
    
    @Override
    public void actionPerformed(ActionEvent e) {
        if(e.getSource() == botonInsertar){
            modelo.addRow(new Object[]{nombre.getText()});
        }
        if(e.getSource() == botonEliminar){
            int alumno = alumnos.getSelectedRow();
            if(alumno != -1){ // Check if a row is selected
            modelo.removeRow(alumno);
            } else {
                JOptionPane.showMessageDialog(this, "Por favor selecciona una fila para eliminar.", "Error", JOptionPane.ERROR_MESSAGE);
            }
        }
    }
    
    public static void main(String[] args) {
        new TareaAlumnosTablas();
    }
    
}
