from flask import Flask, render_template, request
from flask_mysqldb import MySQL

app = Flask(__name__, template_folder="templates")
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'root'
app.config['MYSQL_DB'] = 'diwali'
mysql = MySQL(app)


@app.route('/')
def index():
    return render_template('form.html')


@app.route('/submit', methods=['POST', 'GET'])
def login():
    if request.method == 'GET':
        return "login"
    if request.method == 'POST':
        username = request.form['username']
        email = request.form['email']

        cursor = mysql.connection.cursor()
        cursor.execute("INSERT INTO MEMBERS VALUES(%s,%s)", (username, email))
        mysql.connection.commit()
        cursor.close()
        return f"data successfully submit....."
    app.run('127.0.0.1', 404)


if __name__ == "__main__":
    app.run(debug=True)
