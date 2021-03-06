from flask import render_template, url_for, request, send_from_directory
from jms import jms #, socketio
import csv
import time
import subprocess
from time import strftime
import sqlite3 as lite
import numpy as np
from bokeh.plotting import figure, output_file, show
from bokeh.embed import server_document
import pandas as pd
import json
import psutil
import platform
from threading import Thread
#from json2html import *


#----------------- Variables for maintenance -----------------------------------------------


livetime = strftime("%Y-%m-%d %H:%M:%S")
os = platform.system()
release = platform.release()
utility_levy = psutil.disk_usage('/')
levynkaytto = str(round(utility_levy.free/1024.0/1024.0,1)) + " Mt"
levytiedot = str(round(utility_levy.total/1024.0/1024.0,1)) + "Mt"
netti = psutil.net_io_counters(pernic=True)
nettiosoite = subprocess.check_output(["hostname -I"], shell=True, universal_newlines=True)
gateway = subprocess.check_output(["route -n | grep 'UG[ \t]' | awk '{print $2}'"], shell=True, universal_newlines=True)
subnet = subprocess.check_output(["route -n | grep 'U[ \t]' | awk '{print $3}'"], shell=True, universal_newlines=True)
uptime_aika = subprocess.check_output(['uptime -p'], shell=True, universal_newlines=True)
uptime_kaynnistetty = subprocess.check_output(['uptime -s'], shell=True, universal_newlines=True)
hostname = platform.node()
kokonaismuisti = str(psutil.virtual_memory().total/1024/1024) + " Mt"
vapaamuisti = str(psutil.virtual_memory().free/1024/1024) + " Mt" 
cpu = psutil
percent = cpu.cpu_percent()
processor = str(round(percent)) + '%'

#--------------------------------------------------------------------------------

# -------------------CSV ja Database Variables ----------------------------------

db_dir = '/home/jms/JMS/data/measure.db'
csv1 = '/home/jms/JMS/data/out1.csv'
csv2 = '/home/jms/JMS/data/out2.csv'
csv3 = '/home/jms/JMS/data/out3.csv'
csv4 = '/home/jms/JMS/data/out4.csv'
csv5 = '/home/jms/JMS/data/out5.csv'
csv6 = '/home/jms/JMS/data/out6.csv'
csv7 = '/home/jms/JMS/data/out7.csv'
csv8 = '/home/jms/JMS/data/out8.csv'

#--------------------------------------------------------------------------------

# -----------Data Fetch Functions ------------------------------------------------

def sensor11():
     con = lite.connect(db_dir)
     cur = con.cursor()
     data = cur.execute("SELECT aika,value FROM measure1 WHERE strftime('%Y-%m-%d %H-%M-%S', aika) BETWEEN ? AND ? ",  (pvm1, pvm2)) # Haetaan data
     with open(csv1, 'w') as f:																										 # Avataan csv
            writer = csv.writer(f)																									 #
            writer.writerow(['aika', 'arvo'])																						 # Luodaan header data csv:hen 
            writer.writerows(data)																									 # Luodaan data csv:hen
     con.close()
     return
            
def sensor12():
     con = lite.connect(db_dir)
     cur = con.cursor()
     data = cur.execute("SELECT aika,value FROM measure2 WHERE strftime('%Y-%m-%d %H-%M-%S', aika) BETWEEN ? AND ? ",  (pvm1, pvm2))
     with open(csv2, 'w') as f:
            writer = csv.writer(f)
            writer.writerow(['aika', 'arvo'])
            writer.writerows(data)
     con.close()
     return

def sensor13():
     con = lite.connect(db_dir)
     cur = con.cursor()
     data = cur.execute("SELECT aika,value FROM measure3 WHERE strftime('%Y-%m-%d %H-%M-%S', aika) BETWEEN ? AND ? ",  (pvm1, pvm2))
     with open(csv3, 'w') as f:
            writer = csv.writer(f)
            writer.writerow(['aika', 'arvo'])
            writer.writerows(data)
     con.close()
     return

def sensor14():
     con = lite.connect(db_dir)
     cur = con.cursor()
     data = cur.execute("SELECT aika,value FROM measure4 WHERE strftime('%Y-%m-%d %H-%M-%S', aika) BETWEEN ? AND ? ",  (pvm1, pvm2))
     with open(csv4, 'w') as f:
            writer = csv.writer(f)
            writer.writerow(['aika', 'arvo'])
            writer.writerows(data)
     con.close()
     return

def sensor15():
     con = lite.connect(db_dir)
     cur = con.cursor()
     data = cur.execute("SELECT aika,value FROM measure5 WHERE strftime('%Y-%m-%d %H-%M-%S', aika) BETWEEN ? AND ? ",  (pvm1, pvm2))
     with open(csv5, 'w') as f:
            writer = csv.writer(f)
            writer.writerow(['aika', 'arvo'])
            writer.writerows(data)
     con.close()
     return

