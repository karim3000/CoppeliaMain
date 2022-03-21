# -*- coding: utf-8 -*-
"""
Created on Sun Mar 20 20:47:11 2022

@author: Karim
"""

import sim
import time
import sys
import math

vel=90  
accel=40
jerk=80
x = 0
jointHandles = []
currentConf = []
path = '/Franka/joint'
data = (0, 0)

#sim.simxFinish(-1) # just in case, close all opened connections
clientID=sim.simxStart('127.0.0.1',19999,True,True,5000,5) # Connect to CoppeliaSim

if clientID!=-1:
    print ('Connected to remote API server')
    for x in range(7):
        if x > 0:
            path = path + '/link' + str(x+1) + '_resp' + '/joint' 
            print(path)
        data = sim.simxGetObjectHandle(clientID, path, sim.simx_opmode_oneshot)
        jointHandles.append(data)
        print(sim.simxGetObjectHandle(clientID, path, sim.simx_opmode_oneshot))
    
    maxVel={vel*math.pi/180,vel*math.pi/180,vel*math.pi/180,vel*math.pi/180,vel*math.pi/180,vel*math.pi/180,vel*math.pi/180}
    maxAccel={accel*math.pi/180,accel*math.pi/180,accel*math.pi/180,accel*math.pi/180,accel*math.pi/180,accel*math.pi/180,accel*math.pi/180}
    maxJerk={jerk*math.pi/180,jerk*math.pi/180,jerk*math.pi/180,jerk*math.pi/180,jerk*math.pi/180,jerk*math.pi/180,jerk*math.pi/180}
    targetPos1={90*math.pi/180,90*math.pi/180,135*math.pi/180,-45*math.pi/180,90*math.pi/180,180*math.pi/180,0}
     
    # for x in range(7):
    #     currentConf[x]=sim.simxGetJointPosition(clientID, jointHandles[x], sim.simx_opmode_oneshot)
    #     print(currentConf[x])
else:
    print ('Failed connecting to remote API server')
    print ('Program ended')
    sys.exit

