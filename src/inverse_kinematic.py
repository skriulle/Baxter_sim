#-*- coding:utf-8 -*-

import numpy as np
from numpy import cos, sin
from baxter_link import Baxter_Link, Baxter_Test
import csv

PI = np.pi
FREQUENCY = 50.0 #Hz


class Inverse_Kinematic:
    def __init__(self, links, initial_angles ,valids=[False, True, False, True, False, False, False]):
        self.original_links = links         #dictionary
        self.initial_angles = initial_angles
        self.valids = valids
        self.links = None                   #array
        self.valid_links()

    def write_position_file(self, positions):
        filename = "result/" + filename + "xyz" + "01" + ".dat"
        f = open(filename, 'w')
        for t, p in enumerate(positions):
            x, y, z = p
            v = [t/FREQUENCY, x, y, z]
            f.write(str(v[0]) + " " + str(v[1]) + " " +  str(v[2]) + " " + str(v[3]) + "\n")
        f.close()

        
    def valid_links(self):
        self.links = []
        elements = zip(self.initial_angles, self.valids)
    
        matrix = np.matrix([[1,0,0,0],[0,1,0,0],[0,0,1,0],[0,0,0,1]])
        for j, av in enumerate(elements):
            a, v = av
            i = 7-j
            l = self.original_links[i]
            if v:
                matrix = matrix * l.get_T_Matrix(a)
            else:
                matrix = matrix * l.get_T_Matrix(0)
                self.links.append(matrix)

                matrix = np.matrix([[1,0,0,0],[0,1,0,0],[0,0,1,0],[0,0,0,1]]) #reset

        self.links.append(matrix)


        
    def make_angle(self, positions):
        angles = []
        x1, z1 = 0.069, 0.2703
        x2, z2 = 0.138-x1, 0.6347-z1
        x3, z3 = 0.148-(x1+x2), 1.2385-(z1+z2)
        
        #l1 = np.sqrt(x1**2 + z1**2)
        #a1 = np.arctan2(z1, x1)
        l2 = np.sqrt(x2**2 + z2**2)
        a2 = np.arctan2(z2, x2)
        l3 = np.sqrt(x3**2 + z3**2)
        a3 = np.arctan2(z3, x3)
        print "link ", map(str, [l2, l3])
        print "angle", map(str, [a2, a3])
        
        theta1_init, theta2_init = a2, a3-a2
        
        for p in positions:
            x, y, z = p

            k1 = x-x1
            k2 = z-z1

            try:
                ee = ((k1**2+k2**2)-(l2**2+l3**2)) / (2*l2*l3)
                theta2 = np.arccos(ee)
            except Warning:
                print  ((k1**2+k2**2)-(l2**2+l3**2)) / (2*l2*l3)
            
            k3 = l2 + l3*cos(theta2)
            k4 = l3*sin(theta2)
        
            #theta1 = -np.arccos((k1*k3 + k2*k4) / (k1**2 + k2**2))
            theta1 = -np.arcsin((k1*k4 - k2*k3) / (k1**2 + k2**2))

            angles.append([0,theta1_init-theta1,0,theta2_init-theta2,0,0,0])
            #angles.append([0,0,0,0,0,0,0])
            #angles.append([theta1_init-theta1, theta2_init-theta2])
        #print angles
        #return [[theta1_init, theta2_init]]
        return angles


    
