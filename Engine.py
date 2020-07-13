from gl import Render
from gl import color

r = Render(400, 300)


r.set_color(color(255,0,0))

posX = 10
posY = 10

for x in range(100):
    r.point( posX, posY)
    posX += 1
    posY += 1

r.point(50,200)

#print(r.pixels)

r.write('output.bmp')