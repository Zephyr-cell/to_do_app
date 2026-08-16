from flask import Flask, render_template, redirect, request, url_for
import sqlite3

app = Flask(__name__)

def get_db_connection():
    conn = sqlite3.connect("tasks.db")
    conn.row_factory = sqlite3.Row
    return conn


def init_db():
    conn = sqlite3.connect("tasks.db")
    c = conn.cursor()
    c.execute("""
        CREATE TABLE IF NOT EXISTS tasks (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            completed BOOLEAN NOT NULL DEFAULT 0
        )
    """)
    conn.commit()
    conn.close()

init_db()

@app.route("/")
def data():
    conn= get_db_connection()
    tasks=conn.execute("SELECT *FROM tasks").fetchall()
    conn.close()
    return render_template("layout.html",tasks=tasks)



@app.route("/add",methods=["POST"])
def add_task():
    task_name= request.form["task"]
    conn= get_db_connection()
    conn.execute("INSERT INTO tasks(name) VALUES (?)",(task_name,))
    conn.commit()
    conn.close()
    return redirect(url_for("data"))


@app.route("/complete/<int:id>")
def complete_task(id):
    conn=get_db_connection()
    conn.execute("UPDATE tasks SET completed=1 WHERE id=?",(id,))
    conn.commit()
    conn.close()
    return redirect(url_for("data"))



@app.route("/delete/<int:id>")
def delete_task(id):
    conn=get_db_connection()
    conn.execute("DELETE FROM tasks WHERE id=?",(id,))
    conn.commit()   
    conn.close()
    return redirect(url_for("data"))
if __name__ == "__main__":
    app.run(debug=True)
