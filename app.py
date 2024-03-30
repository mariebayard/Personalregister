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
    return render_template('hem.html')

@app.route("/anstallda")
def anstallda():
    q=request.args.get('q','')
    sort_column=request.args.get('sort_column','id')
    sort_order=request.args.get('sort_order','asc')
    page=request.args.get('page', 1, type=int)
    employees=db.session.query(Employee, EmployeePicture).join(EmployeePicture).filter(EmployeePicture.picture_size=='thumbnail')
    employees=employees.filter(
        Employee.id.like('%'+ q+ '%')|
        Employee.name.like('%'+ q+ '%')|
        Employee.age.like('%'+ q+ '%')|
        Employee.phone.like('%'+ q+ '%')|
        Employee.country.like('%'+ q+ '%')
    )
    if sort_column == 'name':
        sort_by=Employee.name
    elif sort_column == 'age':
        sort_by=Employee.age
    elif sort_column == 'phone':
        sort_by = Employee.phone
    elif sort_column == 'email':
        sort_by = Employee.email
    else:
        sort_by=Employee.id

    if sort_order == 'asc':
        sort_by=sort_by.asc()
    elif sort_order == 'desc':
        sort_by = sort_by.desc()
    
    employees=employees.order_by(sort_by)

    pa_obj=employees.paginate(page=page, per_page=30, error_out=True)
    return render_template('anstallda.html', 
                           employees=pa_obj.items,
                           q=q,
                           sort_order=sort_order,
                           sort_column=sort_column,
                           pagination=pa_obj,
                           page=page,
                           nr_pages=pa_obj.pages,
                           has_next=pa_obj.has_next,
                           has_prev=pa_obj.has_prev)

@app.route("/personkort/search", methods=['POST'])
def search_person():
   query=request.form.get('query', type=int)
   person= db.session.query(Employee).filter_by(id=query).first()
   if person:
       picture=db.session.query(EmployeePicture).filter_by(employee_id=person.id, picture_size='large').first()
       return render_template('personkort.html', person=person, picture=picture)
   else:
       message='Det finns ingen anställd med sökt ID'
       return render_template('personkort.html', message=message)

@app.route("/personkort/<person_id>")
def personkort(person_id):
    person=db.session.query(Employee).filter(Employee.id==person_id).first()
    picture=db.session.query(EmployeePicture).filter_by(employee_id=person_id, picture_size='large').first()
    return render_template('personkort.html',person=person, picture=picture)

@app.route("/kontakt")
def kontakt():
    return render_template('kontakt.html')

@app.route("/logga_ut")
def logga_ut():
    return render_template('logout.html')

if __name__ == '__main__':
    with app.app_context():
        upgrade()
        seed_data(db)

    app.run(debug=True)