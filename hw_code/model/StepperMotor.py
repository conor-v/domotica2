from RPi import GPIO
from time import sleep


class StepperMotor():
    positie_list = [0b00001000,
                    0b00001100,
                    0b00000100,
                    0b00000110,
                    0b00000010,
                    0b00000011,
                    0b00000001,
                    0b00001001]

    # reverse_list = [0b00001001,
    #                 0b00000001,
    #                 0b00000011,
    #                 0b00000010,
    #                 0b00000110,
    #                 0b00000100,
    #                 0b00001100,
    #                 0b00001000]

    def __init__(self, driverpin_1, driverpin_2, driverpin_3, driverpin_4, stepdir=1):
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(driverpin_1, GPIO.OUT)
        GPIO.setup(driverpin_2, GPIO.OUT)
        GPIO.setup(driverpin_3, GPIO.OUT)
        GPIO.setup(driverpin_4, GPIO.OUT)
        self._stepdir = stepdir

        self.__list_driverpins = [driverpin_1, driverpin_2, driverpin_3, driverpin_4]
        # self.__driverpin_1 = driverpin_1
        # self.__driverpin_2 = driverpin_2
        # self.__driverpin_3 = driverpin_3
        # self.__driverpin_4 = driverpin_4

    def draai_links(self, aantal_rondjes):

        for rondjes in range(0, aantal_rondjes):

            mask_getal = 0b00001000
            self._stepdir = 1

            for getal in range(0, 8):
                # print(self.positie_list[getal])
                for getal2 in range(0, 4):
                    # print(self.positie_list[getal] & (mask_getal >> getal2))
                    print("Pin " + str(self.__list_driverpins[getal2]) + " krijgt " + str(
                        self.positie_list[getal] & (mask_getal >> getal2)))
                    GPIO.output(self.__list_driverpins[getal2], self.positie_list[getal] & (mask_getal >> getal2))

                sleep(0.01)

    def draai_rechts(self, aantal_rondjes):

        for rondjes in range(0, aantal_rondjes):

            mask_getal = 0b00001000
            self._stepdir = -1

            for getal in range(8, 0, -1):

                mask_getal = 0b00001000

                for getal in range(0, 8):
                    # print(self.positie_list[getal])
                    for getal2 in range(0, 4):
                        # print(self.positie_list[getal] & (mask_getal >> getal2))
                        print("Pin " + str(self.__list_driverpins[getal2]) + " krijgt " + str(
                            self.positie_list[getal] & (mask_getal >> getal2)))
                        GPIO.output(self.__list_driverpins[getal2], self.positie_list[getal] & (mask_getal >> getal2))
                sleep(0.01)