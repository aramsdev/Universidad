package Menu;

import java.awt.*;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;
import javax.swing.*;

public class MenuSimple extends JFrame implements ActionListener{
    
    public static final int ANCHO = 400;
    public static final int ALTO = 300;
    private JPanel panelRojo;
    private JPanel panelBlanco;
    private JPanel panelVerde;
    private JMenuItem redChoice, whiteChoice,greenChoice,exitChoice,cleanChoice;
    
    
    public MenuSimple(){
        super("Demostración Menu Simple");
        setSize(ANCHO, ALTO);
        setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        setLayout(new GridLayout(1,3));        
        panelRojo = new JPanel();
        panelRojo.setBackground(Color.LIGHT_GRAY);
        panelBlanco = new JPanel();
        panelBlanco.setBackground(Color.LIGHT_GRAY);
        panelVerde = new JPanel();
        panelVerde.setBackground(Color.LIGHT_GRAY);
        add(panelVerde);
        add(panelBlanco);
        add(panelRojo);
        
        // Creando un menú de opciones similares
        JMenu colorMenu = new JMenu("Colores");
        
        // Poniendo un nemónico al menu anterior
        colorMenu.setMnemonic('C');
        
        // Creando opciones para el menu anterior
        redChoice = new JMenuItem("Rojo");
        whiteChoice = new JMenuItem("Blanco");
        greenChoice = new JMenuItem("Verde");
        
        redChoice.addActionListener(this);
        whiteChoice.addActionListener(this);
        greenChoice.addActionListener(this);
        
        
        colorMenu.add(greenChoice);
        colorMenu.add(whiteChoice);
        colorMenu.add(redChoice);
        
        // Creando otro menu 
        JMenu otroMenu = new JMenu("Otro");
        otroMenu.setMnemonic('O');
        
        // Creando opciones
        cleanChoice = new JMenuItem("Limpiar");
        cleanChoice.addActionListener(this);
        
        // Colocando una combinacion de teclas a la opcion recien creada
        cleanChoice.setAccelerator(KeyStroke.getKeyStroke('L',1));
        
        exitChoice = new JMenuItem("Salir");
        exitChoice.addActionListener(this);
        
        // Agregando las opciones
        otroMenu.add(cleanChoice);
        otroMenu.add(exitChoice);
        
        // Creando la barra de menu
        JMenuBar bar = new JMenuBar();
        
        // Añadiendo menus a la barra
        bar.add(colorMenu);
        bar.add(otroMenu);
        
        // Poniendo la barra de menú en la ventana
        setJMenuBar(bar);
        setLocationRelativeTo(null);
        setVisible(true);
    }
    
    @Override
    public void actionPerformed(ActionEvent e) {
        
        if(e.getSource() == whiteChoice){
            panelBlanco.setBackground(Color.WHITE);
        } else if(e.getSource() == greenChoice){
            panelVerde.setBackground(Color.GREEN);
        } else if(e.getSource() == redChoice){
            panelRojo.setBackground(Color.RED);
        } else if(e.getSource() == cleanChoice){
            panelBlanco.setBackground(Color.LIGHT_GRAY);
            panelRojo.setBackground(Color.LIGHT_GRAY);
            panelVerde.setBackground(Color.LIGHT_GRAY);
        } else if(e.getSource() == exitChoice){
            
        }

    }
    
    public static void main(String[] args) {
        new MenuSimple();
    }
}
