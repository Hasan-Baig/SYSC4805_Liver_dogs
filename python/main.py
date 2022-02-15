import sim
import connect
import move
import plow
from time import sleep

WAIT_TIME = 5

if __name__ == "__main__":

    clientID = connect.connectToCoppelia()

    motor_control = move.Move(clientID)
    plow = plow.Plow(clientID)

    plow.closePlow()
    motor_control.stop()

    # motor_control.moveStraight()
    # motor_control.turnLeft()
    # motor_control.turnRight()
    motor_control.rotateLeft()
    motor_control.rotateRight()

    plow.openPlow()
    sleep(WAIT_TIME)
    plow.closePlow()

    sim.simxFinish(-1)

    # Before closing the connection to CoppeliaSim, make sure that the last command sent out had time to arrive. You can guarantee this with (for example):
    sim.simxGetPingTime(clientID)

    # Now close the connection to CoppeliaSim:
    sim.simxFinish(clientID)
