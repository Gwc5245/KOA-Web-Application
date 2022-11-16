from flask import Flask, redirect, render_template, request
import pymongo as pymongo
from pymongo.server_api import ServerApi
import pandas as pd
import os

app = Flask(__name__)

# Before you run app make sure you replace access/secret key below with actual key(s) values to access data from the database
# otherwise you wont be able to see the weather data.
client = pymongo.MongoClient("mongodb+srv://AKIAUECD3KFKSDVHZJXB:qKjmQF8VKRwZXyJtlakEKZ1dzsWixQHHSHjX3jV0@cluster0"
                            ".re3ie7p.mongodb.net/?authSource=%24external&authMechanism=MONGODB-AWS&retryWrites=true"
                           "&w=majority", server_api=ServerApi('1'))


db = client.KOA_WebApp


@app.route('/', methods=['GET', 'POST'])
def index():
    return render_template('KOP.html')


@app.route('/Welcome', methods=['GET', 'POST'])
def welcome():
    collection = db.KOA_WebApp.Temp
    # cursor = db.Temp.find({"_id": "1"})
    cursor = retrieveMongoDocument("Temp", "_id", "1")
    list_MonLow = list(cursor)
    MonLow = pd.DataFrame(list_MonLow)
    collection = db.Temp
    cursor = db.Temp.find({"_id": "2"})
    list_MonHigh = list(cursor)
    MonHigh = pd.DataFrame(list_MonHigh)

    cursor = db.Temp.find({"_id": "3"})
    list_MonLow = list(cursor)
    TueLow = pd.DataFrame(list_MonLow)
    collection = db.KOA_WebApp.Temp
    cursor = db.Temp.find({"_id": "4"})
    list_MonHigh = list(cursor)
    TueHigh = pd.DataFrame(list_MonHigh)
    return render_template('Welcome.html', MonLow=MonLow, MonHigh=MonHigh, TueHigh=TueHigh, TueLow=TueLow)


# Retrieves the document with the following criteria:
# The name of the collection it is in (MongoDB),
# The field name of the document you're querying,
# The value that should be in the field.
# The method will return a PyMongo cursor object.
def retrieveMongoDocument(collectionName, searchFieldName, searchFieldValue):
    collection = db[collectionName]
    cursor = collection.find_one({searchFieldName: searchFieldValue})
    return cursor


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


@app.route('/Data-Analyst')
def DataAnalyst():
    return render_template('Data-Analyst.html')


app.run(host='0.0.0.0')
