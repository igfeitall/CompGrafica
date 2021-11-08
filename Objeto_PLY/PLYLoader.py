from OpenGL.GLUT import *
from OpenGL.GLU import *
from OpenGL.GL import *

class PLY:

    def __init__ (self, file):
        self.dir = file
        self.vertex_count = 35947
        self.face_count = 69451

    def _extract_data(self):
        ply_object = open(self.dir, 'r')
        
        lines = ply_object.read().splitlines()
        
        return self._get_data(lines[13:])

    def _get_data(self, lines):
        
        vectors = []
        faces = []

        for line in lines[:self.vertex_count]:
            aux = line.split(" ")
            vectors.append([float(x) for x in aux[:3]])
        
        for line in lines[(self.vertex_count + 1):]:
            aux = line.split(" ")
            faces.append(aux[1:4])

        return vectors , faces

    def draw(self):
      vectors , faces = self._extract_data()

      for face in faces:
        print(face)
        glBegin(GL_TRIANGLES)
        for vertex in face:
          print(vertex)
          print(vectors[int(vertex)])
          glVertex3fv(vectors[int(vertex)])
        glEnd()