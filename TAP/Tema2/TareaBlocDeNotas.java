package Tema2;

import javax.swing.*;
import java.awt.*;
import java.awt.event.*;
import java.io.*;

public class TareaBlocDeNotas extends JFrame implements ActionListener{
    private JTextArea texto;
    JMenuBar menu;
    JMenu menuArchivos;
    JMenuItem abrir, guardar,cerrar;
    JFileChooser fc = new JFileChooser();

    public static void main(String[] args) {
        new TareaBlocDeNotas();
    }
    
    public TareaBlocDeNotas(){
        setTitle("File to JTextField Example");
        setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        getContentPane();
        setSize(400, 300);
        colocaComponentes();
        setVisible(true);
    }

    private void colocaComponentes() {
        texto = new JTextArea(10,30);
        JScrollPane scroll = new JScrollPane(texto);
        add(scroll, BorderLayout.CENTER);
        

        menu = new JMenuBar();
        setJMenuBar(menu);

        menuArchivos = new JMenu("Opciones");
        menu.add(menuArchivos);

        abrir = new JMenuItem("Abrir Archivo");
        abrir.setAccelerator(KeyStroke.getKeyStroke('O',1));
        abrir.addActionListener(this);
        menuArchivos.add(abrir);

        guardar = new JMenuItem("Guardar Archivo");
        guardar.addActionListener(this);
        guardar.setAccelerator(KeyStroke.getKeyStroke('G',1));
        guardar.setEnabled(false);
        menuArchivos.add(guardar);

        cerrar = new JMenuItem("Cerrar Archivo");
        cerrar.addActionListener(this);
        menuArchivos.add(cerrar);
    }
    
    @Override
    public void actionPerformed(ActionEvent e){
        if(e.getSource() ==  abrir){
            int returnValue = fc.showOpenDialog(null);
            if (returnValue == JFileChooser.APPROVE_OPTION) {
                File selectedFile = fc.getSelectedFile();
                try {
                    FileReader reader = new FileReader(selectedFile);
                    BufferedReader br = new BufferedReader(reader);
                    StringBuilder sb = new StringBuilder();
                    String linea;
                    while ((linea = br.readLine()) != null) {
                        sb.append(linea).append("\n");
                    }
                    br.close();
                    texto.setText(sb.toString());
                } catch (IOException ex) {
                    ex.printStackTrace();
                    JOptionPane.showMessageDialog(null, "Error leyendo el archivo", "Error", JOptionPane.ERROR_MESSAGE);
                }
            }
            guardar.setEnabled(true);
        } else if(e.getSource() == guardar){
            int returnValue = fc.showSaveDialog(null);
            if (returnValue == JFileChooser.APPROVE_OPTION) {
                File selectedFile = fc.getSelectedFile();
                try (PrintWriter writer = new PrintWriter(selectedFile)) {
                    writer.print(texto.getText());
                    JOptionPane.showMessageDialog(null, "Archivo guardado", "Exito!", JOptionPane.INFORMATION_MESSAGE);
                } catch (IOException ex) {
                    ex.printStackTrace();
                    JOptionPane.showMessageDialog(null, "Error guardando el archivo", "Error", JOptionPane.ERROR_MESSAGE);
                }
            }
        } else if (e.getSource() == cerrar){
            texto.setText("");
            guardar.setEnabled(false);
        }
    }
}
