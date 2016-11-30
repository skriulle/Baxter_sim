#-*- coding:utf-8 -*-

import numpy as np
from numpy import cos, sin
from baxter_link import Baxter_Link, Baxter_Test
from inverse_kinematic import Inverse_Kinematic
from experiment import *
import function01 as f01
import csv

PI = np.pi
g = np.array([0, 0, 9.81, 0])
FREQUENCY = 50.0 #Hz
sim_time = 40.0 #s


class Baxter_Simulation():
    def __init__(self):
        self.baxter_test = Baxter_Test()
        self.links = self.baxter_test.links
        self.n = self.baxter_test.n
        self.inverse_kinematic = Inverse_Kinematic(self.links, [0,0,0,0,0,0,0])
        self.filename = ""
    
    def get_function(self):
        q, dq, ddq = f01.function2(10)
        return q, dq, ddq
            
    def T(self, start, end, q):
        T = np.matrix(np.identity(4))
        while True:
            if start == end:
                break
            elif start < end:
                theta = q[end-1]
                T = self.links[end].get_T_Matrix(theta) * T
                
                end -= 1
            else: #inverse matrix needs to be implemented
                break
        return T

    def U(self, q, i, j, k=None):
        U = np.matrix(np.identity(4))
        if k is not None:
            if i < j or i < k:
                pass
            else:
                if k > j:
                    o = k; k = j; j = o
                U = self.T(0, k-1, q) * self.links[k].Q() * self.T(k-1, j-1, q) * self.links[j].Q() * self.T(j-1, i, q)  
        else:
            if j > i:
                U = np.zeros((4, 4))
            else:
                U = self.T(0, j-1, q) * self.links[j].Q() * self.T(j-1, i, q)

        return U

    def dK(self, i, q, dq, ddq):
        dK = 0
        for j in range(i, self.n+1):
            Jj = self.links[j].J()
            for k in range(1, j+1):
                Ujk = self.U(q, j,k)
                M = Ujk * Jj * Ujk.T
                dK += M.trace() * ddq[k-1]

                Uji = self.U(q, j,i)
                dqk = dq[k-1]
                for m in range(1, j+1):
                    Ujkm = self.U(q, j,k,m)
                    dqm = dq[m-1]
                    M = Ujkm * Jj * Uji.T
                    dK += M.trace() * dqk * dqm
                    
        return dK

    def dL_dq(self, i, q):
        dL_dq = 0
        for j in range(i, self.baxter_test.n+1):
            m = self.links[j].m
            r = self.links[j].com
            U = self.U(q, j, i)
            dL_dq += m*g * U * r
            
        return float(dL_dq)

    def get_torque(self, i, q, dq, ddq):
        dK = self.dK(i, q, dq, ddq)
        dL_dq = self.dL_dq(i, q)
        t = dK-dL_dq
        return float(t)

    def sim(self, q_v, dq_v, ddq_v):
        t_vector = []
        for i in range(1, self.n+1):
            ti_vector = []
            filename = "result/" + self.filename + "0" + str(i) + ".dat"
            f = open(filename, 'w')
            for t,(q, dq, ddq) in enumerate(zip(q_v, dq_v, ddq_v)):
                v = [t/FREQUENCY, self.get_torque(i, q, dq, ddq)]
                ti_vector.append([t/FREQUENCY, self.get_torque(i, q, dq, ddq)])
                f.write(str(v[0]) + " " + str(v[1]) + "\n")
      
            f.close()
            print i, ti_vector
            t_vector.append(ti_vector)


    def visualize(self, xyz):
        xp, yp, zp = xyz

        from mpl_toolkits.mplot3d import Axes3D
        import matplotlib.pyplot as plt

        
        fig = plt.figure()
        ax = fig.gca(projection='3d')
        ax.set_xlim3d(0, 1)
        ax.set_ylim3d(-0.5, 0.5)
        ax.set_zlim3d(0, 1)

        line, = ax.plot(xp, yp, zs=np.array(zp), zdir='z')
        plt.show()

    def main(self):

        positions, self.filename = ex04(sim_time)
        angles = self.inverse_kinematic.make_angle(positions)
        q, dq, ddq = f01.angle2acceleration(angles, sim_time)
        self.sim(q, dq, ddq)

        '''
        xp = []
        yp = []
        zp = []
        for angle in angles:
            for i in range(8):

                """
                theta1 = 1
                theta2 = PI-1
                """
                _, theta1, _2, theta2, _3, _4, _5 = angle
                T = self.T(0, i, [0,theta1,0,theta2,0,0,0])[:,3].T
                T = np.array(T).reshape(-1,).tolist()
                #print T[0:3]
                x, y, z = T[0:3]
                xp.append(x)
                yp.append(y)
                #zp.append(0)
                zp.append(z)
                print x, z

        self.visualize([xp, yp, zp])
        '''

        
if __name__ == "__main__":
    bs = Baxter_Simulation()
    bs.main()
