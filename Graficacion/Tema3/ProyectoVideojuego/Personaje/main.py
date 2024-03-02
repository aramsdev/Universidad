import pygame as py
import math
from OpenGL.GLU import *
from OpenGL.GL import *
from OpenGL.GLUT import *
from pygame.locals import *
from PIL import *
import personaje

py.init()
py.mixer.init()

display = (600,600)
py.display.set_mode(display, DOUBLEBUF | OPENGL)

gluPerspective(45, (display[0]/display[1]),0.1,50.0)
glTranslatef(0,0,-5)
glOrtho(0,15,0,15,0,6)


camara_speed = 0.1
rotacion_speed = 0.2
mouse_sensivity = 0.1
py.event.set_grab(True)
py.mouse.set_visible(False)
ban = 0
directorio_script = os.path.dirname(os.path.abspath(__file__))

def draw():
    glEnable(GL_DEPTH_TEST)

    glColor3f(0.4, 0.2, 0.0) 
    glPushMatrix()
    glTranslatef(0, 0, 0)
    glScalef(2, 2, 2)
    personaje.draw_beard()
    personaje.draw_hair()
    glPopMatrix()

    glColor3f(0.0, 0.0, 0.0) 
    glPushMatrix()
    glTranslatef(0, 0, 0)
    glScalef(2, 2, 2)
    # personaje.draw_smile
    # personaje.draw_sad()
    personaje.draw_mad()
    glPopMatrix()

    # glColor3f(0.2, 0.6, 1.0) 
    # Enojado
    glColor3f(1.0, 0.0, 0.0) 
    glPushMatrix()
    glTranslatef(0, 0, 0)
    glScalef(2, 2, 2)
    # personaje.draw_eyes()
    personaje.draw_gino()
    glPopMatrix()
    
    glColor3f(1.0, 0.92, 0.92) 
    glPushMatrix()
    glTranslatef(0, 0, 0)
    glScalef(2, 2, 2)
    personaje.draw_rigth_leg()
    personaje.draw_left_leg()
    personaje.draw_head()
    personaje.draw_rigth_arm()
    personaje.draw_left_arm()
    glPopMatrix()

    glColor3f(0.53, 0.53, 0.53) 
    glPushMatrix()
    glTranslatef(0, 0, 0)
    glScalef(2, 2, 2)
    personaje.draw_body()
    glPopMatrix()

speed = 0.1
move_duration = 1000
timer = None 

while True:
    for event in py.event.get():
        if event.type == py.QUIT:
            py.quit()
            quit()
        elif event.type == py.KEYDOWN:
            if event.key == py.K_SPACE:
                timer = py.time.get_ticks()
    
    current_time = py.time.get_ticks()
    if timer:
        if current_time - timer <= move_duration:
            glTranslatef(0.0,speed, 0.0) 
        else:
            timer = None
    
    x,y = py.mouse.get_rel()
    x *= mouse_sensivity
    y *= mouse_sensivity
    if x != 0:
        glRotate(x,0,1,0)
    py.mouse.set_pos(display[0]//2,display[1]//2)
    
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glEnable(GL_DEPTH_TEST)
    glPushMatrix()
    glRotatef(-90, 1, 0, 0) 
    glRotatef(-90, 0, 0, 1) 
    draw()
    glPopMatrix()    
    py.display.flip()
    py.time.wait(100)