import math

class Vector2(object):
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y
        self.EPS = 0.000001

    # Arithmetic
    def __add__(self, other):
        return Vector2(self.x + other.x, self.y + other.y)

    def __sub__(self, other):
        return Vector2(self.x - other.x, self.y - other.y)

    def __neg__(self):
        return Vector2(-self.x, -self.y)

    def __mul__(self, scalar):
        return Vector2(self.x * scalar, self.y * scalar)

    def __div__(self, scalar):
        if scalar != 0:
            return Vector2(self.x / float(scalar), self.y / float(scalar))
        return None

    def __truediv__(self, scalar):
        return self.__div__(scalar)

    # Comparisons
    def __eq__(self, other):
        if abs(self.x - other.x) < self.EPS:
            if abs(self.y - other.y) < self.EPS:
                return True
        return False

    # Magnitude
    def magnitude2(self):
        return self.x**2 + self.y**2

    def magnitude(self):
        return math.sqrt(self.magnitude2())

    # Conversions
    def copy(self):
        return Vector2(self.x, self.y)

    def asTuple(self):
        return self.x, self.y

    def asInt(self):
        return int(self.x), int(self.y)

    def __str__(self):
        return f"<{self.x}, {self.y}>"

    def __getitem__(self, i):
        return self.x if not bool(i) else self.y
    
