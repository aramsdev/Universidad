import pygame as py
import math
from OpenGL.GLU import *
from OpenGL.GL import *
from OpenGL.GLUT import *
from pygame.locals import *
from PIL import *

def draw_sphere(radius, num_slices, num_segments):
    for i in range(num_slices + 1):
        lat0 = math.pi * (-0.5 + (i-1)/num_slices)
        z0 = radius * math.sin(lat0)
        zr0 = radius * math.cos(lat0)
        
        lat1 = math.pi * (-0.5 + i/num_slices)
        z1 = radius * math.sin(lat1)
        zr1 = radius * math.cos(lat1)
        
        glBegin(GL_QUAD_STRIP)
        
        for j in range(num_segments + 1):
            lng = 2 * math.pi * j / num_segments
            x = zr0 * math.cos(lng)
            y = zr0 * math.sin(lng)
            
            glNormal3f(x,y,z0)
            glVertex3f(x,y,z0)
            
            x = zr1 * math.cos(lng)
            y = zr1 * math.sin(lng)
            
            glNormal3f(x,y,z1)
            glVertex3f(x,y,z1)
        
        glEnd()

def draw_cube():
    glBegin(GL_QUADS)
    #Cara Frontal
    glVertex3f(-10.0,-10.0,10.0)
    glVertex3f(10.0,-10.0,10.0)        
    glVertex3f(10.0,10.0,10.0)        
    glVertex3f(-10.0,10.0,10.0)     
    
    #Cara Trasera
    glVertex3f(-10.0,-10.0,-10.0)
    glVertex3f(10.0,-10.0,-10.0)        
    glVertex3f(10.0,10.0,-10.0)        
    glVertex3f(-10.0,10.0,-10.0)   
    
    #Caras Laterales
    glVertex3f(-10.0,-10.0,10.0)
    glVertex3f(10.0,-10.0,10.0)        
    glVertex3f(10.0,-10.0,-10.0)        
    glVertex3f(-10.0,-10.0,-10.0)    
    
    glVertex3f(-10.0,10.0,10.0)
    glVertex3f(10.0,10.0,10.0)        
    glVertex3f(10.0,10.0,-10.0)        
    glVertex3f(-10.0,10.0,-10.0)    
    
    glVertex3f(-10.0,-10.0,10.0)
    glVertex3f(-10.0,10.0,10.0)        
    glVertex3f(-10.0,10.0,-10.0)        
    glVertex3f(-10.0,-10.0,-10.0)  
    
    glVertex3f(10.0,-10.0,10.0)
    glVertex3f(10.0,10.0,10.0)        
    glVertex3f(10.0,10.0,-10.0)        
    glVertex3f(10.0,-10.0,-10.0) 
    
    glEnd()    

def draw_cone(radius, height, num_segments):
    glBegin(GL_TRIANGLE_FAN)  
    glVertex3f(0,0,height)
    for i in range(num_segments + 1):
        theta = 2.0 * math.pi * i/num_segments
        x = radius * math.cos(theta)
        y = radius * math.sin(theta)
        glVertex3f(x,y,0)
    glEnd()
    
    glBegin(GL_TRIANGLE_FAN)  
    glVertex3f(0,0,0)
    for i in range(num_segments + 1):
        theta = 2.0 * math.pi * i/num_segments
        x = radius * math.cos(theta)
        y = radius * math.sin(theta)
        glVertex3f(x,y,0)
    glEnd()
    
    glBegin(GL_TRIANGLE_FAN)  
    glVertex3f(0,0,height)
    for i in range(num_segments + 1):
        theta = 2.0 * math.pi * i/num_segments
        x = radius * math.cos(theta)
        y = radius * math.sin(theta)
        glVertex3f(x,y,0)
    glEnd()
    
