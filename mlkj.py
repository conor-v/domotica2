from mcp import mpc
import time


instance_mcp = mpc()

instance_mcp.lees_kanaal_uit(1)
try:
    while True:
        data = instance_mcp.lees_kanaal_uit(0)
        licht = instance_mcp.bepaal_percentage_licht(0)
        print("----------------")
        print("1licht = {}" .format(data))
        print("1Volt = {}" .format(licht))

        data = instance_mcp.lees_kanaal_uit(7)
        temp = instance_mcp.bepaal_temperatuur(7)
        print("1temp = {}".format(data))
        print("1°C = {}".format(temp))
        print("----------------")
        time.sleep(3)

        data = instance_mcp.lees_kanaal_uit(1)
        licht = instance_mcp.bepaal_percentage_licht(1)
        print("----------------")
        print("2licht = {}".format(data))
        print("2Volt = {}".format(licht))

        data = instance_mcp.lees_kanaal_uit(7)
        temp = instance_mcp.bepaal_temperatuur(7)
        print("2temp = {}".format(data))
        print("2°C = {}".format(temp))
        print("----------------")
        time.sleep(3)

        data = instance_mcp.lees_kanaal_uit(2)
        licht = instance_mcp.bepaal_percentage_licht(2)
        print("----------------")
        print("licht3 = {}".format(data))
        print("Volt3 = {}".format(licht))

        data = instance_mcp.lees_kanaal_uit(7)
        temp = instance_mcp.bepaal_temperatuur(7)
        print("3temp = {}".format(data))
        print("3°C = {}".format(temp))
        print("----------------")
        time.sleep(3)

        data = instance_mcp.lees_kanaal_uit(3)
        licht = instance_mcp.bepaal_percentage_licht(3)
        print("----------------")
        print("licht4 = {}".format(data))
        print("Volt4 = {}".format(licht))

        data = instance_mcp.lees_kanaal_uit(7)
        temp = instance_mcp.bepaal_temperatuur(7)
        print("4temp = {}".format(data))
        print("4°C = {}".format(temp))
        print("----------------")
        time.sleep(3)
except:
    print("Wrong!")