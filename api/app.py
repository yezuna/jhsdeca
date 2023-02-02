from flask import Flask
from flask import request, render_template, flash, redirect, url_for
app = Flask(__name__)
app.secret_key = 'elusivekey'

@app.route('/')
def home():
    return 'Hello, World!'

                
@app.route('/login', methods=['GET', 'POST'])
def login():
    error = None
    if request.method == 'POST':
        if request.form['password'] != 'secret':
            error = 'Invalid credentials'
        else:
            flash('You were successfully logged in')
            return render_template('index.html')
    return render_template('login.html', error=error)