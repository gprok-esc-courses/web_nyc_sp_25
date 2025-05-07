from flask import Flask, render_template, request, redirect, session, jsonify
from flask_session import Session
import sqlite3 

app = Flask(__name__)

app.config["SESSION_TYPE"] = "filesystem"

Session(app)

def get_all_cuisines():
    db = get_db_connection()
    result = db.execute("SELECT * FROM cuisines")
    return result

def get_db_connection():
    conn = sqlite3.connect('restaurants.db')
    return conn 

@app.route('/')
def home():
    db = get_db_connection()
    cuisines = get_all_cuisines()
    return render_template('home.html', cuisines=cuisines)

@app.route('/api/restaurants')
def api_restaurants_all():
    db = get_db_connection()
    result = db.execute("SELECT * FROM restaurants")
    rows = result.fetchall()
    return jsonify(rows)

@app.route('/restaurants')
def restaurants_all():
    db = get_db_connection()
    cuisines = get_all_cuisines()
    result = db.execute("SELECT * FROM restaurants")
    return render_template('restaurants.html', cuisine='All', restaurants=result, cuisines=cuisines)

@app.route('/cuisine/<int:cid>')
def cuisine(cid):
    db = get_db_connection()
    cuisines = get_all_cuisines()
    cdata = db.execute("SELECT * FROM cuisines WHERE id=?", (cid,)).fetchone()
    result = db.execute("SELECT * FROM restaurants WHERE cuisine_id=?", (cid,))
    return render_template('restaurants.html', cuisine=cdata[1], restaurants=result, cuisines=cuisines)

@app.route('/restaurant/<int:rid>')
def restaurant(rid):
    db = get_db_connection()
    cuisines = get_all_cuisines()
    restaurant = db.execute("SELECT * FROM restaurants WHERE id=?", (rid,)).fetchone()
    cuisine = db.execute("SELECT * FROM cuisines WHERE id=?", (restaurant[5],)).fetchone()
    reviews = db.execute("SELECT * FROM reviews WHERE restaurant_id=?", (rid,))
    return render_template('restaurant.html', restaurant=restaurant, cuisine=cuisine, cuisines=cuisines, reviews=reviews)

@app.route('/login', methods=['GET', 'POST'])
def login():
    cuisines = get_all_cuisines()
    if request.method == 'POST': 
        username = request.form.get('username')
        password = request.form.get('password')
        db = get_db_connection() 
        result = db.execute("SELECT * FROM users WHERE username=? AND password=?", (username, password)).fetchone()
        if result is None:
            return render_template('login.html', message='Invalid credentials', cuisines=cuisines)
        else:
            session['username'] = result[1]
            session['role'] = result[3]
            session['uid'] = result[0]
            return redirect('/welcome')
    return render_template('login.html', message='')

@app.route('/logout')
def logout():
    session["username"] = None 
    session["role"] = None 
    session["uid"] = None
    return redirect('/login')

@app.route('/welcome')
def welcome():
    cuisines = get_all_cuisines()
    if not session.get("username"):
        return render_template('login.html', message='You need to login', cuisines=cuisines)
    else:
        username = session.get("username")
        return render_template('welcome.html', username=username, cuisines=cuisines)
    
@app.route('/add/review', methods=['POST'])
def add_review():
    rate = request.form['rate']
    comment = request.form['comment']
    rid = request.form['rid']
    uid = session.get("uid")
    db = get_db_connection()
    db.execute("INSERT INTO reviews (rate, comment, user_id, restaurant_id) VALUES (?, ?, ?, ?)",
               (rate, comment, uid, rid))
    db.commit()
    return redirect('/restaurant/' + rid)

if __name__ == '__main__':
    app.run(debug=True, port=5000)