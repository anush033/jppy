from flask import Flask,request,render_template
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
@app.route('/submit',methods=['POST'])
def submit():
    username=request.form['username']
    email = request.form['email']
    return f'hello,{username}! your mail is {email}'

if __name__== '__main__':
    app.run()