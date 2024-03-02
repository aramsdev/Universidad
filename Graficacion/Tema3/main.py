import pygame as py
import math
from OpenGL.GLU import *
from OpenGL.GL import *
from OpenGL.GLUT import *
from pygame.locals import *
from PIL import *
import escenarios as es
import objetos as ob
import sonido as so

py.init()
py.mixer.init()

display = (600,600)
py.display.set_mode(display, DOUBLEBUF | OPENGL)

gluPerspective(45, (display[0]/display[1]),0.1,50.0)
glTranslatef(-2,0,-2)
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
    glColor3f(0.0,1.0,0.0)
    glPushMatrix()
    glTranslatef(-20,5,4)
    glScalef(0.5,0.5,0.5)
    # ob.draw_sphere(1,30,40)
    ob.draw_cube()
    # ob.draw_cone(1,2,40)
    glPopMatrix()

while True:
    for event in py.event.get():
        if event.type == py.QUIT:
            py.quit()
            quit()
        if event.type == py.KEYDOWN:
            if event.key == py.K_p:
                so.play("Sonidos/audio.mp3")
            if event.key == py.K_s:
                so.stop()
    
    x,y = py.mouse.get_rel()
    x *= mouse_sensivity
    y *= mouse_sensivity
    if x != 0:
        glRotate(x,0,1,0)
    py.mouse.set_pos(display[0]//2,display[1]//2)
    
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    es.draw_e5("/home/aramsdev/Graficacion/Tema2/Ejemplos3d/Imagenes/fondo.jpg")
    glEnable(GL_DEPTH_TEST)
    glPushMatrix()
    glRotate(180,0,1,0)
    draw()
    glPopMatrix()    
    py.display.flip()
    py.time.wait(100)