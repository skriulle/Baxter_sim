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
        pass


    def function01(self, sim_time = 10):
        positions = []
        for t in range(int(sim_time*FREQUENCY)+2):
            x = 20
            y = 0
            z = sin(2*PI*t/FREQUENCY/2.0)+10 #T = 2s
        return positions

    