def sensor16():
     con = lite.connect(db_dir)
     cur = con.cursor()
     data = cur.execute("SELECT aika,value FROM measure6 WHERE strftime('%Y-%m-%d %H-%M-%S', aika) BETWEEN ? AND ? ",  (pvm1, pvm2))
     with open(csv6, 'w') as f:
            writer = csv.writer(f)
            writer.writerow(['aika', 'arvo'])
            writer.writerows(data)
     con.close()
     return

def sensor17():
     con = lite.connect(db_dir)
     cur = con.cursor()
     data = cur.execute("SELECT aika,value FROM measure7 WHERE strftime('%Y-%m-%d %H-%M-%S', aika) BETWEEN ? AND ? ",  (pvm1, pvm2))
     with open(csv7, 'w') as f:
            writer = csv.writer(f)
            writer.writerow(['aika', 'arvo'])
            writer.writerows(data)
     con.close()
     return

def sensor18():
     con = lite.connect(db_dir)
     cur = con.cursor()
     data = cur.execute("SELECT aika,value FROM measure8 WHERE strftime('%Y-%m-%d %H-%M-%S', aika) BETWEEN ? AND ? ",  (pvm1, pvm2))
     with open(csv8, 'w') as f:
            writer = csv.writer(f)
            writer.writerow(['aika', 'arvo'])
            writer.writerows(data)
     con.close()
     return

# ------------------------------------------------------------------------------

# ---------------Flask Routes Begins ... --------------------------------------------

@jms.route('/')
@jms.route('/index', methods=['GET', 'POST'])
def index():
    return render_template('index.html', title='JMS', livetime=livetime)

@jms.route('/live')
def live():
   script = server_document(url="http://192.168.1.202:5006/live_graph")
   return render_template('live.html',  script = script, title='JMS')

@jms.route('/historia')
def historia():
    return render_template('historiakysely.html', title='JMS', livetime=livetime)


# Select Whitch Sensors Are Shown And Write JSON File From That. history_graph.py Reads This File When it Collects Data.
# We Ask For Dates Here Too..

@jms.route('/graafi', methods=['GET', 'POST'])
def posti():
    if request.method=='POST':      
        global pvm1
        pvm1 = request.form['pvm1']
        global pvm2
        pvm2 = request.form['pvm2']
        sensor1 = 'Sensor1' in request.form
        sensor2 = 'Sensor2' in request.form
        sensor3 = 'Sensor3' in request.form
        sensor4 = 'Sensor4' in request.form
        sensor5 = 'Sensor5' in request.form
        sensor6 = 'Sensor6' in request.form
        sensor7 = 'Sensor7' in request.form
        sensor8 = 'Sensor8' in request.form
        
        sensors_enabled = {"sensor1": sensor1,  "sensor2":sensor2, "sensor3":sensor3, "sensor4": sensor4,  "sensor5":sensor5, "sensor6":sensor6,  "sensor7":sensor7, "sensor8":sensor8} #, sensor4, sensor5, sensor6, sensor7, sensor8 ]
        print (sensors_enabled)
         
        with open('/home/jms/JMS/data/sensor_enabled.json', 'w') as f:
              f.write(json.dumps(sensors_enabled))
        
        if (sensor1):
            sensor11()
     
        if (sensor2):
            sensor12()
            
        if (sensor3):
            sensor13()
            
        if (sensor4):
            sensor14()
            
        if (sensor5):
            sensor15()
            
        if (sensor6):
            sensor16()
            
        if (sensor7):
            sensor17()
            
        if (sensor8):
            sensor18()
        
        script = server_document(url="http://192.168.1.202:5006/history_graph") #
    
    return render_template('graafi.html',  pvm1 = pvm1, pvm2 = pvm2, script = script, title='JMS', livetime=livetime)

# ------------------------------------------------------------------------------------    

