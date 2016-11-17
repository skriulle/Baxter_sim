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


        
    def make_angle(self):
        angles = []
        positions, variable = self.function01()
        x1, z1 = 0.069, 0.2703
        x2, z2 = 0.138-x1, 0.6347-z1
        x3, z3 = 0.14800000000000002-(x1+x2), 1.009-(z1+z2)
        
        #l1 = np.sqrt(x1**2 + z1**2)
        #a1 = np.arctan2(z1, x1)
        l2 = 0.439875127233 - 0.069#np.sqrt(x2**2 + z2**2)
        a2 = np.arctan2(z2, x2)
        l3 = 0.814308686092 - 0.439875127233 #np.sqrt(x3**2 + z3**2)
        a3 = np.arctan2(z3, x3)
        print "link ", map(str, [l2, l3])
        print "angle", map(str, [a2, a3])
        
        theta1_init, theta2_init = a2, a3-a2
        
        for p in positions:
            x, y, z = p

            k1 = x-x1
            k2 = z-z1
            
            theta2 = np.arccos( ((k1**2+k2**2)-(l2**2+l3**2)) / (2*l2*l3))
            
            k3 = l2 + l3*cos(theta2)
            k4 = l3*sin(theta2)
            
            #theta1 = np.arctan2(k2-l2*sin(theta2) , k1-l2*cos(theta2))
            #theta1 = -np.arccos((k1*k3 + k2*k4) / (k1**2 + k2**2))
            theta1 = -np.arcsin((k1*k4 - k2*k3) / (k1**2 + k2**2))
            #print theta1, theta2

            #theta1, theta2 = PI/2, PI/4
            angles.append([theta1_init-theta1, theta2_init-theta2])

        #print angles
        #return [[theta1_init, theta2_init]]
        return angles

    def function01(self, sim_time = 10):
        positions = []
        for t in range(int(sim_time*FREQUENCY)+2):
            x = 0.42
            y = 0
            z = 0.15*sin(2*PI*t/FREQUENCY/2.0)+0.55 #T = 2s
            positions.append([x,y,z])
        return positions, 2 #2 means z is a variable, the others are constants

    
