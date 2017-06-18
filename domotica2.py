from flask import Flask, render_template, redirect, request
from hw_code.model.dbconn import DbConnection

db = DbConnection('db_domotica')
app = Flask(__name__)


@app.route("/")
def begin():
    return render_template('home.html')


@app.route("/home")
def home():
    return render_template('home.html')


@app.route("/kamers", methods=["GET", "POST"])
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

    db = DbConnection('db_domotica')
    if request.method == "POST":
        button_id = request.form['button_id']
        # drukknop_g = request.form['garage']
        query3 = "select lamp_status from kamers WHERE id = " + button_id + ";"
        query4 = "UPDATE kamers SET lamp_status=1  WHERE lamp_status=0 ;"
        query5 = "UPDATE kamers SET lamp_status=0 WHERE lamp_status=1 ;"
        query6 = "UPDATE garage SET  WHERE id = 1;"
        lamp_status_result = db.query(query3)
        lamp_status_list = []
        for test in lamp_status_result:
            for x in test:
                lamp_status_list.append(x)
        lamp_status = lamp_status_list[0]

        if lamp_status == 1:
            db.execute(query5)
        else:
            db.execute(query4)

    return render_template('kamers.html', temp=tempwaarden, lichtwaarden=lichtwaarden)


@app.route("/instellingen")
def instellingen():
    return render_template('instellingen.html')


@app.route("/muziek")
def muziek():
    return render_template('muziek.html')


if __name__ == "__main__":
    app.run(debug=True, host='169.254.10.1')
