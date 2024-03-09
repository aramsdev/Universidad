import pygame as py
import math
from OpenGL.GLU import *
from OpenGL.GL import *
from OpenGL.GLUT import *
from pygame.locals import *
from PIL import *

def draw_head():
    glBegin(GL_QUADS)
    # Cara Frontal
    glVertex3f(3.95, -0.05, 3.5)
    glVertex3f(3.95, -0.05, 6.0)
    glVertex3f(-0.05, -0.05, 6.0)
    glVertex3f(-0.05, -0.05, 3.5)

    # Cara Trasera
    glVertex3f(3.95, -3.95, 3.5)
    glVertex3f(3.95, -3.95, 6.0)
    glVertex3f(-0.05, -3.95, 6.0)
    glVertex3f(-0.05, -3.95, 3.5)

    # Caras Laterales
    glVertex3f(3.95, -0.05, 3.5)
    glVertex3f(3.95, -3.95, 3.5)
    glVertex3f(3.95, -3.95, 6.0)
    glVertex3f(3.95, -0.05, 6.0)

    glVertex3f(-0.05, -0.05, 3.5)
    glVertex3f(-0.05, -3.95, 3.5)
    glVertex3f(-0.05, -3.95, 6.0)
    glVertex3f(-0.05, -0.05, 6.0)

    glVertex3f(-0.05, -0.05, 6.0)
    glVertex3f(3.95, -0.05, 6.0)
    glVertex3f(-0.05, -3.95, 6.0)
    glVertex3f(3.95, -3.95, 6.0)

    glVertex3f(3.95, -0.05, 3.5)
    glVertex3f(-0.05, -0.05, 3.5)
    glVertex3f(-0.05, -3.95, 3.5)
    glVertex3f(3.95, -3.95, 3.5)

    
    glEnd()  

def draw_body():
    glBegin(GL_QUADS)
    #Cara Frontal
    glVertex3f(4.0, 0.0, 3.5)
    glVertex3f(4.0, 0.0, 2.0)
    glVertex3f(0.0, 0.0, 2.0)
    glVertex3f(0.0, 0.0, 3.5)

    # Cara Trasera
    glVertex3f(4.0, -4.0, 3.5)
    glVertex3f(4.0, -4.0, 2.0)
    glVertex3f(0.0, -4.0, 2.0)
    glVertex3f(0.0, -4.0, 3.5)

    # Caras Laterales
    glVertex3f(4.0, 0.0, 3.5)
    glVertex3f(4.0, -4.0, 3.5)
    glVertex3f(4.0, -4.0, 2.0)
    glVertex3f(4.0, 0.0, 2.0)

    glVertex3f(0.0, 0.0, 3.5)
    glVertex3f(0.0, -4.0, 3.5)
    glVertex3f(0.0, -4.0, 2.0)
    glVertex3f(0.0, 0.0, 2.0)

    glVertex3f(0.0, 0.0, 2.0)
    glVertex3f(4.0, 0.0, 2.0)
    glVertex3f(0.0, -4.0, 2.0)
    glVertex3f(4.0, -4.0, 2.0)

    glVertex3f(4.0, 0.0, 3.5)
    glVertex3f(0.0, 0.0, 3.5)
    glVertex3f(0.0, -4.0, 3.5)
    glVertex3f(4.0, -4.0, 3.5)
    
    glEnd()   

def draw_right_leg():
    glBegin(GL_QUADS)
    #Cara Frontal
    glVertex3f(0.5,-1.5,0.0)
    glVertex3f(0.5,-2.5,0.0)        
    glVertex3f(1.5,-1.5,0.0)
    glVertex3f(1.5,-2.5,0.0)       
    
    #Cara Trasera
    glVertex3f(0.5,-1.5,2.0)
    glVertex3f(0.5,-2.5,2.0)        
    glVertex3f(1.5,-1.5,2.0)
    glVertex3f(1.5,-2.5,2.0)       
    
    #Caras Laterales
    glVertex3f(0.5,-1.5,0.0)
    glVertex3f(1.5,-1.5,0.0)
    glVertex3f(1.5,-1.5,2.0)
    glVertex3f(0.5,-1.5,2.0)  
    
    glVertex3f(0.5,-2.5,0.0)
    glVertex3f(1.5,-2.5,0.0)
    glVertex3f(1.5,-2.5,2.0)
    glVertex3f(0.5,-2.5,2.0) 
    
    glVertex3f(0.5,-1.5,0.0)
    glVertex3f(0.5,-1.5,2.0)
    glVertex3f(0.5,-2.5,0.0)  
    glVertex3f(0.5,-2.5,2.0)
    
    glVertex3f(1.5,-1.5,2.0)
    glVertex3f(1.5,-2.5,2.0) 
    glVertex3f(1.5,-1.5,0.0)
    glVertex3f(1.5,-2.5,0.0) 
    
    glEnd()

