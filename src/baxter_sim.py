#-*- coding:utf-8 -*-

import numpy as np
from numpy import cos, sin
from baxter_link import Baxter_Test
import function01 as f01

PI = np.pi
g = 9.81
FREQUENCY = 50.0 #Hz


class Baxter_Simulation():
    def __init__(self):
        self.baxter_test = Baxter_Test()
        self.links = self.baxter_test.links
    
    def sim(self):
        p, dp, ddp = f01.function1()
            
    def T(self, start, end):
        
        T = np.matrix([[1, 0, 0, 0], [0, 1, 0, 0], [0, 0, 1, 0], [0, 0, 0, 1]])
        while True:
            if start == end:
                break
            elif start < end:
                T = self.links[end].get_T_Matrix() * T
                end -= 1
            else:#inverse matrix needs to be implemented
                break
        return T
    

    def main(self):
        self.sim()
        print self.T(0, 5)
        

if __name__ == "__main__":
    bs = Baxter_Simulation()
    bs.main()
