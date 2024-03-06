import pygame as py
from OpenGL.GLU import *
from OpenGL.GL import *
from OpenGL.GLUT import *

def draw_text(text, PosX, porY, PosZ, SizeFont, R,G,B,RB,GB,BB):
    font = py.font.Font(None, SizeFont)
    text_surface = font.render(text, True, (R,G,B), (RB,GB,BB))
    text_data = py.image.tostring(text_surface, "RGBA", True)
    glRasterPos3d(text_surface.get_width(), text_surface.get_height()
                  , GL_RGBA, GL_UNSIGNED_BYTE
                  , text_data)