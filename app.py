from flask import Flask, redirect, render_template, request
import pymongo as pymongo
from pymongo.server_api import ServerApi
import pandas as pd
import os
import logging

app = Flask(__name__)

# Before you run app make sure you replace access/secret key below with actual key(s) values to access data from the database
# otherwise you wont be able to see the weather data.

client = pymongo.MongoClient("mongodb+srv://AKIAUECD3KFKU2H4TMXC:JLqhLU5YRhePCnl4lpF0VRujuvEKdjYopNBhTYVf@cluster0"
                             ".re3ie7p.mongodb.net/?authSource=%24external&authMechanism=MONGODB-AWS&retryWrites=true"
                             "&w=majority", server_api=ServerApi('1'))

db = client.KOADB


@app.route('/', methods=['GET', 'POST'])
def index():
    collection = db.KOADB
    # The 'time' gets specific data from the database which is captured between those points.
    # The 'date' gets specific data from the database which is captured on that date. the limit is set to 1 to gathero only 1 data set

    #cursor = db.WeatherStationData.find({'station':'Dewie', 'date':'2022-11-30'}).limit(1) #'time': {"$gte":'18:20:45', "$lt":'18:30:57'}}).limit(1) 
    
    cursorM = db.WeatherStationData.find({'station':'Dewie','date':'2022-12-12'}).limit(1)
    cursorT = db.WeatherStationData.find({'station':'Dewie','date':'2022-12-13'}).limit(1)
    cursorW = db.WeatherStationData.find({'station':'Dewie','date':'2022-12-14'}).limit(1)
    cursorTh = db.WeatherStationData.find({'station':'Dewie','date':'2022-12-15'}).limit(1)
    cursorF = db.WeatherStationData.find({'station':'Dewie','date':'2022-12-16'}).limit(1)
    cursorS = db.WeatherStationData.find({'station':'Dewie','date':'2022-12-17'}).limit(1)
    cursorSun = db.WeatherStationData.find({'station':'Dewie','date':'2022-12-18'}).limit(1)

    cursor1 = db.WeatherStationData.find({'station':'Huey'})
    cursor2 = db.WeatherStationData.find({'station':'Louie'})
    # Get sensor readings for sensor and choose the most recent entry with index "0"
    list_MDewie = list(cursorM)
    list_TDewie = list(cursorT)
    list_WDewie = list(cursorW)
    list_ThDewie = list(cursorTh)
    list_FDewie = list(cursorF)
    list_SDewie = list(cursorS)
    list_SunDewie = list(cursorSun)


    
    list_SHuey = list(cursor1)
    list_SLouie = list(cursor2)
    

    
    return render_template('Welcome.html', MDewie=list_MDewie,  TDewie=list_TDewie, WDewie=list_WDewie, ThDewie = list_ThDewie, FDewie=list_FDewie,SunDewie=list_SunDewie, SDewie=list_SDewie, SHuey=list_SHuey, SLouie=list_SLouie)
   
@app.route('/Welcome', methods=['GET', 'POST'])
def Welcome():
    collection = db.KOADB
    # The 'time' gets specific data from the database which is captured between those points.
    # The 'date' gets specific data from the database which is captured on that date. the limit is set to 1 to gathero only 1 data set

    #cursor = db.WeatherStationData.find({'station':'Dewie', 'date':'2022-11-30'}).limit(1) #'time': {"$gte":'18:20:45', "$lt":'18:30:57'}}).limit(1) 
    
    cursorM = db.WeatherStationData.find({'station':'Dewie','date':'2022-12-12'}).limit(1)
    cursorT = db.WeatherStationData.find({'station':'Dewie','date':'2022-12-13'}).limit(1)
    cursorW = db.WeatherStationData.find({'station':'Dewie','date':'2022-12-14'}).limit(1)
    cursorTh = db.WeatherStationData.find({'station':'Dewie','date':'2022-12-15'}).limit(1)
    cursorF = db.WeatherStationData.find({'station':'Dewie','date':'2022-12-16'}).limit(1)
    cursorS = db.WeatherStationData.find({'station':'Dewie','date':'2022-12-17'}).limit(1)
    cursorSun = db.WeatherStationData.find({'station':'Dewie','date':'2022-12-18'}).limit(1)

    cursor1 = db.WeatherStationData.find({'station':'Huey'})
    cursor2 = db.WeatherStationData.find({'station':'Louie'})
    # Get sensor readings for sensor and choose the most recent entry with index "0"
    list_MDewie = list(cursorM)
    list_TDewie = list(cursorT)
    list_WDewie = list(cursorW)
    list_ThDewie = list(cursorTh)
    list_FDewie = list(cursorF)
    list_SDewie = list(cursorS)
    list_SunDewie = list(cursorSun)


    
    list_SHuey = list(cursor1)
    list_SLouie = list(cursor2)
    

    
    return render_template('Welcome.html', MDewie=list_MDewie,  TDewie=list_TDewie, WDewie=list_WDewie, ThDewie = list_ThDewie, FDewie=list_FDewie,SunDewie=list_SunDewie, SDewie=list_SDewie, SHuey=list_SHuey, SLouie=list_SLouie)
   
