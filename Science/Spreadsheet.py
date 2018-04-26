import sqlite3
import pyoo

desktop = pyoo.Desktop('localhost', 2002)

doc = desktop.create_spreadsheet()
doc.sheets[0]
sheet = doc.sheets[0]

sheet[0,0].value = 0
sheet[0,1].value = "Date"
sheet[0,2].value = "Lowest Temp"
sheet[0,3].value = "Highest Temp"
sheet[0,4].value = "PrecipProbability"
sheet[0,5].value = "Pressure"
sheet[0,6].value = "Humidity"
sheet[0,7].value = "Windspeed"
sheet[0,8].value = "Visibility"

y = 1
conn = sqlite3.connect('weather.db')
db = conn.cursor()

for row in db.execute("select * from watertownSD"):
    sheet[y,0].value = y
    sheet[y,1].value = row[0]
    sheet[y,2].value = row[1]
    sheet[y,3].value = row[2]
    sheet[y,4].value = row[3]
    sheet[y,5].value = row[4]
    sheet[y,6].value = row[5]
    sheet[y,7].value = row[6]
    sheet[y,8].value = row[7]
    y +=  1
