import pygame as py
import math
from OpenGL.GLU import *
from OpenGL.GL import *
from OpenGL.GLUT import *
from pygame.locals import *
from PIL import *
import Personaje.personaje as personaje
import escenarios as es
import tkinter.messagebox as messagebox
import sonido as so
import iluminacion as il
import textos as txt
import colisiones as coli

py.init()
py.mixer.init()

display = (1000,1000)
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

speed = 0.1
move_duration = 1000
timer = None 
scene = 0

aux = 0
PosX_Objeto = 2
PosY_Objeto = 0
PosZ_Objeto = 0
Obj1_height = 4

def draw_mov(movX, movY):
    global PosX_Objeto, PosY_Objeto
    PosX_Objeto = PosX_Objeto + movX
    PosY_Objeto = PosY_Objeto + movY
    glEnable(GL_DEPTH_TEST)
    glPushMatrix()
    glTranslatef(PosX_Objeto, PosY_Objeto)
    
    glDisable(GL_LIGHTING)
    glDisable(GL_LIGHT0)

PosX_Objeto2 = 8
PosY_Objeto2 = 6
PosZ_Objeto2 = 4
Obj2_width = 1
Obj2_height = 1
Obj2_depth = 1

def draw_Objeto2():
    glEnable(GL_DEPTH_TEST)
    glPushMatrix()
    glTranslate(PosX_Objeto2, PosY_Objeto2, PosZ_Objeto2)
    il.iluminacion(0.0,0.0,1.0)
    draw()
    draw_body()
    draw_ext()
    draw_eyes()
    draw_helmet()
    draw_smile()
    
    glDisable(GL_LIGHTING)
    glDisable(GL_LIGHT0)
    glPopMatrix()

def draw():
    glEnable(GL_DEPTH_TEST)
    glEnable(GL_POLYGON_SMOOTH)
    glColor3f(0.89, 0.894, 0.8980) 
    glPushMatrix()
    glTranslatef(0, 0, 0)
    glScalef(2, 2, 2)
    personaje.draw_shield()
    glPopMatrix()

    glColor3f(0.9176470590,0.7450,0.2470)
    glPushMatrix()
    glTranslatef(0, 0, 0)
    glScalef(2, 2, 2)
    personaje.draw_beard()
    personaje.draw_hair()
    glPopMatrix()

def draw_helmet():
    glEnable(GL_DEPTH_TEST)
    glColor3f(1.0, 0.0, 0.0) 
    glPushMatrix()
    glTranslatef(0, 0, 0)
    glScalef(2, 2, 2)
    personaje.draw_helmet()
    glPopMatrix()  

def draw_body():
    glEnable(GL_DEPTH_TEST)
    glEnable(GL_POLYGON_SMOOTH)
    glColor3f(0.53, 0.53, 0.53) 
    glPushMatrix()
    glTranslatef(0, 0, 0)
    glScalef(2, 2, 2)
    personaje.draw_body()
    glPopMatrix() 

def draw_ext():
    glEnable(GL_DEPTH_TEST)
    glEnable(GL_POLYGON_SMOOTH)
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

def draw_eyes():
    glEnable(GL_DEPTH_TEST)
    glColor3f(0.2, 0.6, 1.0) 
    # Enojado
    # glColor3f(1.0, 0.0, 0.0) 
    glPushMatrix()
    glTranslatef(0, 0, 0)
    glScalef(2, 2, 2)
    personaje.draw_eyes()
    # personaje.draw_gino()
    glPopMatrix()

def draw_mad_eyes():
    glEnable(GL_DEPTH_TEST)
    glColor3f(1.0, 0.0, 0.0) 
    glPushMatrix()
    glTranslatef(0, 0, 0)
    glScalef(2, 2, 2)
    personaje.draw_eyes()
    glPopMatrix()

def draw_gino():
    glEnable(GL_DEPTH_TEST)
    glColor3f(0.2, 0.6, 1.0) 
    glPushMatrix()
    glTranslatef(0, 0, 0)
    glScalef(2, 2, 2)
    personaje.draw_gino()
    glPopMatrix()

def draw_smile():
    glEnable(GL_DEPTH_TEST)
    glColor3f(0.0, 0.0, 0.0) 
    glPushMatrix()
    glTranslatef(0, 0, 0)
    glScalef(2, 2, 2)
    personaje.draw_smile()
    # personaje.draw_sad()
    # personaje.draw_mad()
    glPopMatrix()

def draw_sad():
    glEnable(GL_DEPTH_TEST)
    glColor3f(0.0, 0.0, 0.0) 
    glPushMatrix()
    glTranslatef(0, 0, 0)
    glScalef(2, 2, 2)
    personaje.draw_sad()
    glPopMatrix()

def draw_mad():
    glEnable(GL_DEPTH_TEST)
    glColor3f(0.0, 0.0, 0.0) 
    glPushMatrix()
    glTranslatef(0, 0, 0)
    glScalef(2, 2, 2)
    personaje.draw_mad()
    glPopMatrix()

