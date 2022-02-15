import sim
import time

class Plow():
    def __init__(self,clientID):
        self.clientID = clientID
        res,self.leftPlowJoint = sim.simxGetObjectHandle(clientID,'LeftPlowJoint',sim.simx_opmode_blocking)
        res,self.rightPlowJoint = sim.simxGetObjectHandle(clientID,'RightPlowJoint',sim.simx_opmode_blocking)

    def openPlow(self):
        sim.simxSetJointTargetVelocity(self.clientID,self.leftPlowJoint,0.2,sim.simx_opmode_blocking)
        sim.simxSetJointTargetVelocity(self.clientID,self.rightPlowJoint,0.2,sim.simx_opmode_blocking)
        time.sleep(1)
        sim.simxSetJointTargetVelocity(self.clientID,self.leftPlowJoint,0,sim.simx_opmode_blocking)
        sim.simxSetJointTargetVelocity(self.clientID,self.rightPlowJoint,0,sim.simx_opmode_blocking)
    
    def closePlow(self):
        sim.simxSetJointTargetVelocity(self.clientID,self.leftPlowJoint,-0.2,sim.simx_opmode_blocking)
        sim.simxSetJointTargetVelocity(self.clientID,self.rightPlowJoint,-0.2,sim.simx_opmode_blocking)
        time.sleep(1)
        sim.simxSetJointTargetVelocity(self.clientID,self.leftPlowJoint,0,sim.simx_opmode_blocking)
        sim.simxSetJointTargetVelocity(self.clientID,self.rightPlowJoint,0,sim.simx_opmode_blocking)