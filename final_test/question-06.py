class Coordinate:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def distance(self, other):
        x_diff_sq = (self.x-other.x)**2
        y_diff_sq = (self.y-other.y)**2
        return (x_diff_sq + y_diff_sq)**0.5

    def __str__(self):
        return "<" + str(self.x) + "," + str(self.y) + ">"


class Coordinate3D(Coordinate):
    """ Uma coordenada3D contém valores x, y, e z"""

    def __init__(self, c=Coordinate(0, 0), a=0):
        """ Sets the x, y, and z values """
        super().__init__(c.x, c.y)  # point1#
        # self.x, self.y = c.x, c.y
        self.z = a  # point2#

    def distance(self, other):
        """Retorna a distância euclidiana entre duas Coordinate3D's"""
        x_diff_sq = (self.x-other.x)**2
        y_diff_sq = (self.y-other.y)**2
        z_diff_sq = (self.z-other.z)**2
        return (x_diff_sq + y_diff_sq + z_diff_sq)**0.5

    def __str__(self):
        return '[' + str(self.x) + ', ' + str(self.y) + ']'


# c3d = Coordinate3D
# print(Coordinate3D(Coordinate(1, 2), 3))
p1 = Coordinate(3, 4)
p2 = Coordinate3D(Coordinate(2, 3), 6)
orig1 = Coordinate(0, 0)
orig2 = Coordinate3D(orig1, 0)

# print(p1.distance(orig1))  # point3#

# print(p2.distance(orig2))  #point4#

# print(Coordinate3D.__str__(p1))  #point5#

print(p1.__str__() == p2.__str__())  #point6#
