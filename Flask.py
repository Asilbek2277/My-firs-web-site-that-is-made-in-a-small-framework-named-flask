# Flask and Django

from flask import Flask, redirect, render_template
from sqlite3 import connect

loyiha=Flask("Birnchi dastur")

@loyiha.route('/books')

def new_books():

    with connect("kitoblar.db") as db:
        kursor=db.cursor()
        kursor.execute(
            """
            select * from Kitob
            """

        )
        hammasi=kursor.fetchall()

    return  render_template('book_records.html', kitoblar=hammasi)
loyiha.run()