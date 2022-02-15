import sim
import time

def moveStraight(clientID):
    
    res,leftMotorFront = sim.simxGetObjectHandle(clientID,'LeftMotorFront',sim.simx_opmode_blocking)
    res,rightMotorFront = sim.simxGetObjectHandle(clientID,'RightMotorFront',sim.simx_opmode_blocking)
    res,leftMotorBack = sim.simxGetObjectHandle(clientID,'LeftMotorBack',sim.simx_opmode_blocking)
    res,rightMotorBack = sim.simxGetObjectHandle(clientID,'RightMotorBack',sim.simx_opmode_blocking)

    sim.simxSetJointTargetVelocity(clientID,leftMotorFront,0.2,sim.simx_opmode_blocking)
    sim.simxSetJointTargetVelocity(clientID,rightMotorFront,0.2,sim.simx_opmode_blocking)
    sim.simxSetJointTargetVelocity(clientID,leftMotorBack,0.2,sim.simx_opmode_blocking)
    sim.simxSetJointTargetVelocity(clientID,rightMotorBack,0.2,sim.simx_opmode_blocking)
    time.sleep(10)
    sim.simxSetJointTargetVelocity(clientID,leftMotorFront,0,sim.simx_opmode_blocking)
    sim.simxSetJointTargetVelocity(clientID,rightMotorFront,0,sim.simx_opmode_blocking)
    sim.simxSetJointTargetVelocity(clientID,leftMotorBack,0,sim.simx_opmode_blocking)
    sim.simxSetJointTargetVelocity(clientID,rightMotorBack,0,sim.simx_opmode_blocking)