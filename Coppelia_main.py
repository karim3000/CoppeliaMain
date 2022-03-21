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
currentConf = [0, 0, 0, 0, 0, 0, 0]
path = '/Franka/joint'
data = (0, 0)

sim.simxFinish(-1) # just in case, close all opened connections
clientID=sim.simxStart('127.0.0.1',19999,True,True,5000,5) # Connect to CoppeliaSim

if clientID!=-1:
    print ('Connected to remote API server')
    # for x in range(7):
    #     if x > 0:
    #         path = path + '/link' + str(x+1) + '_resp' + '/joint' 
    #         # print(path)
    #     data = sim.simxGetObjectHandle(clientID, path, sim.simx_opmode_oneshot)
    #     jointHandles.append(data[0])
    #     print(data)
    
    jointHandles = [16, 19, 22, 24, 26, 28, 30]
    
    while 1+1 == 2:
        # maxVel={vel*math.pi/180,vel*math.pi/180,vel*math.pi/180,vel*math.pi/180,vel*math.pi/180,vel*math.pi/180,vel*math.pi/180}
        # maxAccel={accel*math.pi/180,accel*math.pi/180,accel*math.pi/180,accel*math.pi/180,accel*math.pi/180,accel*math.pi/180,accel*math.pi/180}
        # maxJerk={jerk*math.pi/180,jerk*math.pi/180,jerk*math.pi/180,jerk*math.pi/180,jerk*math.pi/180,jerk*math.pi/180,jerk*math.pi/180}
        # targetPos1={90*math.pi/180,90*math.pi/180,135*math.pi/180,-45*math.pi/180,90*math.pi/180,180*math.pi/180,0}
         
        for x in range(6):
            currentConf[x] = sim.simxGetJointPosition(clientID, jointHandles[x], sim.simx_opmode_oneshot)
        print(currentConf)
        sim.simxSetJointTargetPosition(clientID, 28, 2.8, sim.simx_opmode_oneshot)
        sim.simxSetJointTargetPosition(clientID, 26, 1.24, sim.simx_opmode_oneshot)
        sim.simxSetJointTargetPosition(clientID, 24, -1, sim.simx_opmode_oneshot)
        
        
else:
    print ('Failed connecting to remote API server')
    print ('Program ended')
    sys.exit

