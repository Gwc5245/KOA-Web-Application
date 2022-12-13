from flask import Flask, redirect, render_template, request
import pymongo as pymongo
from pymongo.server_api import ServerApi
import pandas as pd
import os

app = Flask(__name__)

# Before you run app make sure you replace access/secret key below with actual key(s) values to access data from the database
# otherwise you wont be able to see the weather data.
client = pymongo.MongoClient("mongodb+srv://<AWS access key>:<AWS secret key>@cluster0"
                            ".re3ie7p.mongodb.net/?authSource=%24external&authMechanism=MONGODB-AWS&retryWrites=true"
                           "&w=majority", server_api=ServerApi('1'))


db = client.KOA_WebApp
db = client.KOADB


@app.route('/', methods=['GET', 'POST'])
def index():
    return render_template('Welcome.html')


@app.route('/Welcome', methods=['GET', 'POST'])
def welcome():
    collection = db.KOADB
    # The 'time' gets specific data from the database which is captured between those points.
    # The 'date' gets specific data from the database which is captured on that date. the limit is set to 1 to gathero only 1 data set

    cursor = db.WeatherStationData.find({'station':'Dewie', 'date':'2022-11-30'}).limit(1) #'time': {"$gte":'18:20:45', "$lt":'18:30:57'}}).limit(1) 


    cursor1 = db.WeatherStationData.find({'station':'Huey'})
    cursor2 = db.WeatherStationData.find({'station':'Louie'})

    list_SDewie = list(cursor)
    list_SHuey = list(cursor1)
    list_SLouie = list(cursor2)
    

    return render_template('Welcome.html', SDewie=list_SDewie, SHuey=list_SHuey, SLouie=list_SLouie)


# Retrieves the document with the following criteria:
# The name of the collection it is in (MongoDB),
# The field name of the document you're querying,
# The value that should be in the field.
# The method will return a PyMongo cursor object.
#def retrieveMongoDocument(collectionName, searchFieldName, searchFieldValue):
    #dbWebApp = client.KOA_WebApp
    #print("Searching for", searchFieldName, "with a value of", searchFieldValue, "in collection", collectionName + ".")
    #cursor = [i for i in dbWebApp[collectionName].find({searchFieldName: (searchFieldValue)})]
    #return cursor

@app.route('/KOP', methods=['GET', 'POST'])
def kop():
    return render_template('KOP.html')

@app.route('/Lewie', methods=['GET', 'POST'])
def lewie():
    return render_template('Lewie.html')

@app.route('/MonthlyLewie', methods=['GET', 'POST'])
def monthlylewie():
    return render_template('MonthlyLewie.html')

@app.route('/Huwey', methods=['GET', 'POST'])
def huwey():
    return render_template('Huwey.html')

@app.route('/MonthlyHuwey', methods=['GET', 'POST'])
def monthlyhuwey():
    return render_template('MonthlyHuwey.html')

@app.route('/Monthly', methods=['GET', 'POST'])
def monthly():
    return render_template('Monthly.html')

@app.route('/Settings', methods=['GET', 'POST'])
def settings():
    return render_template('Settings.html')


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
    collection = db.KOADB
    cursor = db.WeatherStationData.find({'station':'Dewie'})
    cursor1 = db.WeatherStationData.find({'station':'Huey'})
    cursor2 = db.WeatherStationData.find({'station':'Louie'})

    list_SDewie = list(cursor)
    list_SHuey = list(cursor1)
    list_SLouie = list(cursor2)


    #MonLow = pd.DataFrame(list_MonLow)
    print(list_SDewie)
    return render_template('Data-Analyst.html', SDewie=list_SDewie, SHuey=list_SHuey, SLouie=list_SLouie)


app.run(host='0.0.0.0')
