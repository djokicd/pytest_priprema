import numpy as np

class Mnogougao:
    def __init__(self, vertices = None):
        self.vertices = vertices
    
    def povrsina(self):
        area = 0
        numberOfVertices = len(self.vertices)
        for idx in range(numberOfVertices):
            x1, y1 = self.vertices[idx]
            x2, y2 = self.vertices[(idx + 1) % numberOfVertices]
            area += x1 * y2 - x2 * y1
        return abs(area) / 2
    
    def obim(self):
        perimeter = 0
        numberOfVertices = len(self.vertices)
        for idx in range(numberOfVertices):
            x1, y1 = self.vertices[idx]
            x2, y2 = self.vertices[(idx + 1) % numberOfVertices]
            side_length = np.sqrt((x2 - x1)**2 + (y2 - y1)**2)
            perimeter += side_length
        return perimeter 
  
    def rotiraj(self, alpha):
        radians = np.radians(alpha)
        rotation_matrix = np.array([[np.cos(radians), -np.sin(radians)],
                                    [np.sin(radians), np.cos(radians)]])
        for i in range(len(self.vertices)):
            x, y = self.vertices[i]
            self.vertices[i] = np.dot(rotation_matrix, np.array([x, y]))

    def centar(self):
        x = 0
        y = 0
        for i in range(len(self.vertices)):
            x += self.vertices[i][0]
            y += self.vertices[i][1]
        x /= len(self.vertices)
        y /= len(self.vertices)
        return (x, y)

class Kvadrat(Mnogougao):
    def __init__(self, a):
        if a <= 0:
            raise ValueError("Duzina stranice mora biti pozitivna.")
        self.vertices = [(0, 0), (a, 0), (a, a), (0, a)]

class Trougao(Mnogougao):
    def __init__(self, a, b, c):
        self.vertices = [(0, 0), (a, 0), (b, c)]

class PravougliTrougao(Trougao):
    def __init__(self, a, b):
        super().__init__(a, 0, b)
