#-*- coding:utf-8 -*-

import numpy as np
from numpy import cos, sin

PI = np.pi
g = 9.81
FREQUENCY = 50.0


def ex01(sim_time = 10):
    name = "ex01/plot"
    positions = []
    for t in range(int(sim_time*FREQUENCY)+2):
        x = 0.62
        y = 0
        z = 0.15*sin(2*PI*t/FREQUENCY/6.0)+0.35 #T = 6s
        positions.append([x,y,z])

    return positions, name


def ex02(sim_time = 10):
    name = "ex02/plot"
    positions = []
    for t in range(int(sim_time*FREQUENCY)+2):
        x = 0.62
        y = 0
        z = 0.15*sin(2*PI*t/FREQUENCY/2.0)+0.35 #T = 2s
        positions.append([x,y,z])

    return positions, name


def ex03(sim_time = 10):
    name = "ex03/plot"
    positions = []
    for t in range(int(sim_time*FREQUENCY)+2):
        x = 0.2*sin(2*PI*t/FREQUENCY/6.0)+0.42
        y = 0
        z = 0.55
        positions.append([x,y,z])

    return positions, name


def ex04(sim_time = 10):
    name = "ex04/plot"
    positions = []
    for t in range(int(sim_time*FREQUENCY)+2):
        x = 0.15*sin(2*PI*t/FREQUENCY/6.0)+0.62
        y = 0
        z = 0.15*sin(2*PI*t/FREQUENCY/2.0)+0.55
        positions.append([x,y,z])

    return positions, name



def ex05(sim_time = 10):
    name = "ex05/plot"
    positions = []
    for t in range(int(sim_time*FREQUENCY)+2):
        x = 0.15*sin(2*PI*t/FREQUENCY/6.0)+0.62
        y = 0
        z = 0.15*sin(2*PI*t/FREQUENCY/6.0)+0.55
        positions.append([x,y,z])

    return positions, name



def ex05(sim_time = 10):
    name = "ex05/plot"
    positions = []
    for t in range(int(sim_time*FREQUENCY)+2):
        x = 0.15*sin(2*PI*t/FREQUENCY/6.0)+0.62
        y = 0
        z = 0.15*sin(2*PI*t/FREQUENCY/6.0)+0.55
        positions.append([x,y,z])

    return positions, name



def ex06(sim_time = 10):
    name = "ex06/plot"
    positions = []
    for t in range(int(sim_time*FREQUENCY)+2):
        x = 0.05*sin(2*PI*t/FREQUENCY/6.0)+0.62
        y = 0
        z = 0.15*sin(2*PI*t/FREQUENCY/6.0)+0.4
        positions.append([x,y,z])

    return positions, name


def ex07(sim_time = 10):
    name = "ex07/plot"
    positions = []
    for t in range(int(sim_time*FREQUENCY)+2):
        x = -0.025*sin(2*PI*t/FREQUENCY/6.0)+0.025*sin(2*PI*t/FREQUENCY/12.0) + 0.62
        y = 0
        z = 0.15*sin(2*PI*t/FREQUENCY/6.0)+0.35
        positions.append([x,y,z])

    return positions, name


def ex08(sim_time = 10):
    name = "ex08/plot"
    positions = []
    for t in range(int(sim_time*FREQUENCY)+2):
        x = 0.15*sin(2*PI*t/FREQUENCY/6.0)+1.0
        y = 0
        z = 0.15*sin(2*PI*t/FREQUENCY/2.0)+0.6
        positions.append([x,y,z])

    return positions, name

