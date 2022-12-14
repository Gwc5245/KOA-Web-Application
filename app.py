from flask import Flask, redirect, render_template, request
import pymongo as pymongo
from pymongo.server_api import ServerApi
import pandas as pd
import os
import logging

app = Flask(__name__)

# Before you run app make sure you replace access/secret key below with actual key(s) values to access data from the database
# otherwise you wont be able to see the weather data.

client = pymongo.MongoClient("mongodb+srv://<AWS access key>:<AWS secret key>@cluster0"
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
    cursor1 = db.WeatherStationData.find({'station':'Lewie','date':'2022-12-1'}).limit(1)
    cursor2 = db.WeatherStationData.find({'station':'Lewie','date':'2022-12-2'}).limit(1)
    cursor3 = db.WeatherStationData.find({'station':'Lewie','date':'2022-12-3'}).limit(1)
    cursor4 = db.WeatherStationData.find({'station':'Lewie','date':'2022-12-4'}).limit(1)
    cursor5 = db.WeatherStationData.find({'station':'Lewie','date':'2022-12-5'}).limit(1)
    cursor6 = db.WeatherStationData.find({'station':'Lewie','date':'2022-12-6'}).limit(1)
    cursor7 = db.WeatherStationData.find({'station':'Lewie','date':'2022-12-7'}).limit(1)
    cursor8 = db.WeatherStationData.find({'station':'Lewie','date':'2022-12-8'}).limit(1)
    cursor9 = db.WeatherStationData.find({'station':'Lewie','date':'2022-12-9'}).limit(1)
    cursor10 = db.WeatherStationData.find({'station':'Lewie','date':'2022-12-10'}).limit(1)
    cursor11 = db.WeatherStationData.find({'station':'Lewie','date':'2022-12-11'}).limit(1)
    cursor12 = db.WeatherStationData.find({'station':'Lewie','date':'2022-12-12'}).limit(1)
    cursor13 = db.WeatherStationData.find({'station':'Lewie','date':'2022-12-13'}).limit(1)
    cursor14 = db.WeatherStationData.find({'station':'Lewie','date':'2022-12-14'}).limit(1)

    
    # Get sensor readings for sensor and choose the most recent entry with index "0"
    list_1Lewie = list(cursor1)
    list_2Lewie = list(cursor2)
    list_3Lewie = list(cursor3)
    list_4Lewie = list(cursor4)
    list_5Lewie = list(cursor5)
    list_6Lewie = list(cursor6)
    list_7Lewie = list(cursor7)
    list_8Lewie = list(cursor8)
    list_9Lewie = list(cursor9)
    list_10Lewie = list(cursor10)
    list_11Lewie = list(cursor11)
    list_12Lewie = list(cursor12)
    list_13Lewie = list(cursor13)
    list_14Lewie = list(cursor14)


    

    
    return render_template('MonthlyLewie.html', Lewie1=list_1Lewie,  Lewie2=list_2Lewie, Lewie3=list_3Lewie, Lewie4 = list_4Lewie, Lewie5=list_5Lewie,Lewie6=list_6Lewie, Lewie7=list_7Lewie,Lewie8=list_8Lewie, Lewie9=list_9Lewie,Lewie10=list_10Lewie,Lewie11=list_11Lewie,Lewie12=list_12Lewie,Lewie13=list_13Lewie,Lewie14=list_14Lewie)
   

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
    cursor1 = db.WeatherStationData.find({'station':'Huey','date':'2022-12-1'}).limit(1)
    cursor2 = db.WeatherStationData.find({'station':'Huey','date':'2022-12-2'}).limit(1)
    cursor3 = db.WeatherStationData.find({'station':'Huey','date':'2022-12-3'}).limit(1)
    cursor4 = db.WeatherStationData.find({'station':'Huey','date':'2022-12-4'}).limit(1)
    cursor5 = db.WeatherStationData.find({'station':'Huey','date':'2022-12-5'}).limit(1)
    cursor6 = db.WeatherStationData.find({'station':'Huey','date':'2022-12-6'}).limit(1)
    cursor7 = db.WeatherStationData.find({'station':'Huey','date':'2022-12-7'}).limit(1)
    cursor8 = db.WeatherStationData.find({'station':'Huey','date':'2022-12-8'}).limit(1)
    cursor9 = db.WeatherStationData.find({'station':'Huey','date':'2022-12-9'}).limit(1)
    cursor10 = db.WeatherStationData.find({'station':'Huey','date':'2022-12-10'}).limit(1)
    cursor11 = db.WeatherStationData.find({'station':'Huey','date':'2022-12-11'}).limit(1)
    cursor12 = db.WeatherStationData.find({'station':'Huey','date':'2022-12-12'}).limit(1)
    cursor13 = db.WeatherStationData.find({'station':'Huey','date':'2022-12-13'}).limit(1)
    cursor14 = db.WeatherStationData.find({'station':'Huey','date':'2022-12-14'}).limit(1)

    
    # Get sensor readings for sensor and choose the most recent entry with index "0"
    list_1Huey = list(cursor1)
    list_2Huey = list(cursor2)
    list_3Huey = list(cursor3)
    list_4Huey = list(cursor4)
    list_5Huey = list(cursor5)
    list_6Huey = list(cursor6)
    list_7Huey = list(cursor7)
    list_8Huey = list(cursor8)
    list_9Huey = list(cursor9)
    list_10Huey = list(cursor10)
    list_11Huey = list(cursor11)
    list_12Huey = list(cursor12)
    list_13Huey = list(cursor13)
    list_14Huey = list(cursor14)


    

    
    return render_template('MonthlyHuwey.html', Huey1=list_1Huey,  Huey2=list_2Huey, Huey3=list_3Huey, Huey4 = list_4Huey, Huey5=list_5Huey,Huey6=list_6Huey, Huey7=list_7Huey, Huey8=list_8Huey, Huey9=list_9Huey,Huey10=list_10Huey,Huey11=list_11Huey,Huey12=list_12Huey,Huey13=list_13Huey,Huey14=list_14Huey)
   

@app.route('/Monthly', methods=['GET', 'POST'])
def monthly():
    cursor1 = db.WeatherStationData.find({'station':'Dewie','date':'2022-12-1'}).limit(1)
    cursor2 = db.WeatherStationData.find({'station':'Dewie','date':'2022-12-2'}).limit(1)
    cursor3 = db.WeatherStationData.find({'station':'Dewie','date':'2022-12-3'}).limit(1)
    cursor4 = db.WeatherStationData.find({'station':'Dewie','date':'2022-12-4'}).limit(1)
    cursor5 = db.WeatherStationData.find({'station':'Dewie','date':'2022-12-5'}).limit(1)
    cursor6 = db.WeatherStationData.find({'station':'Dewie','date':'2022-12-6'}).limit(1)
    cursor7 = db.WeatherStationData.find({'station':'Dewie','date':'2022-12-7'}).limit(1)
    cursor8 = db.WeatherStationData.find({'station':'Dewie','date':'2022-12-8'}).limit(1)
    cursor9 = db.WeatherStationData.find({'station':'Dewie','date':'2022-12-9'}).limit(1)
    cursor10 = db.WeatherStationData.find({'station':'Dewie','date':'2022-12-10'}).limit(1)
    cursor11 = db.WeatherStationData.find({'station':'Dewie','date':'2022-12-11'}).limit(1)
    cursor12 = db.WeatherStationData.find({'station':'Dewie','date':'2022-12-12'}).limit(1)
    cursor13 = db.WeatherStationData.find({'station':'Dewie','date':'2022-12-13'}).limit(1)
    cursor14 = db.WeatherStationData.find({'station':'Dewie','date':'2022-12-14'}).limit(1)

    
    # Get sensor readings for sensor and choose the most recent entry with index "0"
    list_1Dewie = list(cursor1)
    list_2Dewie = list(cursor2)
    list_3Dewie = list(cursor3)
    list_4Dewie = list(cursor4)
    list_5Dewie = list(cursor5)
    list_6Dewie = list(cursor6)
    list_7Dewie = list(cursor7)
    list_8Dewie = list(cursor8)
    list_9Dewie = list(cursor9)
    list_10Dewie = list(cursor10)
    list_11Dewie = list(cursor11)
    list_12Dewie = list(cursor12)
    list_13Dewie = list(cursor13)
    list_14Dewie = list(cursor14)


    

    
    return render_template('Monthly.html', Dewie1=list_1Dewie,  Dewie2=list_2Dewie, Dewie3=list_3Dewie, Dewie4 = list_4Dewie, Dewie5=list_5Dewie,Dewie6=list_6Dewie, Dewie7=list_7Dewie, Dewie8=list_8Dewie, Dewie9=list_9Dewie,Dewie10=list_10Dewie,Dewie11=list_11Dewie,Dewie12=list_12Dewie,Dewie13=list_13Dewie,Dewie14=list_14Dewie)
   

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
