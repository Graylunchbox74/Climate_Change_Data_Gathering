import requests
from scipy import misc
from io import BytesIO
import json
import sqlite3
import datetime
#from matplotlib import pyplot as plt
#import numpy as np
conn = sqlite3.connect('weather.db')
db = conn.cursor()
key =""
#          https://api.darksky.net/forecast/[key]/[latitude],[longitude],[time]
for time in range (0, 1523768400, 86400):
    URL = "https://api.darksky.net/forecast/" + key + "/44.071071, -103.217924," + str(time) +"?exclude=hourly,currently,minutely,alerts,flags"
    try:
        r = requests.get(url=URL)
        strDate = datetime.datetime.fromtimestamp(time).strftime('%Y-%m-%d')
        data = r.json()
        #(day varchar[14], temperatureMin float, temperatureMax float, precipProbability float, precipAccumulation float, precipType text, pressure float, humidity float, windSpeed float, visibility float, cloudCover float);
        executeString = "INSERT INTO rapidCitySD (day,temperatureMin,temperatureMax,precipProbability,pressure,humidity,windSpeed,visibility) values(\""+strDate +"\","+ str(data["daily"]["data"][0]["temperatureMin"])+","+ str(data["daily"]["data"][0]["temperatureMax"]) +","+ str(data["daily"]["data"][0]["precipProbability"]) +","+ str(data["daily"]["data"][0]["pressure"]) +","+ str(data["daily"]["data"][0]["humidity"]) +","+ str(data["daily"]["data"][0]["windSpeed"]) +","+ str(data["daily"]["data"][0]["visibility"]) +")"
        print(executeString)
        db.execute(executeString)
        conn.commit()
    except:
        print("url: ", URL ,"does not exist")
for time in range (0, 1523768400, 86400):
    URL = "https://api.darksky.net/forecast/" + key + "/44.375163, -100.319996," + str(time) +"?exclude=hourly,currently,minutely,alerts,flags"
    try:
        r = requests.get(url=URL)
        strDate = datetime.datetime.fromtimestamp(time).strftime('%Y-%m-%d')
        data = r.json()
        #(day varchar[14], temperatureMin float, temperatureMax float, precipProbability float, precipAccumulation float, precipType text, pressure float, humidity float, windSpeed float, visibility float, cloudCover float);
        executeString = "INSERT INTO pierreSD (day,temperatureMin,temperatureMax,precipProbability,pressure,humidity,windSpeed,visibility) values(\""+strDate +"\","+ str(data["daily"]["data"][0]["temperatureMin"])+","+ str(data["daily"]["data"][0]["temperatureMax"]) +","+ str(data["daily"]["data"][0]["precipProbability"]) +","+ str(data["daily"]["data"][0]["pressure"]) +","+ str(data["daily"]["data"][0]["humidity"]) +","+ str(data["daily"]["data"][0]["windSpeed"]) +","+ str(data["daily"]["data"][0]["visibility"]) +")"
        print(executeString)
        db.execute(executeString)
        conn.commit()
    except:
        print("url: ", URL ,"does not exist")
for time in range (0, 1523768400, 86400):
    URL = "https://api.darksky.net/forecast/" + key + "/44.375163, -100.319996," + str(time) +"?exclude=hourly,currently,minutely,alerts,flags"
    try:
        r = requests.get(url=URL)
        strDate = datetime.datetime.fromtimestamp(time).strftime('%Y-%m-%d')
        data = r.json()
        #(day varchar[14], temperatureMin float, temperatureMax float, precipProbability float, precipAccumulation float, precipType text, pressure float, humidity float, windSpeed float, visibility float, cloudCover float);
        executeString = "INSERT INTO pierreSD (day,temperatureMin,temperatureMax,precipProbability,pressure,humidity,windSpeed,visibility) values(\""+strDate +"\","+ str(data["daily"]["data"][0]["temperatureMin"])+","+ str(data["daily"]["data"][0]["temperatureMax"]) +","+ str(data["daily"]["data"][0]["precipProbability"]) +","+ str(data["daily"]["data"][0]["pressure"]) +","+ str(data["daily"]["data"][0]["humidity"]) +","+ str(data["daily"]["data"][0]["windSpeed"]) +","+ str(data["daily"]["data"][0]["visibility"]) +")"
        print(executeString)
        db.execute(executeString)
        conn.commit()
    except:
        print("url: ", URL ,"does not exist")
for time in range (0, 1523768400, 86400):
    URL = "https://api.darksky.net/forecast/" + key + "/44.302416, -96.785336," + str(time) +"?exclude=hourly,currently,minutely,alerts,flags"
    try:
        r = requests.get(url=URL)
        strDate = datetime.datetime.fromtimestamp(time).strftime('%Y-%m-%d')
        data = r.json()
        #(day varchar[14], temperatureMin float, temperatureMax float, precipProbability float, precipAccumulation float, precipType text, pressure float, humidity float, windSpeed float, visibility float, cloudCover float);
        executeString = "INSERT INTO brookingsSD (day,temperatureMin,temperatureMax,precipProbability,pressure,humidity,windSpeed,visibility) values(\""+strDate +"\","+ str(data["daily"]["data"][0]["temperatureMin"])+","+ str(data["daily"]["data"][0]["temperatureMax"]) +","+ str(data["daily"]["data"][0]["precipProbability"]) +","+ str(data["daily"]["data"][0]["pressure"]) +","+ str(data["daily"]["data"][0]["humidity"]) +","+ str(data["daily"]["data"][0]["windSpeed"]) +","+ str(data["daily"]["data"][0]["visibility"]) +")"
        print(executeString)
        db.execute(executeString)
        conn.commit()
    except:
        print("url: ", URL ,"does not exist")
for time in range (0, 1523768400, 86400):
    URL = "https://api.darksky.net/forecast/" + key + "/44.8994, -97.1151," + str(time) +"?exclude=hourly,currently,minutely,alerts,flags"
    try:
        r = requests.get(url=URL)
        strDate = datetime.datetime.fromtimestamp(time).strftime('%Y-%m-%d')
        data = r.json()
        #(day varchar[14], temperatureMin float, temperatureMax float, precipProbability float, precipAccumulation float, precipType text, pressure float, humidity float, windSpeed float, visibility float, cloudCover float);
        executeString = "INSERT INTO watertownSD (day,temperatureMin,temperatureMax,precipProbability,pressure,humidity,windSpeed,visibility) values(\""+strDate +"\","+ str(data["daily"]["data"][0]["temperatureMin"])+","+ str(data["daily"]["data"][0]["temperatureMax"]) +","+ str(data["daily"]["data"][0]["precipProbability"]) +","+ str(data["daily"]["data"][0]["pressure"]) +","+ str(data["daily"]["data"][0]["humidity"]) +","+ str(data["daily"]["data"][0]["windSpeed"]) +","+ str(data["daily"]["data"][0]["visibility"]) +")"
        print(executeString)
        db.execute(executeString)
        conn.commit()
    except:
        print("url: ", URL ,"does not exist")
conn.close()
