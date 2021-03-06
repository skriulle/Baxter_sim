#-*- coding:utf-8 -*-

import numpy as np
from numpy import cos, sin

PI = np.pi

class Baxter_Link:
    
    def __init__(self, num, inertias, com, dh):
        self.num = num
        self.__intertias = inertias
        #__inertias has 6 values of inertias of the link(xx, yy, zz, xy, yz, xz)
        com.append(1)
        self.com = np.matrix(com).T
        #com has the position of Center of Mass(x, y, z)
        self.d, self.a, self.alfa, self.m = dh
        #__dh has the Denavit-Hartenberg parameters(d, a, alfa, m)

    def __str__(self):
        res = self.__class__.__name__
        res += '@'
        res += '0x'
        res += '%X' % id(self)
        res += '[\n'
        res += '-number='
        res += '%d' % self.num
        res += ',\n-intertias(xx, xy, xz, yy, yz, zz)\n  ='
        res += str(self.__intertias)
        res += ',\n-CenterOfMass='
        res += str(self.com)
        res += ',\n-DH parameters(d, a, alfa, m)='
        res += str([self.d, self.a, self.alfa, self.m])
        res += '\n]'
        return res
        
    def get_T_Matrix(self, theta=0):
        #This function of object L(i) returns transform matrix ^(i-1)T_(i)
        d, a, alfa, m = self.d, self.a, self.alfa, self.m
        #print d, a, alfa, m
        #print self
        return np.matrix([
            [cos(theta), -cos(alfa)*sin(theta),  sin(alfa)*sin(theta), a*cos(theta)],
            [sin(theta),  cos(alfa)*cos(theta), -sin(alfa)*cos(theta), a*sin(theta)],
            [         0,             sin(alfa),             cos(alfa),            d],
            [         0,                     0,                     0,            1]
        ])

    def J(self):
        xx, yy, zz, xy, yz, xz = self.__intertias
        d, a, alfa, m = self.d, self.a, self.alfa, self.m
        x, y, z, _ = map(int, self.com)
        return np.matrix([
            [(-xx+yy+zz)/2,           xy,            xz, m*x],
            [           xy, (xx-yy+zz)/2,            yz, m*y],
            [           xz,           yz, (+xx+yy-zz)/2, m*z],
            [          m*x,          m*y,           m*z,   m]
        ])

    def Q(self):
        return np.matrix([
            [ 0, -1, 0, 0],
            [ 1,  0, 0, 0],
            [ 0,  0, 0, 0],
            [ 0,  0, 0, 0]
        ])

        


class Baxter_Test():

    def __init__(self):
        self.links = {
            1: Baxter_Link(1,
                           [0.0470910226, 0.035959884, 0.0376697645, -0.0061487003, -0.0007808689, 0.0001278755],
                           [-0.05117, 0.07908, 0.00086],
                           [0.2703, 0.069, -1*PI/2.0, 5.70044]
            ),
            2: Baxter_Link(2,
                           [0.027885975, 0.020787492, 0.0117520941, -0.0001882199, 0.0020767576, -0.00030096397],
                           [0.00269, -0.00529, 0.06845],
                           [0, 0, PI/2.0, 3.22698]
            ),
            3: Baxter_Link(3,
                           [0.0266173355, 0.012480083, 0.0284435520, -0.0039218988, -0.001083893, 0.0002927063],
                           [-0.07176, 0.08149, 0.00132],
                           [0.3644, 0.069, -PI/2, 4.31272]
            ),
            4: Baxter_Link(4,
                           [0.0131822787, 0.009268520, 0.0071158268, -0.0001966341, 0.000745949, 0.0003603617],
                           [0.00159, -0.01117, 0.02618],
                           [0, 0, PI/2, 2.07206]
            ),
            5: Baxter_Link(5,
                           [0.0166774282, 0.003746311, 0.0167545726, -0.0001865762, 0.0006473235, 0.0001840370],
                           [-0.01168, 0.13111, 0.0046],
                           [0.3743, 0.01, -PI/2, 2.24665]
            ),
            6: Baxter_Link(6,
                           [0.0070053791, 0.005527552, 0.0038760715, 0.0001534806, -0.0002111503, -0.0004438478],
                           [0.00697, 0.006, 0.06048],
                           [0, 0, PI/2, 1.60979]
            ),
            7: Baxter_Link(7,
                           [0.0008162135, 0.0008735012, 0.0005494148, 0.000128440, 0.0001057726, 0.00018969891],
                           [0.005137, 0.0009572, -0.06682],
                           [0.2295, 0, 0, 0.54218]
            )
        }
        self.n = 7


"""

def main():
    b = Baxter_Link(0,0,[10,3,6],[0,0,0,0])
    print b.get_T_Matrix(0)
    print b.com
"""

if __name__ == "__main__" :
    main()