@app.route('/KOP', methods=['GET', 'POST'])
def kop():
    return render_template('KOP.html')

@app.route('/Lewie', methods=['GET', 'POST'])
def lewie():
    cursorM = db.WeatherStationData.find({'station':'Lewie','date':'2022-12-12'}).limit(1)
    cursorT = db.WeatherStationData.find({'station':'Lewie','date':'2022-12-13'}).limit(1)
    cursorW = db.WeatherStationData.find({'station':'Lewie','date':'2022-12-14'}).limit(1)
    cursorTh = db.WeatherStationData.find({'station':'Lewie','date':'2022-12-15'}).limit(1)
    cursorF = db.WeatherStationData.find({'station':'Lewie','date':'2022-12-16'}).limit(1)
    cursorS = db.WeatherStationData.find({'station':'Lewie','date':'2022-12-17'}).limit(1)
    cursorSun = db.WeatherStationData.find({'station':'Lewie','date':'2022-12-18'}).limit(1)


    # Get sensor readings for sensor and choose the most recent entry with index "0"
    list_MLewie = list(cursorM)
    list_TLewie = list(cursorT)
    list_WLewie = list(cursorW)
    list_ThLewie = list(cursorTh)
    list_FLewie = list(cursorF)
    list_SLewie = list(cursorS)
    list_SunLewie = list(cursorSun)


    

    

    
    return render_template('Lewie.html', MLewie=list_MLewie,  TLewie=list_TLewie, WLewie=list_WLewie, ThLewie = list_ThLewie, FLewie=list_FLewie,SunLewie=list_SunLewie, SLewie=list_SLewie)

@app.route('/MonthlyLewie', methods=['GET', 'POST'])
def monthlylewie():
    return render_template('MonthlyLewie.html')

@app.route('/Huwey', methods=['GET', 'POST'])
def huwey():
    cursorM = db.WeatherStationData.find({'station':'Huey','date':'2022-12-12'}).limit(1)
    cursorT = db.WeatherStationData.find({'station':'Huey','date':'2022-12-13'}).limit(1)
    cursorW = db.WeatherStationData.find({'station':'Huey','date':'2022-12-14'}).limit(1)
    cursorTh = db.WeatherStationData.find({'station':'Huey','date':'2022-12-15'}).limit(1)
    cursorF = db.WeatherStationData.find({'station':'Huey','date':'2022-12-16'}).limit(1)
    cursorS = db.WeatherStationData.find({'station':'Huey','date':'2022-12-17'}).limit(1)
    cursorSun = db.WeatherStationData.find({'station':'Huey','date':'2022-12-18'}).limit(1)


    # Get sensor readings for sensor and choose the most recent entry with index "0"
    list_MHuwey = list(cursorM)
    list_THuwey = list(cursorT)
    list_WHuwey = list(cursorW)
    list_ThHuwey = list(cursorTh)
    list_FHuwey = list(cursorF)
    list_SHuwey = list(cursorS)
    list_SunHuwey = list(cursorSun)


    

    

    
    return render_template('Huwey.html', MHuwey=list_MHuwey,  THuwey=list_THuwey, WHuwey=list_WHuwey, ThHuwey = list_ThHuwey, FHuwey=list_FHuwey,SunHuwey=list_SunHuwey, SHuwey=list_SHuwey)


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
    cursor2 = db.WeatherStationData.find({'station':'Lewie'})

    list_SDewie = list(cursor)
    list_SHuey = list(cursor1)
    list_SLouie = list(cursor2)


    #MonLow = pd.DataFrame(list_MonLow)
    print(list_SDewie)
    return render_template('Data-Analyst.html', SDewie=list_SDewie, SHuey=list_SHuey, SLouie=list_SLouie)


app.run(host='0.0.0.0')
