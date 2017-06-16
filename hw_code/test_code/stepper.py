from RPi import GPIO
from time import sleep
from hw_code.model.Mpc import Mpc
from hw_code.model.StepperMotor import StepperMotor

try:
    instantie_motor = StepperMotor(driverpin_1=27, driverpin_2=22, driverpin_3=23, driverpin_4=24)
    instantie_mpc = Mpc()

    while True:
        print("start")
        instantie_motor.draai_links(50)
        sleep(2)

        instantie_motor.draai_rechts(50)
        sleep(2)

        print("end")

finally:
    GPIO.cleanup()