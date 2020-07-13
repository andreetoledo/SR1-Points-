import struct

def char(c):
    # 1 byte
    return struct.pack('=c', c.encode('ascii'))

def word(w):
    # 2 bytes
    return struct.pack('=h', w)

def dword(d):
    # 4 bytes
    return struct.pack('=l',d)

def color(r, g, b):
    return bytes([b, g, r])

BLACK = color(0,0,0)
WHITE = color(255,255,255)

class Render(object):
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.curr_color = WHITE
        self.clear()
    
    def clear(self):
        self.pixels = [ [ BLACK for x in range(self.width)] for y in range(self.height) ]

    def point(self, x, y):
        self.pixels[y][x] = self.curr_color

    def set_color(self, _color):
        self.curr_color = _color

    def write(self, filename):
        archivo = open(filename, 'wb')

        #File header 14 bytes
        archivo.write(char('B'))
        archivo.write(char('M'))
        archivo.write(dword(14 + 40 + self.width * self.height * 3))
        archivo.write(dword(0))
        archivo.write(dword(14 + 40))

        # Image Header 40 bytes
        archivo.write(dword(40))
        archivo.write(dword(self.width))
        archivo.write(dword(self.height))
        archivo.write(word(1))
        archivo.write(word(24))
        archivo.write(dword(0))
        archivo.write(dword(self.width * self.height * 3))
        archivo.write(dword(0))
        archivo.write(dword(0))
        archivo.write(dword(0))
        archivo.write(dword(0))

        #Pixels, 3 bytes cada uno

        for x in range(self.height):
            for y in range(self.width):
                archivo.write(self.pixels[x][y])

        archivo.close()

