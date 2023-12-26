from flask import Flask
from flask_mysqldb import MySQL

app=Flask(__name__)
@app.route('/')
def index():
    return render_template('form.html')
