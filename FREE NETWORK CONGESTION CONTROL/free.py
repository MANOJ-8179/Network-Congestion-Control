import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
import random

packets = []
congested = False

def draw_text(position, text):
    glRasterPos2f(*position)
    for char in text:
        glutBitmapCharacter(GLUT_BITMAP_HELVETICA_18, ord(char))

def draw_router():
    glColor3f(0.2, 0.3, 1)
    glPushMatrix()
    glutSolidSphere(0.5, 20, 20)  # Ensure OpenGL is ready before calling this
    glPopMatrix()

def draw_line():
    glColor3f(1, 1, 1)
    glBegin(GL_LINES)
    glVertex2f(-1, 0)
    glVertex2f(1, 0)
    glEnd()

def draw_packet(x, y):
    glColor3f(1, 0, 0)
    glBegin(GL_QUADS)
    glVertex2f(x - 0.05, y - 0.05)
    glVertex2f(x + 0.05, y - 0.05)
    glVertex2f(x + 0.05, y + 0.05)
    glVertex2f(x - 0.05, y + 0.05)
    glEnd()

def update_packets():
    global congested
    for p in packets:
        p[0] += 0.02 if not congested else 0.005
        if p[0] > 1:
            packets.remove(p)
    
    if random.random() < 0.1:
        packets.append([-1, 0])
    
    congested = len(packets) > 10

def draw_scene():
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glLoadIdentity()
    gluLookAt(0, 0, 5, 0, 0, 0, 0, 1, 0)

    draw_text((-0.5, 1), "Network Congestion Control")
    draw_router()
    draw_line()

    for p in packets:
        draw_packet(p[0], p[1])

    pygame.display.flip()

def main():
    pygame.init()
    display = (800, 600)
    pygame.display.set_mode(display, DOUBLEBUF | OPENGL)

    glutInit()  # Ensure GLUT is initialized
    glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGB | GLUT_DEPTH)  # Correct GLUT mode
    glEnable(GL_DEPTH_TEST)  # Enable depth testing for proper rendering

    gluOrtho2D(-2, 2, -2, 2)

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == QUIT or (event.type == KEYDOWN and event.key == K_ESCAPE):
                running = False

        update_packets()
        draw_scene()
        pygame.time.wait(50)

    pygame.quit()

if __name__ == "__main__":
    main()
