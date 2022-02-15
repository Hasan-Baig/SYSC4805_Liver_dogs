import sim
from time import sleep

WAIT_TIME = 5

class Move():
    def __init__(self,clientID):
        self.clientID = clientID
        res,self.leftMotorFront = sim.simxGetObjectHandle(clientID,'LeftMotorFront',sim.simx_opmode_blocking)
        res,self.rightMotorFront = sim.simxGetObjectHandle(clientID,'RightMotorFront',sim.simx_opmode_blocking)
        res,self.leftMotorBack = sim.simxGetObjectHandle(clientID,'LeftMotorBack',sim.simx_opmode_blocking)
        res,self.rightMotorBack = sim.simxGetObjectHandle(clientID,'RightMotorBack',sim.simx_opmode_blocking)

    def stop(self):
        sim.simxSetJointTargetVelocity(self.clientID,self.leftMotorFront,0,sim.simx_opmode_blocking)
        sim.simxSetJointTargetVelocity(self.clientID,self.rightMotorFront,0,sim.simx_opmode_blocking)
        sim.simxSetJointTargetVelocity(self.clientID,self.leftMotorBack,0,sim.simx_opmode_blocking)
        sim.simxSetJointTargetVelocity(self.clientID,self.rightMotorBack,0,sim.simx_opmode_blocking)


    def moveStraight(self):
        
        sim.simxSetJointTargetVelocity(self.clientID,self.leftMotorFront,0.2,sim.simx_opmode_blocking)
        sim.simxSetJointTargetVelocity(self.clientID,self.rightMotorFront,0.2,sim.simx_opmode_blocking)
        sim.simxSetJointTargetVelocity(self.clientID,self.leftMotorBack,0.2,sim.simx_opmode_blocking)
        sim.simxSetJointTargetVelocity(self.clientID,self.rightMotorBack,0.2,sim.simx_opmode_blocking)
        sleep(WAIT_TIME)
        self.stop()

    def turnLeft(self):
        
        sim.simxSetJointTargetVelocity(self.clientID,self.leftMotorFront,0.2,sim.simx_opmode_blocking)
        sim.simxSetJointTargetVelocity(self.clientID,self.rightMotorFront,0.1,sim.simx_opmode_blocking)
        sim.simxSetJointTargetVelocity(self.clientID,self.leftMotorBack,0.2,sim.simx_opmode_blocking)
        sim.simxSetJointTargetVelocity(self.clientID,self.rightMotorBack,0.1,sim.simx_opmode_blocking)
        sleep(WAIT_TIME)
        self.stop()

    def turnRight(self):

        sim.simxSetJointTargetVelocity(self.clientID,self.leftMotorFront,0.1,sim.simx_opmode_blocking)
        sim.simxSetJointTargetVelocity(self.clientID,self.rightMotorFront,0.2,sim.simx_opmode_blocking)
        sim.simxSetJointTargetVelocity(self.clientID,self.leftMotorBack,0.1,sim.simx_opmode_blocking)
        sim.simxSetJointTargetVelocity(self.clientID,self.rightMotorBack,0.2,sim.simx_opmode_blocking)
        sleep(WAIT_TIME)
        self.stop()

    def rotateLeft(self):
        
        sim.simxSetJointTargetVelocity(self.clientID,self.leftMotorFront,0.2,sim.simx_opmode_blocking)
        sim.simxSetJointTargetVelocity(self.clientID,self.rightMotorFront,-0.2,sim.simx_opmode_blocking)
        sim.simxSetJointTargetVelocity(self.clientID,self.leftMotorBack,0.2,sim.simx_opmode_blocking)
        sim.simxSetJointTargetVelocity(self.clientID,self.rightMotorBack,-0.2,sim.simx_opmode_blocking)
        sleep(WAIT_TIME)
        self.stop()

    def rotateRight(self):
        
        sim.simxSetJointTargetVelocity(self.clientID,self.leftMotorFront,-0.2,sim.simx_opmode_blocking)
        sim.simxSetJointTargetVelocity(self.clientID,self.rightMotorFront,0.2,sim.simx_opmode_blocking)
        sim.simxSetJointTargetVelocity(self.clientID,self.leftMotorBack,-0.2,sim.simx_opmode_blocking)
        sim.simxSetJointTargetVelocity(self.clientID,self.rightMotorBack,0.2,sim.simx_opmode_blocking)
        sleep(WAIT_TIME)
        self.stop()
