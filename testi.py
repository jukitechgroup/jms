import csv
import time
from time import strftime
import sqlite3 as lite

def hae_databasesta():
    con = lite.connect('/home/jukka/jms/jms/templates/measure.db')
    cur = con.cursor()
    data = cur.execute("SELECT aika, value FROM Measure1")
    with open ('out.csv', 'wb') as f:
        writer = csv.writer(f)
        writer.writerow(['aika', 'value'])
        writer.writerows(data)
        f.close
        
hae_databasesta()