#-*- coding:utf-8 -*-

"""
This is a first experiment of baxter project.
We give the movement of joints and get torques of each joint.
"""

import numpy as np
from numpy import cos, sin
import baxter_link
from baxter_link import Baxter_Test

PI = np.pi
g = 9.81
FREQUENCY = 50.0 #Hz

