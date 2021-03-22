x1 = 10
y1 = 8

x2 = 9
y2 = 8

ponto1 = (10, 8)
ponto2 = (9, 8)
ponto3 = (10, 7)
ponto4 = (17, 18)

class Point():
    def __init__(self, coordX, coordY):
        self.x = coordX
        self.y = coordY

    def razao(self):
        r = self.x/self.y
        return r

p1 = Point(10,8)
p2 = Point(9,8)


print(ponto1)
print(p1.razao())
print(p2.razao())

