import math
#Returns a point
class Point():
    def __init__(self, _posX, _posY):
        self.posX, self.posY = _posX, _posY

    def getX(self):
        return self.posX

    def getY(self):
        return self.posY

get_num_digits = lambda d: math.floor(math.log(d, 10))+1
mix = lambda a, b, t: (b-a)*t + a
unmix = lambda v, a, b: (v-a)/(b-a)
constrain = lambda v, a, b: min(max(v, a), b)
dec = lambda a, d: float(int(a * pow(10, d))) / pow(10, d)
class Vector:
    def __init__ (self, x=0.0, y=0.0):
        self.x = x
        self.y = y
    def scale (self, n):
        return Vector(self.x * n, self.y * n)
    def mult (self, v):
        return Vector(self.x * v.x, self.y * v.y)
    def mag (self):
        return math.sqrt(self.x ** 2 + self.y ** 2)
    def neg (self):
        return Vector(-self.x, -self.y)
    def add (self, v):
        return Vector(self.x + v.x, self.y + v.y)
    def __add__ (self, v):
        if type(v) == Vector:
            return self.add(v)
        else:
            return self.add(Vector(v, v))
    def __sub__ (self, v):
        if type(v) == Vector:
            return self.sub(v)
        else:
            return self.sub(Vector(v, v))
    def __mul__ (self, v):
        if type(v) == Vector:
            return self.mult(v)
        else:
            return self.scale(float(v))
    def __truediv__ (self, v):
        if type(v) == Vector:
            return self.mult(Vector(1/v.x, 1/v.y))
        else:
            return self.mult(1/v)
    def sub (self, v):
        return self.add(v.neg())
    def dist (self, v):
        return self.sub(v).mag()
    def dot (self, v):
        return self.x * v.x + self.y * v.y
    def copy (self):
        return Vector(self.x, self.y)
    def to_tuple (self):
        return (self.x, self.y)
    def to_complex(self):
        return self.x + self.y*1j
    @staticmethod
    def from_complex(c):
        return Vector(c.real, c.imag)
    def normalize(self):
        return self.scale(1/max(self.mag(), 0.0001))
    def mix (self, v, t):
        return Vector(mix(self.x, v.x, t), mix(self.y, v.y, t))
    def to_int (self):
        return Vector(int(self.x), int(self.y))
    @staticmethod
    def in_box (position, size, point):
        return position.x <= point.x <= position.x + size.x and position.y <= point.y <= position.y + size.y
    def __str__ (self):
        return '<%s, %s>'%(self.x, self.y)
class Transform:
    def __init__ (self, translation=Vector(0,0), scale=Vector(1,1)):
        self.translation = translation
        self.scale = scale
    def transform_vector (self, vector):
        return vector.mult(self.scale).add(self.translation)
    def get_inverted_transform (self):
        return Transform(self.translation.neg(), Vector(1/self.scale.x, 1/self.scale.y))
