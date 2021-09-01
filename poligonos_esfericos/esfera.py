from OpenGL.GLUT import *
from OpenGL.GLU import *
from OpenGL.GL import *
import math

r = 1
density = 50
halfpi = math.pi/2


def f(u, v):
    theta = (u*math.pi/(density-1)) - halfpi
    phi = (v*2*math.pi)/(density-1)

    x = r*math.cos(theta)*math.cos(phi)
    y = r*math.sin(theta)
    z = r*math.cos(theta)*math.sin(phi)
    return x, y, z


def color(i):
    c = i/(density-1)
    print(c)
    colorv = [c, c, c]
    return colorv


def desenhaEsfera():
    glBegin(GL_TRIANGLE_STRIP)
    for i in range(density):
        glColor3fv(color(i))
        for j in range(density):
            glVertex3fv(f(i, j))
            glVertex3fv(f(i+1, j))
    glEnd()


a = 0


def desenha():
    global a
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glPushMatrix()
    glRotatef(a, 0, 1, 0)
    desenhaEsfera()
    glPopMatrix()
    glutSwapBuffers()
    a += 1


def timer(i):
    glutPostRedisplay()
    glutTimerFunc(50, timer, 1)


# PROGRAMA PRINCIPAL
glutInit(sys.argv)
glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGBA | GLUT_DEPTH | GLUT_MULTISAMPLE)
glutInitWindowSize(800, 600)
glutCreateWindow("Esfera")
glutDisplayFunc(desenha)
glEnable(GL_MULTISAMPLE)
glEnable(GL_DEPTH_TEST)
glClearColor(0., 0., 0., 1.)
gluPerspective(45, 800.0/600.0, 0.1, 100.0)
glTranslatef(0.0, 0.0, -8)
glutTimerFunc(50, timer, 1)
glutMainLoop()
