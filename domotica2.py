from flask import Flask, render_template, redirect, request
from hw_code.model.dbconn import DbConnection

db = DbConnection('db_domotica')
# db = DbConnection
app = Flask(__name__)


@app.route("/")
def begin():
    return render_template('home.html')


@app.route("/home.html")
def home():
    return render_template('home.html')


@app.route("/kamers.html", methods=["GET", "POST"])
def sensoren():
    db = DbConnection('db_domotica')

    query = "select current_light_precent from kamers;"
    light = db.query(query)
    lichtwaarden = []
    for test in light:
        for x in test:
            lichtwaarden.append(x)

    query2 = "select current_temp_degree from kamers;"
    temp = db.query(query2)
    tempwaarden = []
    for test in temp:
        for x in test:
            tempwaarden.append(x)

    # if request.method == "POST":
        # drukknop_l = request.form['lamp_status']
        # drukknop_g = request.form['garage']
    # query3 = "UPDATE db.kamers SET lamp_status  WHERE id = 1;"
        # query4 = "UPDATE garage SET status = '1' OR '0' WHERE 'drukknop_g' == PUSHED;"
    db.execute("SELECT * FROM kamers WHERE id = '1'; UPDATE kamers  WHERE lamp_status=1", "SET lamp_status=0")
        # db.execute(query4, drukknop_g)

    return render_template('kamers.html')



@app.route("/instellingen.html")
def instellingen():
    return render_template('instellingen.html')


@app.route("/muziek.html")
def muziek():
    return render_template('muziek.html')


if __name__ == "__main__":
    app.run(debug=True, host='169.254.10.1')
