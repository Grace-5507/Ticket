from distutils.log import error
import sqlite3
from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import insert, table, column



app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///SQLite_db.sqlite"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
db = SQLAlchemy(app)


class Buses(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    bus_name = db.Column(db.String(100))
    capacity = db.Column(db.String(100))


class Travellers(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    Passenger_name = db.Column(db.String(100))
    phone_number = db.Column(db.Integer)
 
    
@app.route("/")
def index():
    return render_template("main.html")



@app.route('/get/<travellers_id>/passengers', methods=['GET'])
def get_passengers():
    
    Passengers = db.session.query(Passengers).all()
    Passengers = []
    for Passengers in Passengers:
        Passengers.append()
    return redirect(url_for("index"))


@app.route("/add", methods=['POST'] ) 
def add_passanger():
    passenger_name = request.form.get("passenger")
    print('passenger name', passenger_name)
    new_passenger = Travellers(Passenger_name=passenger_name)
    db.session.add(new_passenger)
    db.session.commit()
    return redirect(url_for("index"))


    self.passanger = []  
    bus = Bus(4)

@app.route("/open_seats/<buses_id>/capacity", methods=["GET"] )
def open_seats(Capacity):
    capacity = request.form.get ("capacity")
    print(capacity)
    return capacity - len(get_passengers)

@app.route("/update/<travellers_id>/passenger/passenger_id", methods=["GET", 'POST'] )
def update():
    return redirect(url_for("index"))

#the program below creates and connects to the database file SQLite_python.db and prints the SQLite version details

try:
    sqliteConnection = sqlite3.connect("SQLite_db.sqlite")
    sqlite3.Cursor = sqliteConnection.cursor()
    print("Database created and sussessfully connected to SQLite")

    sqlite_select_Query = "select sqlite_version();"
    sqlite3.Cursor.execute(sqlite_select_Query)
    record = sqlite3.Cursor.fetchall()

except sqlite3.Error as error:
    print("error while connecting to sqlite", error)
finally:
    if sqliteConnection:
        sqliteConnection.close()
        print("The SQLite connection is closed")

#this program creates tables in the database
try:
    sqliteConnection = sqlite3.connect("SQLite_db.sqlite")
    sqlite_create_table_query ='''CREATE TABLE Buses(
        id INTEGER PRIMARY KEY,
        bus_name TEXT NOT NULL,
        capacity TEXT NOT NULL);'''

    sqlite_create_table_query ='''CREATE TABLE Travellers(
        id INTEGER PRIMARY KEY,
        Passenger_name TEXT NOT NULL,
        phone_number TEXT NOT NULL);'''

    Cursor = sqliteConnection.cursor()
    print("Successfully connected to SQLite")
    Cursor.execute(sqlite_create_table_query)
    sqliteConnection.commit()
    print("SQLite table created")

    Cursor.close()

except sqlite3.Error as error:
    print("Error While creating SQLite tables", error)

finally:
    if sqliteConnection:
        sqliteConnection.close()
        print("sqlite connection is closed")




if __name__ == "__main__":
    db.create_all()
    


    app.run(debug=True)
