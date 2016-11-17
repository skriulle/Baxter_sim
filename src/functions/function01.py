#-*- coding:utf-8 -*-

import numpy as np
from numpy import cos, sin

PI = np.pi
g = 9.81
FREQUENCY = 50.0


def angle2acceleration(angles, sim_time):
    q = angles
    dq = []
    for t in xrange(int(sim_time*FREQUENCY+1)):
        dqt = []
        for i in xrange(7):
            dqt.append((q[t+1][i] - q[t][i]) * FREQUENCY)

        dq.append(dqt)

    ddq = []
    for t in xrange(int(sim_time*FREQUENCY)):
        ddqt = []
        for i in xrange(7):
            ddqt.append((dq[t+1][i] - dq[t][i]) * FREQUENCY)

        ddq.append(ddqt)

    return q, dq, ddq
    

def function1(sim_time = 40.0):
    #T = 3s
    p = []
    dp = []
    ddp = []
    for t in xrange(int(sim_time*FREQUENCY+2)):
        y = sin(2*PI/3.0/FREQUENCY*(t))
        z = np.sqrt(1.0-y**2)
        x = 0.0
        p.append([x, y, z])

        
    for i in range(len(p)-1):
        dx = (p[i+1][0] - p[i][0])*FREQUENCY
        dy = (p[i+1][1] - p[i][1])*FREQUENCY
        dz = (p[i+1][2] - p[i][2])*FREQUENCY
        dp.append([dx, dy, dz])

    for i in range(len(dp)-1):
        ddx = (dp[i+1][0] - dp[i][0])*FREQUENCY
        ddy = (dp[i+1][1] - dp[i][1])*FREQUENCY
        ddz = (dp[i+1][2] - dp[i][2])*FREQUENCY
        ddp.append([ddx, ddy, ddz])
        
    p = p[0:len(ddp)]
    dp = dp[0:len(ddp)]

    ddo = np.matrix(ddp)
    dp = np.matrix(dp)
    p = np.matrix(p)

    return p, dp, ddp


def function2(sim_time = 40.0):
    #theta1 = sin( 2*PI / 3.0 / FREQENCY * t)

    q = []
    for t in xrange(int(sim_time*FREQUENCY+2)):
        qt = []
        qt.append(sin( 2*PI / 3.0 / FREQUENCY * t))
        for i in xrange(6):
            qt.append(0)

        q.append(qt)

    dq = []
    for t in xrange(int(sim_time*FREQUENCY+1)):
        dqt = []
        for i in xrange(7):
            dqt.append((q[t+1][i] - q[t][i]) * FREQUENCY)

        dq.append(dqt)

    ddq = []
    for t in xrange(int(sim_time*FREQUENCY)):
        ddqt = []
        for i in xrange(7):
            ddqt.append((dq[t+1][i] - dq[t][i]) * FREQUENCY)

        ddq.append(ddqt)

    return q, dq, ddq
