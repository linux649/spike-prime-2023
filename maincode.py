# from spike import PrimeHub, Lightmatrix, Button, statusLight, ForceSensor, notionsensor, Speaker, ColorSensor, App, DistanceSensor, Motor, MotorPair
# from spike.contral import waith_for_seconds, wait_until, Tier

from hub import light_matrix
from hub import light
import runloop
import time
import motor
import motor_pair
from hub import port
import random
import force_sensor
from hub import sound
import color
import color_sensor
import distance_sensor
async def trying():
    motor_pair.pair(motor_pair.PAIR_1, port.A, port.E)
    # await motor.run_for_degrees(port.C, 150, (540))
    await motor.run_for_degrees(port.D, 150, (580))
    await motor.run_for_degrees(port.E, 90, (150))
    await motor_pair.move_for_degrees(motor_pair.PAIR_1, (50), 0)
    await motor.run_for_degrees(port.A,  -90, (150))
    await motor_pair.move_for_degrees(motor_pair.PAIR_1, (280), 0)
    await motor.run_for_degrees(port.D, 150, (-220))
    await motor_pair.move_for_degrees(motor_pair.PAIR_1, (-400), 0)
    await motor.run_for_degrees(port.A,-140, (350))
    await motor_pair.move_for_degrees(motor_pair.PAIR_1, (500), 0)
    await motor.run_for_degrees(port.E, 90, (150))
    await motor_pair.move_for_degrees(motor_pair.PAIR_1, (500), 0)
robot = PenguinBot()
# runloop.run(robot.main())
runloop.run(trying())
