from flask import Flask, render_template, request, redirect
import sqlite3 

app = Flask(__name__)

def get_db_connection():
    conn = sqlite3.connect('restaurants.db')
    return conn 

@app.route('/')
def home():
    db = get_db_connection()
    result = db.execute("SELECT * FROM cuisines")
    return render_template('home.html', cuisines=result)

@app.route('/restaurants')
def restaurants_all():
    db = get_db_connection()
    result = db.execute("SELECT * FROM restaurants")
    return render_template('restaurants.html', cuisine='All', restaurants=result)

@app.route('/cuisine/<int:cid>')
def cuisine(cid):
    db = get_db_connection()
    cdata = db.execute("SELECT * FROM cuisines WHERE id=?", (cid,)).fetchone()
    result = db.execute("SELECT * FROM restaurants WHERE cuisine_id=?", (cid,))
    return render_template('restaurants.html', cuisine=cdata[1], restaurants=result)

@app.route('/restaurant/<int:rid>')
def restaurant(rid):
    return render_template('restaurant.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST': 
        print(request.form.get('username'))
        print(request.form.get('password'))
        return redirect('/welcome')
    return render_template('login.html')

@app.route('/welcome')
def welcome():
    return render_template('welcome.html')

if __name__ == '__main__':
    app.run(debug=True)