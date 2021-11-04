from OpenGL.GL import *
from OpenGL.GL.ARB import texture_query_levels
from OpenGL.GLUT import *
from OpenGL.GLU import *
import sys
import png
import math

# Some api in the chain is translating the keystrokes to this octal string
# so instead of saying: ESCAPE = 27, we use the following.
ESCAPE = b'\033'

# Number of the glut window.
window = 0

angle = [0,0]
r = [.5,1,.25]
density = 50
halfpi = math.pi/2

texture = []

def LoadTextures(arquivo):
    global texture
    texture.append(glGenTextures(1))

    ################################################################################
    glBindTexture(GL_TEXTURE_2D, texture[-1])
    reader = png.Reader(filename=arquivo)
    w, h, pixels, metadata = reader.read_flat()
    if(metadata['alpha']):
        modo = GL_RGBA
    else:
        modo = GL_RGB
    glPixelStorei(GL_UNPACK_ALIGNMENT,1)
    glTexImage2D(GL_TEXTURE_2D, 0, modo, w, h, 0, modo, GL_UNSIGNED_BYTE, pixels.tolist())
#    glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_WRAP_S, GL_CLAMP)
#    glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_WRAP_T, GL_CLAMP)
    glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_WRAP_S, GL_REPEAT)
    glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_WRAP_T, GL_REPEAT)
    glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_MAG_FILTER, GL_NEAREST)
    glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_MIN_FILTER, GL_NEAREST)
    glTexEnvf(GL_TEXTURE_ENV, GL_TEXTURE_ENV_MODE, GL_DECAL)
    ################################################################################


def InitGL(Width, Height):             
    LoadTextures("terra.png")
    LoadTextures("sol.png")
    LoadTextures("lua.png")
    glEnable(GL_TEXTURE_2D)
    glClearColor(0.0, 0.0, 0.0, 0.0) 
    glClearDepth(1.0)
    glDepthFunc(GL_LESS)               
    glEnable(GL_DEPTH_TEST)            
    glShadeModel(GL_SMOOTH)            
    glMatrixMode(GL_PROJECTION)
    gluPerspective(45.0, float(Width)/float(Height), 0.1, 100.0)
    glMatrixMode(GL_MODELVIEW)

def ReSizeGLScene(Width, Height):
    if Height == 0:                        
        Height = 1
    glViewport(0, 0, Width, Height)      
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluPerspective(45.0, float(Width)/float(Height), 0.1, 100.0)
    glMatrixMode(GL_MODELVIEW)

def f(u, v,index):
    theta = (u*math.pi/(density-1)) - halfpi
    phi = (v*2*math.pi)/(density-1)

    x = r[index]*math.cos(theta)*math.cos(phi)
    y = r[index]*math.sin(theta)
    z = r[index]*math.cos(theta)*math.sin(phi)
    return x, y, z

def DrawStar(index):
    glBindTexture(GL_TEXTURE_2D, texture[index])
    glBegin(GL_TRIANGLE_STRIP)

    for i in range(density):  
        for j in range(density):
            glTexCoord2f((49 - j)/(density - 1), (49 - i)/(density - 1)) 
            glVertex3fv(f(i,j,index))
            glTexCoord2f((49 - j)/(density - 1), (49 - i - 1)/(density - 1)) 
            glVertex3fv(f(i + 1,j,index))
    glEnd()

def OrbitPosition(x, y , z, distance, angle):    
    x2 = x + (distance * math.cos(angle))
    y2 = y + (distance * math.sin(angle))
    z2 = z

    return x2, y2, z2

def DrawGLScene():
    global rot, texture, angle

    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)    
    glLoadIdentity()                 
    glClearColor(0.1,0.1,0.1,1.0)            
    glTranslatef(0.0,0.0,-10.0)      

    #draw sun
    DrawStar(1)
    
    #draw earth
    glPushMatrix()
    earthPos = OrbitPosition(0,0,-10,7,angle[0])
    glTranslatef(*earthPos)
    DrawStar(0)
    glPopMatrix()

    #draw moon
    glPushMatrix()
    glTranslatef(*OrbitPosition(*earthPos,1.3,angle[1]))
    DrawStar(2)
    glPopMatrix()

    angle[0] += 0.02
    angle[1] += 0.2
    glutSwapBuffers()

def main():
    glutInit(sys.argv)
    glutInitDisplayMode(GLUT_RGBA | GLUT_DOUBLE | GLUT_DEPTH)    
    glutInitWindowSize(640, 480)
    glutInitWindowPosition(0, 0)
    glutCreateWindow("Textura Sistema solar")
    glutDisplayFunc(DrawGLScene)
    glutIdleFunc(DrawGLScene)
    glutReshapeFunc(ReSizeGLScene)
    InitGL(640, 480)
    glutMainLoop()

if __name__ == "__main__":
    main()
