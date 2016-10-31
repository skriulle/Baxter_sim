#-*- coding:utf-8 -*-

import numpy as np
from numpy import cos, sin
from baxter_link import Baxter_Link, Baxter_Test
import function01 as f01

PI = np.pi
g = np.array([0, 0, 9.81, 0])
FREQUENCY = 50.0 #Hz


class Baxter_Simulation():
    def __init__(self):
        self.baxter_test = Baxter_Test()
        self.links = self.baxter_test.links
    
    def sim(self):
        p, dp, ddp = f01.function1()
            
    def T(self, start, end):
        T = np.matrix(np.identity(4))
        while True:
            if start == end:
                break
            elif start < end:
                T = self.links[end].get_T_Matrix() * T
                end -= 1
            else:#inverse matrix needs to be implemented
                break
        return T

    def U(self, i, j, k=None):
        U = np.matrix(np.identity(4))
        if k is not None:
            if i < j or i < k:
                pass
            else:
                if k > j:
                    o = k; k = j; j = o
                _ = self.T(0, k-1)*self.links[k].Q()
                _ = _*self.T(k-1, j-1)
                _ = _*self.links[j].Q()
                _ = _*self.T(j-1, i)
                U = self.T(0, k-1) * self.links[k].Q() * self.T(k-1, j-1) * self.links[j].Q() * self.T(j-1, i)  
        else:
            if j > i:
                U = np.zeros((4, 4))
            else:
                U = self.T(0, j-1) * self.links[j].Q() * self.T(j-1, i)

        return U

    def dL_dq(self, i):
        dL_dq = 0
        for j in range(i, self.baxter_test.n+1):
            m = self.links[j].m
            r = self.links[j].com
            U = self.U(j, i)
            dL_dq += m*g * U * r
            
        return dL_dq


    def main(self):
        self.sim()
        for i in range(1, 8):
            print self.dL_dq(i)
        

if __name__ == "__main__":
    bs = Baxter_Simulation()
    bs.main()
