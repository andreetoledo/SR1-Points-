from gl import Render
from gl import color

bmpFile = Render()
bmpFile.glCreateWindow(800, 600) # Screen size
bmpFile.glViewport(20, 20, 50 , 150) 
bmpFile.glClear()
bmpFile.glClearColor(0, 0, 0) # Black
bmpFile.glColor(0.53, 0.80, 0.92) # Added random color
bmpFile.glVertex(-1, -1) # Point on left lower corner
bmpFile.glVertex(0, 0) # Point on center
bmpFile.glVertex(1, 1) # Point on right upper corner
bmpFile.glFinish()