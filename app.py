from flask import Flask, render_template, redirect, url_for, request
from flask_migrate import Migrate, upgrade
from models import db, seed_data, Employee, EmployeePicture
from dotenv import load_dotenv
import os

load_dotenv()

app = Flask(__name__)

app.config["SQLALCHEMY_DATABASE_URI"] = os.getenv('LOCAL_DATABASE_URI')

db.init_app(app)

migrate = Migrate(app, db)

@app.route("/")
def firstpage ():
    return render_template('firstpage.html')

@app.route("/login")
def login():
    return render_template('login.html')

@app.route("/hem")
def hem():
    return render_template('index.html')

@app.route("/anstallda")
def anstallda():
    employees=db.session.query(Employee, EmployeePicture).join(EmployeePicture).filter(EmployeePicture.picture_size=='medium').all()
    return render_template('anstallda.html', employees=employees)

@app.route("/personkort")
def personkort():
    return render_template('personkort.html')

@app.route("/kontakt")
def kontakt():
    return render_template('kontakt.html')

@app.route("/logga_ut")
def logga_ut():
    return render_template('logga_ut.html')

if __name__ == '__main__':
    with app.app_context():
        upgrade()
        seed_data(db)

    app.run(debug=True)