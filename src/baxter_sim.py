#-*- coding:utf-8 -*-

import numpy as np
from numpy import cos, sin
from baxter_link import Baxter_Test



PI = np.pi
g = 9.81
FREQUENCY = 50.0 #Hz


def function1(sim_time = 40):
    #T = 3s
    p = []
    dp = []
    ddp = []
    for t in xrange(int(sim_time*FREQUENCY+2)):
        y = sin(2*PI/3.0/FREQUENCY*(t-1))
        z = np.sqrt(1.0-y**2)
        x = 0.0
        p.append([x, y, z])

        
    for i in range(len(p)-2):
        dx = (p[i+2][0] - p[i][0])/2.0*FREQUENCY
        dy = (p[i+2][1] - p[i][1])/2.0*FREQUENCY
        dz = (p[i+2][2] - p[i][2])/2.0*FREQUENCY
        dp.append([dx, dy, dz])
        
    p = p[1:len(p)-1]
    
    dp = np.matrix(dp)
    p = np.matrix(p)

    return p, dp

    

def sim():
    p, dp = function1()

    
    


def main():
    sim()

if __name__ == "__main__":
    main()
