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
    await motor_pair.move_for_degrees(motor_pair.PAIR_1, (-250), 0, velocity=700) 
    await motor.run_for_degrees(port.A,-60, (150))
    await motor_pair.move_for_degrees(motor_pair.PAIR_1, (-320), 0, velocity=700)
    await motor.run_for_degrees(port.D, 150, (580))
    await motor_pair.move_for_degrees(motor_pair.PAIR_1, (-100), 0, velocity=700) #back
    await motor.run_for_degrees(port.E,145, (150))
    await motor.run_for_degrees(port.D, 150, (-580))
    await motor_pair.move_for_degrees(motor_pair.PAIR_1, (860), 0, velocity=700)
    await motor.run_for_degrees(port.D, 150, (580)) #take of
    await motor.run_for_degrees(port.E,150, (150))
    await motor_pair.move_for_degrees(motor_pair.PAIR_1, (150), 0, velocity=700)
    await motor.run_for_degrees(port.D, 150, (-580))
    await motor_pair.move_for_degrees(motor_pair.PAIR_1, (-150), 0, velocity=700)
    await motor.run_for_degrees(port.A,-150, (150))
    await motor_pair.move_for_degrees(motor_pair.PAIR_1, (-960), 0, velocity=700)
    for i in range(1, 11):
        light_matrix.write(str(i))
        await runloop.sleep_ms(1000)
    light_matrix.write("!") 
    await motor_pair.move_for_degrees(motor_pair.PAIR_1, (810), 0, velocity=700)
    await motor.run_for_degrees(port.A,-100, (150))
    await motor_pair.move_for_degrees(motor_pair.PAIR_1, (100), 0, velocity=700)
    await motor.run_for_degrees(port.D, 150, (580))
    await motor_pair.move_for_degrees(motor_pair.PAIR_1, (-100), 0, velocity=700)
    await motor.run_for_degrees(port.A,100, (150))
    await motor_pair.move_for_degrees(motor_pair.PAIR_1, (-850), 0, velocity=700)
    await motor.run_for_degrees(port.D, 150, (-580))
    for i in range(1, 20):
        light_matrix.write(str(i))
        await runloop.sleep_ms(1000)
    light_matrix.write("!")
    await motor_pair.move_for_degrees(motor_pair.PAIR_1, (2000), 0, velocity=2500)
    await motor.run_for_degrees(port.E,305, (250))
    await motor_pair.move_for_degrees(motor_pair.PAIR_1, (660), 0, velocity=2500)
    await motor.run_for_degrees(port.D, 150, (580))
    await motor_pair.move_for_degrees(motor_pair.PAIR_1, (-920), 0, velocity=700)
runloop.run(main())