def draw_left_leg():
    glBegin(GL_QUADS)
    #Cara Frontal
    glVertex3f(2.5,-1.5,0.0)
    glVertex3f(2.5,-2.5,0.0)        
    glVertex3f(3.5,-1.5,0.0)
    glVertex3f(3.5,-2.5,0.0)       
    
    #Cara Trasera
    glVertex3f(2.5,-1.5,2.0)
    glVertex3f(2.5,-2.5,2.0)        
    glVertex3f(3.5,-1.5,2.0)
    glVertex3f(3.5,-2.5,2.0)       
    
    #Caras Laterales
    glVertex3f(2.5,-1.5,0.0)
    glVertex3f(3.5,-1.5,0.0)
    glVertex3f(3.5,-1.5,2.0)
    glVertex3f(2.5,-1.5,2.0)
    
    glVertex3f(2.5,-2.5,0.0)
    glVertex3f(3.5,-2.5,0.0)
    glVertex3f(3.5,-2.5,2.0)
    glVertex3f(2.5,-2.5,2.0) 
    
    glVertex3f(3.5,-2.5,0.0)
    glVertex3f(3.5,-2.5,2.0)       
    glVertex3f(3.5,-1.5,2.0)
    glVertex3f(3.5,-1.5,0.0)
    
    glVertex3f(2.5,-2.5,0.0)
    glVertex3f(2.5,-2.5,2.0)       
    glVertex3f(2.5,-1.5,2.0)
    glVertex3f(2.5,-1.5,0.0) 
    
    glEnd()

def draw_beard():
    glBegin(GL_QUADS)

    glVertex3f(0.0, 0.0, 3.5)
    glVertex3f(0.0, 0.0, 6.0)
    glVertex3f(0.5, 0.0, 6.0)
    glVertex3f(0.5, 0.0, 4.0)
    glVertex3f(1.5, 0.0, 4.0)
    glVertex3f(1.5, 0.0, 4.2)
    glVertex3f(2.5, 0.0, 4.2)
    glVertex3f(2.5, 0.0, 3.9)
    glVertex3f(3.5, 0.0, 3.9)
    glVertex3f(3.5, 0.0, 6.0)
    glVertex3f(4.0, 0.0, 6.0)
    glVertex3f(4.0, 0.0, 3.5)

    glVertex3f(4.0, 0.0, 3.5)
    glVertex3f(4.0, 0.0, 4.0)
    glVertex3f(2.5, 0.0, 4.0)
    glVertex3f(2.5, 0.0, 3.5)

    glVertex3f(0.0, 0.0, 3.5)
    glVertex3f(0.0, 0.0, 4.0)
    glVertex3f(1.5, 0.0, 4.0)
    glVertex3f(1.5, 0.0, 3.5)

    glVertex3f(2.5, 0.0, 4.0)
    glVertex3f(1.5, 0.0, 4.0)
    glVertex3f(1.5, 0.0, 3.9)
    glVertex3f(2.5, 0.0, 3.9)

    glVertex3f(2.5, 0.0, 3.6)
    glVertex3f(1.5, 0.0, 3.6)
    glVertex3f(1.5, 0.0, 3.5)
    glVertex3f(2.5, 0.0, 3.5)
    
    glVertex3f(0.0, 0.0, 6.0)
    glVertex3f(0.0, 0.0, 5.2)
    glVertex3f(3.5, 0.0, 5.2)
    glVertex3f(3.5, 0.0, 6.0)

    glEnd()

def draw_rigth_arm():
    glBegin(GL_QUADS)
    #Cara Frontal
    glVertex3f(4.0,-1.5,3.5)
    glVertex3f(4.0,-2.5,3.5)        
    glVertex3f(4.0,-1.5,3.0)
    glVertex3f(4.0,-2.5,3.0)       
    
    #Cara Trasera
    glVertex3f(5.0,-1.5,2.5)
    glVertex3f(5.0,-2.5,2.5)        
    glVertex3f(5.0,-1.5,2.0)
    glVertex3f(5.0,-2.5,2.0)       
    
    #Caras Laterales
    glVertex3f(5.0,-1.5,2.0)
    glVertex3f(5.0,-1.5,2.5)
    glVertex3f(4.0,-1.5,3.0)
    glVertex3f(4.0,-1.5,3.5)        
    
    glVertex3f(5.0,-2.5,2.0)
    glVertex3f(5.0,-2.5,2.5)
    glVertex3f(4.0,-2.5,3.0)
    glVertex3f(4.0,-2.5,3.5)  
    
    glVertex3f(5.0,-1.5,2.0)
    glVertex3f(5.0,-2.5,2.0)
    glVertex3f(4.0,-2.5,3.0)
    glVertex3f(4.0,-1.5,3.0)
    
    glVertex3f(5.0,-1.5,2.5)
    glVertex3f(5.0,-2.5,2.5)
    glVertex3f(4.0,-2.5,3.5)
    glVertex3f(4.0,-1.5,3.5) 
    
    glEnd()

