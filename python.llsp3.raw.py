from hub import light_matrix, port
import motor
import runloop
import motor_pair

ROTATION = 360
DEFAULT_SPEED=540

async def main():
    global ROTATION
    global DEFAULT_SPEED
    motor_pair.pair(motor_pair.PAIR_1, port.A, port.E)
    await runloop.sleep_ms(500)
    await motor.run_for_degrees(port.D, 150, DEFAULT_SPEED)
    await motor_pair.move_for_degrees(motor_pair.PAIR_1, ROTATION, 0, velocity=DEFAULT_SPEED)
    light_matrix.show_image(light_matrix.IMAGE_HAPPY)
    await motor.run_for_degrees(port.A, 270, 540)
    await motor_pair.move_for_degrees(motor_pair.PAIR_1, (ROTATION*2), 0)
    await motor.run_for_degrees(port.A, 45, 45)
    await motor_pair.move_for_degrees(motor_pair.PAIR_1, 90, 0, velocity=DEFAULT_SPEED)
    await motor.run_for_degrees(port.D, -150, DEFAULT_SPEED)

runloop.run(main())
