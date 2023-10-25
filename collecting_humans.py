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
from app import music
from app import display

async def main():
    motor_pair.pair(motor_pair.PAIR_1, port.A, port.E)
    # write your code here
    await motor.run_for_degrees(port.D, 150, (580))
    await motor_pair.move_for_degrees(motor_pair.PAIR_1, (250), 0, velocity=700)
    await motor.run_for_degrees(port.E,55, (150))
    await motor_pair.move_for_degrees(motor_pair.PAIR_1, (250), 0, velocity=700)
    await motor.run_for_degrees(port.D, 150, (-580))
    await motor_pair.move_for_degrees(motor_pair.PAIR_1, (-250), 0, velocity=700) #back
    await motor.run_for_degrees(port.A,-105, (150))
    await motor_pair.move_for_degrees(motor_pair.PAIR_1, (-320), 0, velocity=700)
    await motor.run_for_degrees(port.D, 150, (580))
    await motor_pair.move_for_degrees(motor_pair.PAIR_1, (-100), 0, velocity=700)
    await motor.run_for_degrees(port.E,150, (150))
    await motor.run_for_degrees(port.D, 150, (-580))
    await motor_pair.move_for_degrees(motor_pair.PAIR_1, (700), 0, velocity=700)
    await motor.run_for_degrees(port.D, 150, (580))
    await motor.run_for_degrees(port.E,150, (150))
    await motor_pair.move_for_degrees(motor_pair.PAIR_1, (120), 0, velocity=700)
    await motor.run_for_degrees(port.D, 150, (-580))
    await motor_pair.move_for_degrees(motor_pair.PAIR_1, (-110), 0, velocity=700)
    await motor.run_for_degrees(port.A,-150, (150))
    await motor_pair.move_for_degrees(motor_pair.PAIR_1, (-810), 0, velocity=700)
    await runloop.sleep_ms(5000)
    await motor_pair.move_for_degrees(motor_pair.PAIR_1, (800), 0, velocity=700)
    await motor.run_for_degrees(port.A,-100, (150))
    await motor_pair.move_for_degrees(motor_pair.PAIR_1, (100), 0, velocity=700)
    await motor.run_for_degrees(port.D, 150, (580))
    await motor_pair.move_for_degrees(motor_pair.PAIR_1, (-100), 0, velocity=700)
    await motor.run_for_degrees(port.A,100, (150))
    await motor_pair.move_for_degrees(motor_pair.PAIR_1, (-850), 0, velocity=700)
    await motor.run_for_degrees(port.D, 150, (-580))


runloop.run(main())