def draw_left_arm():
    glBegin(GL_QUADS)
    #Cara Frontal
    glVertex3f(0.0,-1.5,3.5)
    glVertex3f(0.0,-2.5,3.5)        
    glVertex3f(0.0,-1.5,3.0)
    glVertex3f(0.0,-2.5,3.0)       
    
    #Cara Trasera
    glVertex3f(-1.0,-1.5,2.5)
    glVertex3f(-1.0,-2.5,2.5)        
    glVertex3f(-1.0,-1.5,2.0)
    glVertex3f(-1.0,-2.5,2.0)       
    
    #Caras Laterales
    glVertex3f(-1.0,-1.5,2.0)
    glVertex3f(-1.0,-1.5,2.5)
    glVertex3f(0.0,-1.5,3.0)
    glVertex3f(0.0,-1.5,3.5)        
    
    glVertex3f(-1.0,-2.5,2.0)
    glVertex3f(-1.0,-2.5,2.5)
    glVertex3f(0.0,-2.5,3.0)
    glVertex3f(0.0,-2.5,3.5)  
    
    glVertex3f(-1.0,-1.5,2.0)
    glVertex3f(-1.0,-2.5,2.0)
    glVertex3f(0.0,-2.5,3.0)
    glVertex3f(0.0,-1.5,3.0)
    
    glVertex3f(-1.0,-1.5,2.5)
    glVertex3f(-1.0,-2.5,2.5)
    glVertex3f(0.0,-2.5,3.5)
    glVertex3f(0.0,-1.5,3.5) 
    
    glEnd()

def draw_eyes():
    glBegin(GL_QUADS)

    glVertex3f(0.9, 0.0, 4.5)
    glVertex3f(1.4, 0.0, 4.5)
    glVertex3f(1.4, 0.0, 5.0)
    glVertex3f(0.9, 0.0, 5.0)

    glVertex3f(2.6, 0.0, 4.5)
    glVertex3f(3.1, 0.0, 4.5)
    glVertex3f(3.1, 0.0, 5.0)
    glVertex3f(2.6, 0.0, 5.0)

    glEnd()

def draw_hair():
    glBegin(GL_QUADS)

    glVertex3f(0.0, 0.0, 4.5)
    glVertex3f(0.0, 0.0, 6.0)
    glVertex3f(0.0, -4.0, 6.0)
    glVertex3f(0.0, -4.0, 4.5)

    glVertex3f(4.0, -4.0, 4.5)
    glVertex3f(4.0, -4.0, 6.0)
    glVertex3f(0.0, -4.0, 6.0)
    glVertex3f(0.0, -4.0, 4.5)

    glVertex3f(4.0, 0.0, 4.5)
    glVertex3f(4.0, 0.0, 6.0)
    glVertex3f(4.0, -4.0, 6.0)
    glVertex3f(4.0, -4.0, 4.5)

    glEnd()

def draw_smile():
    glBegin(GL_LINES)

    glVertex3f(2.4, 0.0, 3.8)
    glVertex3f(2.2, 0.0, 3.65)

    glVertex3f(2.2, 0.0, 3.65)
    glVertex3f(1.8, 0.0, 3.65)

    glVertex3f(1.8, 0.0, 3.65)
    glVertex3f(1.6, 0.0, 3.8)

    glEnd()

def draw_sad():
    glBegin(GL_LINES)

    glVertex3f(2.4, 0.0, 3.65)
    glVertex3f(2.2, 0.0, 3.8)

    glVertex3f(2.2, 0.0, 3.8)
    glVertex3f(1.8, 0.0, 3.8)

    glVertex3f(1.8, 0.0, 3.8)
    glVertex3f(1.6, 0.0, 3.65)

    glEnd()

def draw_mad():
    glBegin(GL_LINES)

    glVertex3f(2.4, 0.0, 3.8)
    glVertex3f(1.6, 0.0, 3.65)

    glEnd()

