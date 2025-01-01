class Point:
    def __init__(self, x, y)
        self.x = x
        self.y = y

    def __str__(self):
        return f"point({self.x}, {self.y})"

    def __add__(self, other):
        if isinstance(other, point):
            return point(self.x + other.x, self.y + other.y)
        return Notimplemented

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y              

print()              