@jms.route('/yllapito', methods=['GET', 'POST'])
def yllapito():
    if request.method=='POST':
        y_scale_max = request.form['y_scale_max']
        y_scale_min = request.form['y_scale_min']
        line_width = request.form['line_width']
        
        y_size = request.form['y_size']
        x_size = request.form['x_size']
        
        livedata_delay = request.form['livedata_delay']
        historydata_delay = request.form['historydata_delay']
        
        sensor1 = request.form['Sensor1']
        sensor_enabled = request.form['sensor_enabled']
        graph_color = request.form['red']
        graph_type = request.form['Bar']

        def json_configit(Sensor_name, json_path):
            nonlocal y_scale_max
            nonlocal y_scale_min
            nonlocal line_width
            nonlocal y_size
            nonlocal x_size
            nonlocal livedata_delay
            nonlocal historydata_delay
            nonlocal sensor1
            nonlocal sensor_enabled
            nonlocal graph_color
            nonlocal graph_type 
            if (sensor1 == Sensor_name):
                testi = {"sensor_number": sensor1, "sensor_enable": sensor_enabled,  "graph_color": graph_color, "graph_type": graph_type,
                "livedata_delay": livedata_delay, "historydata_delay": historydata_delay, "y_scale_max": y_scale_max, "y_scale_min": y_scale_min,
                "line_width": line_width,"y_size": y_size, "x_size": x_size}
                with open(json_path, 'w') as f:
                    f.write(json.dumps(testi))
                    f.close
                print(testi)
                return testi

        sensor0 = json_configit("Sensor1", '/home/jms/JMS/data/jms_config_1.json')
        sensor2 = json_configit("Sensor2", '/home/jms/JMS/data/jms_config_2.json')
        sensor3 = json_configit("Sensor3", '/home/jms/JMS/data/jms_config_3.json')
        sensor4 = json_configit("Sensor4", '/home/jms/JMS/data/jms_config_4.json')
        sensor5 = json_configit("Sensor5", '/home/jms/JMS/data/jms_config_5.json')
        sensor6 = json_configit("Sensor6", '/home/jms/JMS/data/jms_config_6.json')
        sensor7 = json_configit("Sensor7", '/home/jms/JMS/data/jms_config_7.json')
        sensor8 = json_configit("Sensor8", '/home/jms/JMS/data/jms_config_8.json')
        sensor9 = json_configit("Sensor9", '/home/jms/JMS/data/jms_config_9.json')
        sensor10 = json_configit("Sensor10", '/home/jms/JMS/data/jms_config_10.json')
        sensor11 = json_configit("Sensor11", '/home/jms/JMS/data/jms_config_11.json')
        sensor12 = json_configit("Sensor12", '/home/jms/JMS/data/jms_config_12.json')
        sensor13 = json_configit("Sensor13", '/home/jms/JMS/data/jms_config_13.json')
        sensor14 = json_configit("Sensor14", '/home/jms/JMS/data/jms_config_14.json')
        sensor15 = json_configit("Sensor15", '/home/jms/JMS/data/jms_config_15.json')
        sensor16 = json_configit('Sensor16', '/home/jms/JMS/data/jms_config_16.json')

    def config(json_path):
        with open(json_path, 'r') as f:
            config = json.load(f)
            f.close
            return config
            
    json_config_1 = config('/home/jms/JMS/data/jms_config_1.json')
    json_config_2 = config('/home/jms/JMS/data/jms_config_2.json')
    json_config_3 = config('/home/jms/JMS/data/jms_config_3.json')
    json_config_4 = config('/home/jms/JMS/data/jms_config_4.json')
    json_config_5 = config('/home/jms/JMS/data/jms_config_5.json')
    json_config_6 = config('/home/jms/JMS/data/jms_config_6.json')
    json_config_7 = config('/home/jms/JMS/data/jms_config_7.json')
    json_config_8 = config('/home/jms/JMS/data/jms_config_8.json')
    json_config_9 = config('/home/jms/JMS/data/jms_config_9.json')
    json_config_10 = config('/home/jms/JMS/data/jms_config_10.json')
    json_config_11 = config('/home/jms/JMS/data/jms_config_11.json')
    json_config_12 = config('/home/jms/JMS/data/jms_config_12.json')
    json_config_13 = config('/home/jms/JMS/data/jms_config_13.json')
    json_config_14 = config('/home/jms/JMS/data/jms_config_14.json')
    json_config_15 = config('/home/jms/JMS/data/jms_config_15.json')
    json_config_16 = config('/home/jms/JMS/data/jms_config_16.json')
    print (json_config_16)

        
    return render_template('yllapito.html', os=os, release=release, 
             host=hostname, uptime_aika=uptime_aika, uptime_kaynnistetty=uptime_kaynnistetty,
            processor=processor, netti=netti, nettiosoite=nettiosoite,
            kokonaismuisti=kokonaismuisti, vapaamuisti=vapaamuisti,
            levynkaytto=levynkaytto, levytiedot=levytiedot, gateway=gateway,
            subnet=subnet , title='JMS', livetime=livetime, json_config_1=json_config_1,
            json_config_2=json_config_2, json_config_3=json_config_3, json_config_4=json_config_4,
            json_config_5=json_config_5, json_config_6=json_config_6, json_config_7=json_config_7,
            json_config_8=json_config_8, json_config_9=json_config_9, json_config_10=json_config_10,
            json_config_11=json_config_11, json_config_12=json_config_12, json_config_13=json_config_13,
            json_config_14=json_config_14, json_config_15=json_config_15, json_config_16=json_config_16)
            
# ---------------- Flask routes ends
