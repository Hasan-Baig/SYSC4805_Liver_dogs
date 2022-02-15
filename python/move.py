try:
    import sim
except:
    print ('--------------------------------------------------------------')
    print ('"sim.py" could not be imported. This means very probably that')
    print ('either "sim.py" or the remoteApi library could not be found.')
    print ('Make sure both are in the same folder as this file,')
    print ('or appropriately adjust the file "sim.py"')
    print ('--------------------------------------------------------------')
    print ('')

import time

print ('Program started')
sim.simxFinish(-1) # just in case, close all opened connections
clientID=sim.simxStart('127.0.0.1',19999,True,True,5000,5) # Connect to CoppeliaSim
if clientID!=-1:
    print ('Connected to remote API server')

    res,left_motor = sim.simxGetObjectHandle(clientID,'Left_Motor',sim.simx_opmode_blocking)
    res,right_motor = sim.simxGetObjectHandle(clientID,'Right_Motor',sim.simx_opmode_blocking)

    sim.simxSetJointTargetVelocity(clientID,left_motor,0.2,sim.simx_opmode_blocking)
    sim.simxSetJointTargetVelocity(clientID,right_motor,0.2,sim.simx_opmode_blocking)
    time.sleep(10)
    sim.simxSetJointTargetVelocity(clientID,left_motor,0,sim.simx_opmode_blocking)
    sim.simxSetJointTargetVelocity(clientID,right_motor,0.2,sim.simx_opmode_blocking)

   
    sim.simxFinish(-1)

    # Before closing the connection to CoppeliaSim, make sure that the last command sent out had time to arrive. You can guarantee this with (for example):
    sim.simxGetPingTime(clientID)

    # Now close the connection to CoppeliaSim:
    sim.simxFinish(clientID)
else:
    print ('Failed connecting to remote API server')
    print ('Program ended')
