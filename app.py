from flask import Flask, redirect, render_template, request

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def index():
    return render_template('KOP.html')

@app.route('/Welcome', methods=['GET', 'POST'])
def welcome():
    return render_template('Welcome.html')


@app.route('/SignUp', methods=['GET', 'POST'])
def signup():
    return render_template('SignUp.html')



@app.route('/Fpass', methods=['GET', 'POST'])
def password():
    return render_template('Fpass.HTML')

@app.route('/TOS', methods=['GET', 'POST'])
def TermsAndCoditions():
    return render_template('TOS.html')

app.run()