def draw_shout():
    glBegin(GL_QUADS)

    glVertex3f(2.4, 0.0, 3.65)
    glVertex3f(2.4, 0.0, 3.8)

    glVertex3f(1.6, 0.0, 3.8)
    glVertex3f(1.6, 0.0, 3.65)

    glEnd()

def draw_gino():
    glBegin(GL_QUADS)

    glVertex3f(0.9, 0.0, 4.5)
    glVertex3f(1.4, 0.0, 4.5)
    glVertex3f(1.4, 0.0, 5.0)
    glVertex3f(0.9, 0.0, 5.0)

    glVertex3f(2.6, 0.0, 4.6)
    glVertex3f(3.1, 0.0, 4.6)
    glVertex3f(3.1, 0.0, 4.8)
    glVertex3f(2.6, 0.0, 4.8)

    glEnd()
    

def draw_shield():
    
    glBegin(GL_QUADS)
    
    glVertex3f(5.0,-0.5,6)
    glVertex3f(5.0,-0.5,0.0)
    glVertex3f(5.0,-4,0.0)      
    glVertex3f(5.0,-4,6)        
    
    glEnd()

def draw_helmet():
    glBegin(GL_QUADS)
    
    glVertex3f(1.5, 0.0, 5.4)
    glVertex3f(2.5, 0.0, 5.4)
    glVertex3f(2.5, 0.0, 6.5)
    glVertex3f(1.5, 0.0, 6.5)
    
    glVertex3f(1.5, -4.0, 5.4)
    glVertex3f(2.5, -4.0, 5.4)
    glVertex3f(2.5, -4.0, 6.5)
    glVertex3f(1.5, -4.0, 6.5)    
    
    glVertex3f(2.5, 0.0, 6.5)
    glVertex3f(1.5, 0.0, 6.5)
    glVertex3f(1.5, -4.0, 6.5)
    glVertex3f(2.5, -4.0, 6.5)
    
    glVertex3f(1.5, 0.0, 5.4)
    glVertex3f(2.5, 0.0, 5.4)
    glVertex3f(2.5, -4.0, 5.4)
    glVertex3f(1.5, -4.0, 5.4)       

    glVertex3f(2.5, 0.0, 6.5)
    glVertex3f(2.5, 0.0, 5.4)
    glVertex3f(2.5, -4.0, 5.4)
    glVertex3f(2.5, -4.0, 6.5)
    
    glVertex3f(1.5, 0.0, 6.5)
    glVertex3f(1.5, 0.0, 5.4)
    glVertex3f(1.5, -4.0, 5.4)
    glVertex3f(1.5, -4.0, 6.5)    
    
    glEnd()


def draw_left_arm_up():
    glBegin(GL_QUADS)
    #Cara Frontal
    glVertex3f(0.0,-1.5,3.5)
    glVertex3f(0.0,-2.5,3.5)        
    glVertex3f(0.0,-1.5,3.0)
    glVertex3f(0.0,-2.5,3.0)       
    
    #Cara Trasera
    glVertex3f(-1.0,-1.5,4.5)
    glVertex3f(-1.0,-2.5,4.5)        
    glVertex3f(-1.0,-1.5,4.0)
    glVertex3f(-1.0,-2.5,4.0)       
    
    #Caras Laterales
    glVertex3f(-1.0,-1.5,4.0)
    glVertex3f(-1.0,-1.5,4.5)
    glVertex3f(0.0,-1.5,3.0)
    glVertex3f(0.0,-1.5,3.5)        
    
    glVertex3f(-1.0,-2.5,4.0)
    glVertex3f(-1.0,-2.5,4.5)
    glVertex3f(0.0,-2.5,3.0)
    glVertex3f(0.0,-2.5,3.5)  
    
    glVertex3f(-1.0,-1.5,4.0)
    glVertex3f(-1.0,-2.5,4.0)
    glVertex3f(0.0,-2.5,3.0)
    glVertex3f(0.0,-1.5,3.0)
    
    glVertex3f(-1.0,-1.5,4.5)
    glVertex3f(-1.0,-2.5,4.5)
    glVertex3f(0.0,-2.5,3.5)
    glVertex3f(0.0,-1.5,3.5) 
    
    glEnd()

