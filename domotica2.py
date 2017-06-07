from flask import Flask, render_template
import datetime
app = Flask(__name__)

@app.route("/")
def hello():
    return render_template('home.html')

@app.route("/home.html")
def home():
    return render_template('home.html')

@app.route("/kamers.html")
def kamers():
    return render_template('kamers.html')

@app.route("/Ktoevoegen.html")
def ktoevoegen():
    return render_template('ktoevoegen.html')

@app.route("/instellingen.html")
def instellingen():
    return render_template('instellingen.html')

@app.route("/muziek.html")
def muziek():
    return render_template('muziek.html')

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0')
