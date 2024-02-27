import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLUT import *

# Función para inicializar OpenGL
def init():
    glClearColor(0.0, 0.0, 0.0, 1.0)  # Color de fondo
    glFrustum(-1, 1, -1, 1, 1, 50)  # Configuración de la proyección
    

# Función para dibujar un cubo
def draw_cube():
    vertices = [
        [1, -1, -1],
        [1, 1, -1],
        [-1, 1, -1],
        [-1, -1, -1],
        [1, -1, 1],
        [1, 1, 1],
        [-1, -1, 1],
        [-1, 1, 1]
    ]

    edges = [
        [0, 1],
        [0, 3],
        [0, 4],
        [2, 1],
        [2, 3],
        [2, 7],
        [6, 3],
        [6, 4],
        [6, 7],
        [5, 1],
        [5, 4],
        [5, 7]
    ]

    glBegin(GL_LINES)
    for edge in edges:
        for vertex in edge:
            glVertex3fv(vertices[vertex])
    glEnd()

# Función para controlar la cámara
def camera_control():
    global x_translation, y_translation, z_translation, x_rotation, y_rotation

    keys = pygame.key.get_pressed()
    if keys[pygame.K_w]:
        z_translation += 0.1
    if keys[pygame.K_s]:
        z_translation -= 0.1
    if keys[pygame.K_a]:
        x_translation -= 0.1
    if keys[pygame.K_d]:
        x_translation += 0.1
    if keys[pygame.K_UP]:
        x_rotation -= 1
    if keys[pygame.K_DOWN]:
        x_rotation += 1
    if keys[pygame.K_LEFT]:
        y_rotation -= 1
    if keys[pygame.K_RIGHT]:
        y_rotation += 1

# Función principal
def main():
    global x_translation, y_translation, z_translation, x_rotation, y_rotation

    pygame.init()
    display = (800, 600)
    pygame.display.set_mode(display, DOUBLEBUF | OPENGL)

    init()

    x_translation, y_translation, z_translation = 0, 0, 0
    x_rotation, y_rotation = 0, 0

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        camera_control()

        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
        glMatrixMode(GL_MODELVIEW)
        glLoadIdentity()
        glTranslatef(x_translation, y_translation, z_translation)
        glRotatef(x_rotation, 1, 0, 0)
        glRotatef(y_rotation, 0, 1, 0)

        draw_cube()

        pygame.display.flip()
        pygame.time.wait(10)

main()