def draw_right_arm_up():
    glBegin(GL_QUADS)
    #Cara Frontal
    glVertex3f(4.0,-1.5,3.5)
    glVertex3f(4.0,-2.5,3.5)        
    glVertex3f(4.0,-1.5,3.0)
    glVertex3f(4.0,-2.5,3.0)       
    
    #Cara Trasera
    glVertex3f(5.0,-1.5,4.5)
    glVertex3f(5.0,-2.5,4.5)        
    glVertex3f(5.0,-1.5,4.0)
    glVertex3f(5.0,-2.5,4.0)       
    
    #Caras Laterales
    glVertex3f(5.0,-1.5,4.0)
    glVertex3f(5.0,-1.5,4.5)
    glVertex3f(4.0,-1.5,3.0)
    glVertex3f(4.0,-1.5,3.5)        
    
    glVertex3f(5.0,-2.5,4.0)
    glVertex3f(5.0,-2.5,4.5)
    glVertex3f(4.0,-2.5,3.0)
    glVertex3f(4.0,-2.5,3.5)  
    
    glVertex3f(5.0,-1.5,4.0)
    glVertex3f(5.0,-2.5,4.0)
    glVertex3f(4.0,-2.5,3.0)
    glVertex3f(4.0,-1.5,3.0)
    
    glVertex3f(5.0,-1.5,4.5)
    glVertex3f(5.0,-2.5,4.5)
    glVertex3f(4.0,-2.5,3.5)
    glVertex3f(4.0,-1.5,3.5) 
    
    glEnd()
    
def draw_shield_up():  
    glBegin(GL_QUADS)
    
    glVertex3f(5.0,-0.5,8)
    glVertex3f(5.0,-0.5,2.0)
    glVertex3f(5.0,-4,2.0)      
    glVertex3f(5.0,-4,8)        
    
    glEnd()

def draw_move_right_leg():
    glBegin(GL_QUADS)
    #Cara Frontal
    glVertex3f(0.5,-0.5,0.0)
    glVertex3f(0.5,-1.5,0.0)        
    glVertex3f(1.5,-0.5,0.0)
    glVertex3f(1.5,-1.5,0.0)       
    
    #Cara Trasera
    glVertex3f(0.5,-1.5,2.0)
    glVertex3f(0.5,-2.5,2.0)        
    glVertex3f(1.5,-1.5,2.0)
    glVertex3f(1.5,-2.5,2.0)       
    
    #Caras Laterales
    glVertex3f(0.5,-0.5,0.0)
    glVertex3f(1.5,-0.5,0.0)
    glVertex3f(1.5,-1.5,2.0)
    glVertex3f(0.5,-1.5,2.0)  
    
    glVertex3f(0.5,-1.5,0.0)
    glVertex3f(1.5,-1.5,0.0)
    glVertex3f(1.5,-2.5,2.0)
    glVertex3f(0.5,-2.5,2.0) 
    
    glVertex3f(0.5,-0.5,0.0)
    glVertex3f(0.5,-1.5,2.0)
    glVertex3f(0.5,-1.5,0.0)  
    glVertex3f(0.5,-2.5,2.0)
    
    glVertex3f(1.5,-1.5,2.0)
    glVertex3f(1.5,-2.5,2.0) 
    glVertex3f(1.5,-0.5,0.0)
    glVertex3f(1.5,-1.5,0.0) 
    
    glEnd()

def draw_move_left_leg():
    glBegin(GL_QUADS)
    #Cara Frontal
    glVertex3f(2.5,-0.5,0.0)
    glVertex3f(2.5,-1.5,0.0)        
    glVertex3f(3.5,-0.5,0.0)
    glVertex3f(3.5,-1.5,0.0)       
    
    #Cara Trasera
    glVertex3f(2.5,-1.5,2.0)
    glVertex3f(2.5,-2.5,2.0)        
    glVertex3f(3.5,-1.5,2.0)
    glVertex3f(3.5,-2.5,2.0)       
    
    #Caras Laterales
    glVertex3f(2.5,-0.5,0.0)
    glVertex3f(3.5,-0.5,0.0)
    glVertex3f(3.5,-1.5,2.0)
    glVertex3f(2.5,-1.5,2.0)
    
    glVertex3f(2.5,-1.5,0.0)
    glVertex3f(3.5,-1.5,0.0)
    glVertex3f(3.5,-2.5,2.0)
    glVertex3f(2.5,-2.5,2.0) 
    
    glVertex3f(3.5,-1.5,0.0)
    glVertex3f(3.5,-2.5,2.0)       
    glVertex3f(3.5,-1.5,2.0)
    glVertex3f(3.5,-0.5,0.0)
    
    glVertex3f(2.5,-1.5,0.0)
    glVertex3f(2.5,-2.5,2.0)       
    glVertex3f(2.5,-1.5,2.0)
    glVertex3f(2.5,-0.5,0.0) 
    
    glEnd()
