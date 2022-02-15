import sim
import connect
import simpleMove



if __name__ == "__main__":

    clientID = connect.connectToCoppelia()
    simpleMove.moveStraight(clientID)
    sim.simxFinish(-1)

    # Before closing the connection to CoppeliaSim, make sure that the last command sent out had time to arrive. You can guarantee this with (for example):
    sim.simxGetPingTime(clientID)

    # Now close the connection to CoppeliaSim:
    sim.simxFinish(clientID)
