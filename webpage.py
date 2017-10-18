from flask import Flask
from flask import render_template
from flask import request
app = Flask(__name__)

import sqlite3
connection = sqlite3.connect('data.db')


@app.route('/')
def index():
    return render_template(
        'index.html',
        header='Demo for CS2300'
    )


@app.route('/submit', methods=['POST'])
def insert():
    field = request.form['form-field']

    cursor = connection.cursor()
    cursor.execute(
        'INSERT INTO Stuff VALUES (NULL, :val)',
        {'val': field}
    )
    connection.commit()

    db_contents = get_all_stuff(cursor=cursor)

    return render_template(
        'index.html',
        list_of_stuff=db_contents,
        header='New Stuff Added'
    )


@app.route('/delete/<stuff_id>', methods=['GET'])
def delete(stuff_id):
    id = int(stuff_id)

    cursor = connection.cursor()
    _, stuff = cursor.execute('SELECT * FROM Stuff WHERE id=:sid',
                              {'sid': id})\
                     .fetchone()

    cursor.execute(
        'DELETE FROM Stuff WHERE id=:stuffid',
        {'stuffid': id}
    )
    connection.commit()

    db_contents = get_all_stuff(cursor)

    return render_template(
        'index.html',
        list_of_stuff=db_contents,
        header='Deleted "{}"'.format(stuff)
    )


def get_all_stuff(cursor):
    db_contents = cursor.execute(
        'SELECT * FROM Stuff'
    ).fetchall()
    return db_contents

