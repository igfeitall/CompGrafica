import math
from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
from math import *

cores = ((1, 0, 0), (1, 1, 0), (0, 1, 0), (0, 1, 1), (0, 0, 1), (1, 0, 1))


def Piramide(base):
    # desenha base
    glBegin(GL_POLYGON)
    glColor((0, 1, 1))
    r = 1.
    for i in range(base):
        alph = (i/base) * (2 * math.pi)
        x = r * math.cos(alph)
        y = r * math.sin(alph)
        glVertex3f(x, y, -1)
    glEnd()

    # desenha topo
    glBegin(GL_TRIANGLE_FAN)
    glColor((1, 1, 1))
    glVertex3f(0, 0, 1)
    for i in range(base+1):
        cor = i % len(cores)
        glColor(cores[cor])
        alph = (i/base) * (2 * math.pi)
        x = r * math.cos(alph)
        y = r * math.sin(alph)
        glVertex3f(x, y, -1)
    glEnd()


a = 0


def desenha():
    global a
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glPushMatrix()
    # inclinei meu desenho 90 graus pra cima pra ela ficar em pé mais 13 pra poder ver a base bonita tb rs
    glRotatef(105, -1, 0, 0)
    glRotatef(a, 0, 0, 1)
    Piramide(6)
    glPopMatrix()
    glutSwapBuffers()
    a += 1


def timer(i):
    glutPostRedisplay()
    glutTimerFunc(50, timer, 1)


# PROGRAMA PRINCIPAL
if __name__ == '__main__':
    glutInit(sys.argv)
    glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGBA |
                        GLUT_DEPTH | GLUT_MULTISAMPLE)
    glutInitWindowSize(800, 600)
    glutCreateWindow("PIRAMIDE")
    glutDisplayFunc(desenha)
    glEnable(GL_MULTISAMPLE)
    glEnable(GL_DEPTH_TEST)
    glClearColor(0.7, 0.7, 0.7, 1.)
    gluPerspective(45, 800.0/600.0, 0.1, 100.0)
    glTranslatef(0.0, 0.0, -5)
    glutTimerFunc(50, timer, 1)
    glutMainLoop()