def draw_shout():
    glEnable(GL_DEPTH_TEST)
    glColor3f(0.0, 0.0, 0.0) 
    glPushMatrix()
    glTranslatef(0, 0, 0)
    glScalef(2, 2, 2)
    personaje.draw_shout()
    glPopMatrix()

messagebox.showinfo("Información", "Presione m para ver el menu")

while True:

    is_sad = False
    is_mad = False
    is_happy = True
    gino = False
    shout = False

    for event in py.event.get():
        if event.type == py.QUIT:
            py.quit()
            quit()
        elif event.type == py.KEYDOWN:
            if event.key == py.K_SPACE:
                timer = py.time.get_ticks()
            if event.key == py.K_t:
                is_sad = True
                is_happy = False
            if event.key == py.K_f:
                is_happy = True
            if event.key == py.K_e:
                is_mad = True
                is_happy = False
                so.play("/home/aramsdev/Desktop/Universidad/Graficacion/Tema3/Sonidos/sparta.mp3")
            if event.key == py.K_p:
                shout = True
                so.play("/home/aramsdev/Desktop/Universidad/Graficacion/Tema3/Sonidos/sparta.mp3")
            if event.key == py.K_g:
                gino = True
            if event.key == py.K_0:
                scene = 0
            if event.key == py.K_1:
                scene = 1
            if event.key == py.K_2:
                scene = 2
            if event.key == py.K_3:
                scene = 3
            if event.key == py.K_4:
                scene = 4
            if event.key==py.K_i:
                messagebox.showinfo("Información", "Nombre: Alexis Ramos Saldaña\nNúmero de control: 22280687")    
            if event.key == py.K_m:
                messagebox.showinfo("Menu", "Escenarios\n0 Roma 1.Bosque 2.Grecia 3.Troya 4.Coliseo\nEmociones\np.Triste e.Enojado g.Guiño f.Feliz t.Grito")    
    keys = py.key.get_pressed()

    if keys[py.K_a]:
        glTranslatef(10,0,0)

    if keys[py.K_w]:
        glTranslatef(0,0,-10)
    
    if keys[py.K_s]:
        glTranslatef(0,0,10)

    if keys[py.K_d]:
        glTranslatef(-10,0,0)

    if keys[py.K_x]:
        glTranslatef(0,-10,0)

    if keys[py.K_z]:
        glTranslatef(0,10,0)

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
    
    if keys[py.K_t]:
        is_sad = True
        is_happy = False

    if keys[py.K_e]:
        is_mad = True
        is_happy = False
    
    if keys[py.K_g]:
        gino = True

    if keys[py.K_p]:
        shout = True
        is_happy = False

    if keys[py.K_y]:
        glTranslatef(0,1,0)

    if keys[py.K_h]:
        glTranslatef(0,-1,0)
    
    if keys[py.K_g]:
        glTranslatef(-1,0,0)

    if keys[py.K_j]:
        glTranslatef(1,0,0)
        
    draw()
    # il.iluminacion(1.0, 1.0, 1.0)
    draw_body()
    draw_ext()
    draw_helmet()
    
    if is_sad:
        draw_sad()
        draw_eyes()
    elif is_mad:
        draw_mad_eyes()
        draw_mad()
    elif is_happy:
        draw_smile()
        draw_eyes()
    elif gino:
        draw_gino()
    elif shout:
        draw_shout()
        draw_mad_eyes()
    
    if coli.rombo_colision(PosX_Objeto2, PosY_Objeto2, PosZ_Objeto2,
                           Obj2_width, Obj2_height, Obj2_depth, PosX_Objeto,
                           PosY_Objeto, PosZ_Objeto, Obj1_height):
        txt.draw_text("Colision detectada", 8,8,4,50,150,14,0,0,0,0)
    else:
        txt.draw_text("Graficacion", 8,8,4,50,150,14,0,0,0,0)

    draw_Objeto2()
    
    glPopMatrix() 

    if scene == 0:
        es.draw_e5("/home/aramsdev/Desktop/Universidad/Graficacion/Tema3/ProyectoVideojuego/Imagenes/roma.jpeg")   
    elif scene == 1:
        es.draw_e5("/home/aramsdev/Desktop/Universidad/Graficacion/Tema3/ProyectoVideojuego/Imagenes/bosque.webp") 
    if scene == 2:
        es.draw_e5("/home/aramsdev/Desktop/Universidad/Graficacion/Tema3/ProyectoVideojuego/Imagenes/grecia.jpeg")   
    elif scene == 3:
        es.draw_e5("/home/aramsdev/Desktop/Universidad/Graficacion/Tema3/ProyectoVideojuego/Imagenes/troya.jpg")  
    if scene == 0:
        es.draw_e5("/home/aramsdev/Desktop/Universidad/Graficacion/Tema3/ProyectoVideojuego/Imagenes/coliseo.jpg") 

    py.display.flip()
    py.time.wait(100)