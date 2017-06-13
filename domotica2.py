from flask import Flask, render_template
from dbconn import DbConnection as DBclass
from mcp import mpc



app = Flask(__name__)

@app.route("/")
def hello():
    return render_template('home.html')

@app.route("/home.html")
def home():
    return render_template('home.html')

@app.route("/kamers.html")
def kamers():
    db = DBclass
    instance_mcp = mpc()
    temp = instance_mcp.bepaal_temperatuur(7)
    licht = instance_mcp.bepaal_percentage_licht(0)
    # db.execute("INSERT INTO temperatuur(tijd, graden) values(NOW(), '{param}')",param=temp)

    return render_template('kamers.html', temp=temp, licht=licht)

@app.route("/toevoegen.html")
def toevoegen():
    return render_template('toevoegen.html')

@app.route("/instellingen.html")
def instellingen():
    return render_template('instellingen.html')

@app.route("/muziek.html")
def muziek():
    return render_template('muziek.html')

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0')
