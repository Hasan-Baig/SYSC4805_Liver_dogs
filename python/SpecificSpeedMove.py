import sim

class simpleMove():
    def __init__(self,clientID):
        res,self.leftMotorFront = sim.simxGetObjectHandle(clientID,'LeftMotorFront',sim.simx_opmode_blocking)
        res,self.rightMotorFront = sim.simxGetObjectHandle(clientID,'RightMotorFront',sim.simx_opmode_blocking)
        res,self.leftMotorBack = sim.simxGetObjectHandle(clientID,'LeftMotorBack',sim.simx_opmode_blocking)
        res,self.rightMotorBack = sim.simxGetObjectHandle(clientID,'RightMotorBack',sim.simx_opmode_blocking)

    def moveStraight(self):

        sim.simxSetJointTargetVelocity(self.clientID,self.leftMotorFront,26.66 * 0.075,sim.simx_opmode_blocking)
        sim.simxSetJointTargetVelocity(self.clientID,self.rightMotorFront,26.66 * 0.075,sim.simx_opmode_blocking)
        sim.simxSetJointTargetVelocity(self.clientID,self.leftMotorBack,26.66 * 0.075,sim.simx_opmode_blocking)
        sim.simxSetJointTargetVelocity(self.clientID,self.rightMotorBack,26.66 * 0.075,sim.simx_opmode_blocking)