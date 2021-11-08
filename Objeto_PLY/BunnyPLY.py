from OpenGL.GLUT import *
from OpenGL.GLU import *
from OpenGL.GL import *
from PLYLoader import *
x = 0

def display():
    global ply , x
    glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT)

    glPushMatrix()
    glTranslate(0,-0.1,7.4)
    glRotate(x,0,1,0)
    ply.draw()
    glPopMatrix()
    
    x+= 10
    glutSwapBuffers()

def timer(i):
    glutPostRedisplay()
    glutTimerFunc(50, timer, 1)

def main():
    global ply

    glutInit(sys.argv)
    glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGBA | GLUT_DEPTH | GLUT_MULTISAMPLE)
    glutInitWindowSize(800, 600)
    glutCreateWindow("Bunny")
    glutDisplayFunc(display)
    glEnable(GL_MULTISAMPLE)
    glEnable(GL_DEPTH_TEST)
    glClearColor(0., 0., 0., 1.)
    gluPerspective(45, 800.0/600.0, 0.5, 100.0)
    glTranslatef(0.0, 0.0, -8)
    glutTimerFunc(50, timer, 1)
    ply = PLY("bunny.ply")
    glutMainLoop()

main()
