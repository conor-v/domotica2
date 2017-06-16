from RPi import GPIO
from time import sleep
from hw_code.model.Mpc import Mpc
from hw_code.model.dbconn import DbConnection

try:
    instantie_mpc = Mpc()
    db = DbConnection('db_domotica')
    # licht kanaal mcp, temp kanaal mcp, GPIO pin lamp
    kamers = [[0, 4, 18], [1, 5, 21], [2, 6, 20], [3, 7, 16]]

    GPIO.setmode(GPIO.BCM)

    for getal in range(0, len(kamers)):
        kamer = kamers[getal]
        GPIO.setup(kamer[2], GPIO.OUT)

    GPIO.setup(18, GPIO.OUT)
    GPIO.setup(21, GPIO.OUT)
    GPIO.setup(20, GPIO.OUT)
    GPIO.setup(16, GPIO.OUT)

    while True:
        print("start loop")

        # update sensors in db
        for getal in range(0, len(kamers)):
            kamer = kamers[getal]
            sql = ('UPDATE kamers SET kamers.current_light_precent = %(licht)s, kamers.current_temp_degree = %(graden)s WHERE kamers.id = %(getal)s;')
            params = {
                'licht':  instantie_mpc.bepaal_percentage_licht(kamer[0]),
                'graden': instantie_mpc.bepaal_temperatuur(kamer[1]),
                'getal': getal + 1
            }

            db.execute(sql, params)

        sleep(0.2)

        #controle lampen aangezet
        sql = ('SELECT lamp_status FROM db_domotica.kamers;')
        result = db.query(sql, dictionary=True)

        for getal in range(0, len(kamers)):
            record = result[getal]
            kamer = kamers[getal]

            if record['lamp_status'] == True:
                GPIO.output(kamer[2], GPIO.HIGH)
                print("Lamp: " + str(getal +1) + "aan")
            else:
                GPIO.output(kamer[2], GPIO.LOW)
                print("Lamp: " + str(getal + 1) + "uit")

        print("end loop")



        sleep(0.2)

finally:
    GPIO.cleanup()

