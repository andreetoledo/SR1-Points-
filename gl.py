import struct


def color(r, g, b):
    return bytes([b, g, r])


def normalizeColorArray(colors_array):
    return [round(i*255) for i in colors_array]


def char(myChar):
		return struct.pack('=c', myChar.encode('ascii'))

def word(myChar):
	return struct.pack('=h', myChar)
	
def dword(myChar):
	return struct.pack('=l', myChar)

BLACK = color(0,0,0)

class Render(object):
    # glInit dont needed, 'cause we have an __init__ func
    def __init__(self):
        self.framebuffer = []
        self.width = 520
        self.height = 300
        self.viewport_x = 0
        self.viewport_y = 0
        self.viewport_width = 520
        self.viewport_height = 300
        self.glClear()

    def point(self, x, y):
        self.framebuffer[y][x] = self.color

    def glCreateWindow(self, width, height):
        self.height = height
        self.width = width

    def glViewport(self, x, y, width, height):
        # Setting viewport initial values
        self.viewport_x = x
        self.viewport_y = y
        self.viewport_height = height
        self.viewport_width = width

    def glClear(self):
        self.framebuffer = [
            [BLACK for x in range(self.width)] for y in range(self.height)
        ]

    def glClearColor(self, r=1, g=1, b=1):
        # get normalized colors as array
        normalized = normalizeColorArray([r,g,b])
        clearColor = color(normalized[0], normalized[1], normalized[2])

        self.framebuffer = [
            [clearColor for x in range(self.width)] for y in range(self.height)
        ]

    def glVertex(self, x, y):
        final_x = round((x+1) * (self.viewport_width/2) + self.viewport_x)
        final_y = round((y+1) * (self.viewport_height/2) + self.viewport_y)
        self.point(final_x, final_y)

    def glColor(self, r=0, g=0, b=0):
        # get normalized colors as array
        normalized = normalizeColorArray([r,g,b])
        self.color = color(normalized[0], normalized[1], normalized[2])

    def glFinish(self, filename='output.bmp'):
        # starts creating a new bmp file
        f = open(filename, 'bw')

        f.write(char('B'))
        f.write(char('M'))
        f.write(dword(14 + 40 + self.width * self.height * 3))
        f.write(dword(0))
        f.write(dword(14 + 40))

        # image header
        f.write(dword(40))
        f.write(dword(self.width))
        f.write(dword(self.height))
        f.write(word(1))
        f.write(word(24))
        f.write(dword(0))
        f.write(dword(self.width * self.height * 3))
        f.write(dword(0))
        f.write(dword(0))
        f.write(dword(0))
        f.write(dword(0))

        # finishing placing points
        for x in range(self.height):
            for y in range(self.width):
                f.write(self.framebuffer[x][y])

        f.close()