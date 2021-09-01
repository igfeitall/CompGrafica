from OpenGL.GLUT import *
from OpenGL.GLU import *
from OpenGL.GL import *
from math import *

density = 70
global_radius = 4
center_radius = 2


def donut(u, v):
    theta = (u * 2 * pi) / (density - 1)
    phi = (v * 2 * pi) / (density - 1)
    x = (global_radius + center_radius * cos(theta)) * cos(phi)
    y = (global_radius + center_radius * cos(theta)) * sin(phi)
    z = center_radius * sin(theta)

    return x, y, z


def color(i):
    if i <= density/2:
        c = i*2/(density)
        return [0, c*.5, c]
    else:
        c = 2 - 2*i/(density)
        return [c*.7, 0, c*.5]


def draw_donut():
    glBegin(GL_TRIANGLE_STRIP)
    for i in range(density):
        glColor3fv(color(i))
        for j in range(density):
            glVertex3fv(donut(i, j))
            glVertex3fv(donut(i+1, j))
    glEnd()


angle = 0


def draw():
    global angle

    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glPushMatrix()

    glRotatef(angle, 1, 1, 0)
    draw_donut()

    glPopMatrix()
    glutSwapBuffers()

    angle += 1


def timer(i):
    glutPostRedisplay()
    glutTimerFunc(50, timer, 1)


# PROGRAMA PRINCIPAL
glutInit(sys.argv)
glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGBA | GLUT_DEPTH | GLUT_MULTISAMPLE)
glutInitWindowSize(800, 600)
glutCreateWindow("Donut")
glutDisplayFunc(draw)
glEnable(GL_MULTISAMPLE)
glEnable(GL_DEPTH_TEST)
glClearColor(.8, .8, .8, 1.)
gluPerspective(45, 800.0/600.0, 0.1, 100.0)
glTranslatef(0.0, 0.0, -20)
glutTimerFunc(50, timer, 1)
glutMainLoop()
