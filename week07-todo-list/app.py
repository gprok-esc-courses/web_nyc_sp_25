from flask import Flask, render_template, redirect, request
import sqlite3

app = Flask(__name__)
connection = sqlite3.connect('todo.db')
connection.execute("""CREATE TABLE IF NOT EXISTS tasks 
                    (id INTEGER PRIMARY KEY AUTOINCREMENT, 
                    content TEXT, 
                    closed INT, 
                    date_posted DATETIME DEFAULT current_timestamp)""")

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/add/task', methods=['GET', 'POST'])
def add_task():
    if request.method == 'POST':
        content = request.form['content']
        db = sqlite3.connect('todo.db')
        cursor = db.cursor()
        cursor.execute("INSERT INTO tasks (content, closed) VALUES (?, 0)", (content,))
        db.commit()
        return redirect('/tasks')
    return render_template('add_task.html')

@app.route('/tasks')
def tasks():
    db = sqlite3.connect('todo.db')
    cursor = db.cursor()
    tasks = cursor.execute("SELECT * FROM tasks WHERE closed=0")
    task_list = list(cursor)
    return render_template('tasks.html', tasks=task_list, total=len(task_list))

@app.route('/completed')
def completed():
    db = sqlite3.connect('todo.db')
    cursor = db.cursor()
    tasks = cursor.execute("SELECT * FROM tasks WHERE closed=1")
    task_list = list(tasks)
    return render_template('completed.html', tasks=task_list, total=len(task_list))

@app.route('/complete/<tid>')
def complete_task(tid):
    db = sqlite3.connect('todo.db')
    cursor = db.cursor()
    cursor.execute("UPDATE tasks SET closed=1 WHERE id=" + tid)
    db.commit()
    return redirect('/tasks')

@app.route('/undo/<tid>')
def complet_undo(tid):
    db = sqlite3.connect('todo.db')
    cursor = db.cursor()
    cursor.execute("UPDATE tasks SET closed=0 WHERE id=" + tid)
    db.commit()
    return redirect('/completed')

if __name__ == '__main__':
    app.run(debug=True)