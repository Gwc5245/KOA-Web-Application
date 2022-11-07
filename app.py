from flask import Flask, redirect, render_template, request

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def index():
    return render_template('KOP.html')

@app.route('/Welcome', methods=['GET', 'POST'])
def welcome():
    return render_template('Welcome.html')

@app.route('/Monthly', methods=['GET', 'POST'])
def monthly():
    return render_template('Monthly.html')


@app.route('/SignUp', methods=['GET', 'POST'])
def signup():
    return render_template('SignUp.html')


@app.route('/Fpass', methods=['GET', 'POST'])
def password():
    return render_template('Fpass.HTML')

@app.route('/TOS', methods=['GET', 'POST'])
def TermsAndCoditions():
    return render_template('TOS.html')


@app.route('/Dev', methods=['GET', 'POST'])
def DevDashboard():
    return render_template('Dev.html')

@app.route('/Dev-MngStation')
def DevManageStations():
    return render_template('Dev-MngStation.html')

@app.route('/Dev-AddStation')
def DevAddStations():
    return render_template('Dev-AddStation.html')

@app.route('/Dev-RmStation')
def DevRmStation():
    return render_template('Dev-RmStation.html')


@app.route('/Dev-Alerts')
def DevAlerts():
    return render_template('Dev-Alerts.html')


app.run(host = '0.0.0.0')
