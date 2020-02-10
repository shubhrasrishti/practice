from flask import Flask, render_template, request, url_for, redirect, flash
from flask_mysqldb import MySQL
app = Flask(__name__)

app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'subu@3394'
app.config['MYSQL_DB'] = 'project'

mysql = MySQL(app)


@app.route('/', methods=['GET', 'POST'])
@app.route('/login', methods=['GET', 'POST'])
def index():
    if request.method == "POST":
        details = request.form
        userName = details['uname']
        password = details['pass']
        
        if userName == "shubhra" and password == "flask123":
            cur = mysql.connection.cursor()
            cur.execute("INSERT INTO MyUsers(username, password) VALUES (%s, %s)", (userName, password))
            mysql.connection.commit()
            cur.close()
            return redirect(url_for('home'))
        else:
            pass
    return render_template('login.html')


@app.route('/home', methods=['GET', 'POST'])
def home():
    return render_template('home.html')


if __name__ == '__main__':
    app.run(debug=True)
