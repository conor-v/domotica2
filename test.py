from mcp import mpc
import time
from dbconn import DbConnection as db

db = db
instance_mcp = mpc()




data = instance_mcp.bepaal_temperatuur(7)
def setIntoDB(data):
    while 1:
        time.sleep(60)
        db.execute("INSERT INTO temperatuur(tijd, graden) values(NOW(), +'data'+)")

setIntoDB(data)


data = instance_mcp.bepaal_percentage_licht(0)
def setIntoDB(data):
    while 1:
        time.sleep(60)
        db.execute("INSERT INTO licht(tijd, volt) VALUES(now(), +'data'+)")