# coding=utf-8

from bokeh.io import curdoc
from bokeh.layouts import row , gridplot, widgetbox, layout
from bokeh.models import ColumnDataSource, HoverTool, Label, LabelSet, CDSView, IndexFilter
from bokeh.plotting import figure
import pandas as pd
from pandas import DataFrame, read_csv
import json
from bokeh.driving import count
import time
import random
from collections import deque
from bokeh.models.widgets import DataTable,TableColumn, HTMLTemplateFormatter,Dropdown, Slider, Div, Button
from bokeh.models.callbacks import CustomJS
import serial
import sqlite3 as lite
from time import strftime
from time import sleep
import threading
import memcache

#------ Read Json Configs --------------------

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

sensor1_enable = (json_config_1['sensor_enable'])
sensor2_enable = (json_config_2['sensor_enable'])
sensor3_enable = (json_config_3['sensor_enable'])
sensor4_enable = (json_config_4['sensor_enable'])
sensor5_enable = (json_config_5['sensor_enable'])
sensor6_enable = (json_config_6['sensor_enable'])
sensor7_enable = (json_config_7['sensor_enable'])
sensor8_enable = (json_config_8['sensor_enable'])
sensor9_enable = (json_config_9['sensor_enable'])
sensor10_enable = (json_config_10['sensor_enable'])
sensor11_enable = (json_config_11['sensor_enable'])
sensor12_enable = (json_config_12['sensor_enable'])
sensor13_enable = (json_config_13['sensor_enable'])
sensor14_enable = (json_config_14['sensor_enable'])
sensor15_enable = (json_config_15['sensor_enable'])
sensor16_enable = (json_config_16['sensor_enable'])
livedata_delay0 = int(json_config_1['livedata_delay'])  * 1000
#historydata_delay0 = int(json_config_1['historydata_delay'] * 1000 * 60 )

# ------------- Fetch Sensor Data from memcache --------------------
def data():
    while True:
        try:
            data_from_sensors = memcache.Client(['127.0.0.1:11211'], debug=0)
            global sensor1_data
            global sensor2_data   
            global sensor3_data   
            global sensor4_data
            global sensor5_data   
            global sensor6_data
            global sensor7_data
            global sensor8_data   
            global sensor9_data   
            global sensor10_data
            global sensor11_data   
            global sensor12_data
            global sensor13_data   
            global sensor14_data
            global sensor15_data   
            global sensor16_data                        
            sensor1_data = data_from_sensors.get('sensor1')
            sensor2_data = data_from_sensors.get('sensor2')
            sensor3_data = data_from_sensors.get('sensor3')
            sensor4_data = data_from_sensors.get('sensor4')
            sensor5_data = data_from_sensors.get('sensor5')
            sensor6_data = data_from_sensors.get('sensor6')
            sensor7_data = data_from_sensors.get('sensor7')
            sensor8_data = data_from_sensors.get('sensor8')
            sensor9_data = data_from_sensors.get('sensor9')
            sensor10_data = data_from_sensors.get('sensor10')
            sensor11_data = data_from_sensors.get('sensor11')
            sensor12_data = data_from_sensors.get('sensor12')
            sensor13_data = data_from_sensors.get('sensor13')
            sensor14_data = data_from_sensors.get('sensor14')
            sensor15_data = data_from_sensors.get('sensor15')
            sensor16_data = data_from_sensors.get('sensor16')
            sleep(livedata_delay0/1000)
        except:
            continue

#  --- Start data function to background -----------

db_data = threading.Thread(target=data)
db_data.start()

# -----------------------------------------------------------------------

# --- Variables -------------------------------

# --- Fetch Variables from JSONs  --------------------

y_scale_min0 = int(json_config_1['y_scale_min'])
y_scale_max0 = int(json_config_1['y_scale_max'])
line_width0 = int(json_config_1['line_width'])
y_size0 = int(json_config_1['y_size'])
x_size0 = int(json_config_1['x_size'])
graph_color0 = (json_config_1['graph_color'])
graph_type0 = (json_config_1['graph_type'])

y_scale_min1 = int(json_config_2['y_scale_min'])
y_scale_max1 = int(json_config_2['y_scale_max'])
line_width1 = int(json_config_2['line_width'])
y_size1 = int(json_config_2['y_size'])
x_size1 = int(json_config_2['x_size'])
historydata_delay1 = int(json_config_2['historydata_delay'])
livedata_delay1 = int(json_config_2['livedata_delay'])
graph_color1 = (json_config_2['graph_color'])
graph_type1 = (json_config_2['graph_type'])

y_scale_min2 = int(json_config_3['y_scale_min'])
y_scale_max2 = int(json_config_3['y_scale_max'])
line_width2 = int(json_config_3['line_width'])
y_size2 = int(json_config_3['y_size'])
x_size2 = int(json_config_3['x_size'])
historydata_delay2 = int(json_config_3['historydata_delay'])
livedata_delay2 = int(json_config_3['livedata_delay'])
graph_color2 = (json_config_3['graph_color'])
graph_type2 = (json_config_3['graph_type'])

y_scale_min3 = int(json_config_4['y_scale_min'])
y_scale_max3 = int(json_config_4['y_scale_max'])
line_width3 = int(json_config_4['line_width'])
y_size3 = int(json_config_4['y_size'])
x_size3 = int(json_config_4['x_size'])
historydata_delay3 = int(json_config_4['historydata_delay'])
livedata_delay3 = int(json_config_4['livedata_delay'])
graph_color3 = (json_config_4['graph_color'])
graph_type3 = (json_config_4['graph_type'])

y_scale_min4 = int(json_config_5['y_scale_min'])
y_scale_max4 = int(json_config_5['y_scale_max'])
line_width4 = int(json_config_5['line_width'])
y_size4 = int(json_config_5['y_size'])
x_size4 = int(json_config_5['x_size'])
historydata_delay4 = int(json_config_5['historydata_delay'])
livedata_delay4 = int(json_config_5['livedata_delay'])
graph_color4 = (json_config_5['graph_color'])
graph_type4 = (json_config_5['graph_type'])

y_scale_min5 = int(json_config_6['y_scale_min'])
y_scale_max5 = int(json_config_6['y_scale_max'])
line_width5 = int(json_config_6['line_width'])
y_size5 = int(json_config_6['y_size'])
x_size5 = int(json_config_6['x_size'])
historydata_delay5 = int(json_config_6['historydata_delay'])
livedata_delay5 = int(json_config_6['livedata_delay'])
graph_color5 = (json_config_6['graph_color'])
graph_type5 = (json_config_6['graph_type'])

y_scale_min6 = int(json_config_7['y_scale_min'])
y_scale_max6 = int(json_config_7['y_scale_max'])
line_width6 = int(json_config_7['line_width'])
y_size6 = int(json_config_7['y_size'])
x_size6 = int(json_config_7['x_size'])
historydata_delay6 = int(json_config_7['historydata_delay'])
livedata_delay6 = int(json_config_7['livedata_delay'])
graph_color6 = (json_config_7['graph_color'])
graph_type6 = (json_config_7['graph_type'])

y_scale_min7 = int(json_config_8['y_scale_min'])
y_scale_max7 = int(json_config_8['y_scale_max'])
line_width7 = int(json_config_8['line_width'])
y_size7 = int(json_config_8['y_size'])
x_size7 = int(json_config_8['x_size'])
historydata_delay7 = int(json_config_8['historydata_delay'])
livedata_delay7 = int(json_config_8['livedata_delay'])
graph_color7 = (json_config_8['graph_color'])
graph_type7 = (json_config_8['graph_type'])

y_scale_min8 = int(json_config_9['y_scale_min'])
y_scale_max8 = int(json_config_9['y_scale_max'])
line_width8 = int(json_config_9['line_width'])
y_size8 = int(json_config_9['y_size'])
x_size8 = int(json_config_9['x_size'])
historydata_delay8 = int(json_config_9['historydata_delay'])
livedata_delay8 = int(json_config_9['livedata_delay'])
graph_color8 = (json_config_9['graph_color'])
graph_type8 = (json_config_9['graph_type'])

y_scale_min9 = int(json_config_10['y_scale_min'])
y_scale_max9 = int(json_config_10['y_scale_max'])
line_width9 = int(json_config_10['line_width'])
y_size9 = int(json_config_10['y_size'])
x_size9 = int(json_config_10['x_size'])
historydata_delay9 = int(json_config_10['historydata_delay'])
livedata_delay9 = int(json_config_10['livedata_delay'])
graph_color9 = (json_config_10['graph_color'])
graph_type9 = (json_config_10['graph_type'])

y_scale_min10 = int(json_config_11['y_scale_min'])
y_scale_max10 = int(json_config_11['y_scale_max'])
line_width10 = int(json_config_11['line_width'])
y_size10 = int(json_config_11['y_size'])
x_size10 = int(json_config_11['x_size'])
historydata_delay10 = int(json_config_11['historydata_delay'])
livedata_delay10 = int(json_config_11['livedata_delay'])
graph_color10 = (json_config_11['graph_color'])
graph_type10 = (json_config_11['graph_type'])

y_scale_min11 = int(json_config_12['y_scale_min'])
y_scale_max11 = int(json_config_12['y_scale_max'])
line_width11 = int(json_config_12['line_width'])
y_size11 = int(json_config_12['y_size'])
x_size11 = int(json_config_12['x_size'])
historydata_delay11 = int(json_config_12['historydata_delay'])
livedata_delay11 = int(json_config_12['livedata_delay'])
graph_color11 = (json_config_12['graph_color'])
graph_type11 = (json_config_12['graph_type'])

y_scale_min12 = int(json_config_13['y_scale_min'])
y_scale_max12 = int(json_config_13['y_scale_max'])
line_width12 = int(json_config_13['line_width'])
y_size12 = int(json_config_13['y_size'])
x_size12 = int(json_config_13['x_size'])
historydata_delay12 = int(json_config_13['historydata_delay'])
livedata_delay12 = int(json_config_13['livedata_delay'])
graph_color12 = (json_config_13['graph_color'])
graph_type12 = (json_config_13['graph_type'])

y_scale_min13 = int(json_config_14['y_scale_min'])
y_scale_max13 = int(json_config_14['y_scale_max'])
line_width13 = int(json_config_14['line_width'])
y_size13 = int(json_config_14['y_size'])
x_size13 = int(json_config_14['x_size'])
historydata_delay13 = int(json_config_14['historydata_delay'])
livedata_delay13 = int(json_config_14['livedata_delay'])
graph_color13 = (json_config_14['graph_color'])
graph_type13 = (json_config_14['graph_type'])

y_scale_min14 = int(json_config_15['y_scale_min'])
y_scale_max14 = int(json_config_15['y_scale_max'])
line_width14 = int(json_config_15['line_width'])
y_size14 = int(json_config_15['y_size'])
x_size14 = int(json_config_15['x_size'])
historydata_delay14 = int(json_config_15['historydata_delay'])
livedata_delay14 = int(json_config_15['livedata_delay'])
graph_color14 = (json_config_15['graph_color'])
graph_type14 = (json_config_15['graph_type'])

y_scale_min15 = int(json_config_16['y_scale_min'])
y_scale_max15 = int(json_config_16['y_scale_max'])
line_width15 = int(json_config_16['line_width'])
y_size15 = int(json_config_16['y_size'])
x_size15 = int(json_config_16['x_size'])
historydata_delay15 = int(json_config_16['historydata_delay'])
livedata_delay15 = int(json_config_16['livedata_delay'])
graph_color15 = (json_config_16['graph_color'])
graph_type15 = (json_config_16['graph_type'])





y = deque(11*[0],10)											# 1-Graafin y-muuttuja 10 lukuinen FIFO Lista
x = list(range(10))												# 1-Graafin x-muuttuja lista 0-10
y2 = deque(11*[0],10)											# 2-Graafin y-muuttuja 10 lukuinen FIFO Lista
x2 = list(range(10))											# 2-Graafin x-muuttuja lista 0-10
y3 = deque(11*[0],10)											# 3-Graafin y-muuttuja 10 lukuinen FIFO Lista
x3 = list(range(10))											# 3-Graafin x-muuttuja lista 0-10
y4 = deque(11*[0],10)											# 4-Graafin y-muuttuja 10 lukuinen FIFO Lista
x4 = list(range(10))											# 4-Graafin x-muuttuja lista 0-10
y5 = deque(11*[0],10)											# 5-Graafin y-muuttuja 10 lukuinen FIFO Lista
x5 = list(range(10))											# 5-Graafin x-muuttuja lista 0-10
y6 = deque(11*[0],10)											# 6-Graafin y-muuttuja 10 lukuinen FIFO Lista
x6 = list(range(10))											# 6-Graafin x-muuttuja lista 0-10
y7 = deque(11*[0],10)											# 7-Graafin y-muuttuja 10 lukuinen FIFO Lista
x7 = list(range(10))											# 7-Graafin x-muuttuja lista 0-10
y8 = deque(11*[0],10)											# 8-Graafin y-muuttuja 10 lukuinen FIFO Lista
x8 = list(range(10))											# 8-Graafin x-muuttuja lista 0-10
y9 = deque(11*[0],10)											# 9-Graafin y-muuttuja 10 lukuinen FIFO Lista
x9 = list(range(10))											# 9-Graafin x-muuttuja lista 0-10
y10 = deque(11*[0],10)											# 10-Graafin y-muuttuja 10 lukuinen FIFO Lista
x10 = list(range(10))											# 10-Graafin x-muuttuja lista 0-10
y11 = deque(11*[0],10)											# 11-Graafin y-muuttuja 10 lukuinen FIFO Lista
x11 = list(range(10))											# 11-Graafin x-muuttuja lista 0-10
y12 = deque(11*[0],10)											# 12-Graafin y-muuttuja 10 lukuinen FIFO Lista
x12 = list(range(10))											# 12-Graafin x-muuttuja lista 0-10
y13 = deque(11*[0],10)											# 13-Graafin y-muuttuja 10 lukuinen FIFO Lista
x13 = list(range(10))											# 13-Graafin x-muuttuja lista 0-10
y14 = deque(11*[0],10)											# 14-Graafin y-muuttuja 10 lukuinen FIFO Lista
x14 = list(range(10))											# 14-Graafin x-muuttuja lista 0-10
y15 = deque(11*[0],10)											# 15-Graafin y-muuttuja 10 lukuinen FIFO Lista
x15 = list(range(10))											# 15-Graafin x-muuttuja lista 0-10
y16 = deque(11*[0],10)											# 16-Graafin y-muuttuja 10 lukuinen FIFO Lista
x16 = list(range(10))											# 16-Graafin x-muuttuja lista 0-10




xxx = list(range(1))											# 1-Graafin x-muuttuja lista (1-Luku) 
yyy = deque(1*[0],1)											# 1-Graafin y-muuttuja FIFO Lista (1-luku)
xxx2 = list(range(1))											# 2-Graafin x-muuttuja lista (1-Luku) 
yyy2 = deque(1*[0],1)											# 2-Graafin y-muuttuja FIFO Lista (1-luku)
xxx3 = list(range(1))											# 3-Graafin x-muuttuja lista (1-Luku) 
yyy3 = deque(1*[0],1)											# 3-Graafin y-muuttuja FIFO Lista (1-luku)
xxx4 = list(range(1))											# 4-Graafin x-muuttuja lista (1-Luku) 
yyy4 = deque(1*[0],1)											# 4-Graafin y-muuttuja FIFO Lista (1-luku)
xxx5 = list(range(1))											# 5-Graafin x-muuttuja lista (1-Luku) 
yyy5 = deque(1*[0],1)											# 5-Graafin y-muuttuja FIFO Lista (1-luku)
xxx6 = list(range(1))											# 6-Graafin x-muuttuja lista (1-Luku) 
yyy6 = deque(1*[0],1)											# 6-Graafin y-muuttuja FIFO Lista (1-luku)
xxx7 = list(range(1))											# 7-Graafin x-muuttuja lista (1-Luku) 
yyy7 = deque(1*[0],1)											# 7-Graafin y-muuttuja FIFO Lista (1-luku)
xxx8 = list(range(1))											# 8-Graafin x-muuttuja lista (1-Luku) 
yyy8 = deque(1*[0],1)											# 8-Graafin y-muuttuja FIFO Lista (1-luku)
xxx9 = list(range(1))											# 9-Graafin x-muuttuja lista (1-Luku) 
yyy9 = deque(1*[0],1)											# 9-Graafin y-muuttuja FIFO Lista (1-luku)
xxx10 = list(range(1))											# 10-Graafin x-muuttuja lista (1-Luku) 
yyy10 = deque(1*[0],1)											# 10-Graafin y-muuttuja FIFO Lista (1-luku)
xxx11 = list(range(1))											# 11-Graafin x-muuttuja lista (1-Luku) 
yyy11 = deque(1*[0],1)											# 11-Graafin y-muuttuja FIFO Lista (1-luku)
xxx12 = list(range(1))											# 12-Graafin x-muuttuja lista (1-Luku) 
yyy12 = deque(1*[0],1)											# 12-Graafin y-muuttuja FIFO Lista (1-luku)
xxx13 = list(range(1))											# 13-Graafin x-muuttuja lista (1-Luku) 
yyy13 = deque(1*[0],1)											# 13-Graafin y-muuttuja FIFO Lista (1-luku)
xxx14 = list(range(1))											# 14-Graafin x-muuttuja lista (1-Luku) 
yyy14 = deque(1*[0],1)											# 14-Graafin y-muuttuja FIFO Lista (1-luku)
xxx15 = list(range(1))											# 15 Graafin x-muuttuja lista (1-Luku) 
yyy15 = deque(1*[0],1)											# 15-Graafin y-muuttuja FIFO Lista (1-luku)
xxx16 = list(range(1))											# 16-Graafin x-muuttuja lista (1-Luku) 
yyy16 = deque(1*[0],1)											# 16-Graafin y-muuttuja FIFO Lista (1-luku)


aika1 = list(range(1))											#  Variable To Time
aika = deque(1*[0],1)											#  Variable To Time


#------ Function To Time -----
def time():
    aika = [strftime("%Y-%m-%d %H:%M:%S")]
    #print(aika)
    return dict(x=aika, y=aika1)
#---------------------------

#------Functions to Bar Graph----
def dada1():
    yyy = [y[0]]												# Select Last Number Of Y-FIFO
    value = y[0]												# Change Last Number Of Y-FIFO to String
    aika = strftime("%Y-%m-%d %H:%M:%S")						# Time For Database
    return dict(x=xxx, y=yyy)									# Return Updated X and Y Data

def dada2():
    yyy2 = [y2[0]]
    value = y2[0]
    aika = strftime("%Y-%m-%d %H:%M:%S")
    return dict(x=xxx2, y=yyy2) 

def dada3():
    yyy3 = [y3[0]]
    value = y3[0]
    aika = strftime("%Y-%m-%d %H:%M:%S")
    return dict(x=xxx3, y=yyy3)
    
def dada4():
    yyy4 = [y4[0]]
    value = y4[0]
    aika = strftime("%Y-%m-%d %H:%M:%S")
    return dict(x=xxx4, y=yyy4)
    
def dada5():
    yyy5 = [y5[0]]
    value = y5[0]
    aika = strftime("%Y-%m-%d %H:%M:%S")
    return dict(x=xxx5, y=yyy5)
    
def dada6():
    yyy6 = [y6[0]]
    value = y6[0]
    aika = strftime("%Y-%m-%d %H:%M:%S")
    return dict(x=xxx6, y=yyy6)

def dada7():
    yyy7 = [y7[0]]
    value = y7[0]
    aika = strftime("%Y-%m-%d %H:%M:%S")
    return dict(x=xxx7, y=yyy7)

def dada8():
    yyy8 = [y8[0]]
    value = y8[0]
    aika = strftime("%Y-%m-%d %H:%M:%S")
    return dict(x=xxx8, y=yyy8)

def dada9():
    yyy9 = [y9[0]]
    value = y9[0]
    aika = strftime("%Y-%m-%d %H:%M:%S")
    return dict(x=xxx9, y=yyy9)
    
def dada10():
    yyy10 = [y10[0]]
    value = y10[0]
    aika = strftime("%Y-%m-%d %H:%M:%S")
    return dict(x=xxx10, y=yyy10)
    
def dada11():
    yyy11 = [y11[0]]
    value = y11[0]
    aika = strftime("%Y-%m-%d %H:%M:%S")
    return dict(x=xxx11, y=yyy11)
    
def dada12():
    yyy12 = [y12[0]]
    value = y12[0]
    aika = strftime("%Y-%m-%d %H:%M:%S")
    return dict(x=xxx12, y=yyy12)
    
def dada13():
    yyy13 = [y13[0]]
    value = y13[0]
    aika = strftime("%Y-%m-%d %H:%M:%S")
    return dict(x=xxx13, y=yyy13)
    
def dada14():
    yyy14 = [y14[0]]
    value = y14[0]
    aika = strftime("%Y-%m-%d %H:%M:%S")
    return dict(x=xxx14, y=yyy14)
    
def dada15():
    yyy15 = [y15[0]]
    value = y15[0]
    aika = strftime("%Y-%m-%d %H:%M:%S")
    return dict(x=xxx15, y=yyy15)
    
def dada16():
    yyy16 = [y16[0]]
    value = y16[0]
    aika = strftime("%Y-%m-%d %H:%M:%S")
    return dict(x=xxx16, y=yyy16)
    

#--------------------------------------------------------------

#------- Functions To Line Graph ----------------------------
def daata1():		
    y.appendleft(sensor1_data)										
    return dict(x=x,y=y)
    
def daata2():
    y2.appendleft(sensor2_data)                       
    return dict(x=x2,y=y2)
    
def daata3():
    y3.appendleft(sensor3_data)                           
    return dict(x=x3,y=y3)
    
def daata4():  
    y4.appendleft(sensor4_data)                         
    return dict(x=x4,y=y4)

def daata5():
    y5.appendleft(sensor5_data)                           
    return dict(x=x5,y=y5)

def daata6():
    y6.appendleft(sensor6_data)                           
    return dict(x=x6,y=y6)
    
def daata7():
    y7.appendleft(sensor7_data)                           
    return dict(x=x7,y=y7)

def daata8():
    y8.appendleft(sensor8_data)                           
    return dict(x=x8,y=y8)
    
def daata9():
    y9.appendleft(sensor9_data)                           
    return dict(x=x9,y=y9)
    
def daata10():
    y10.appendleft(sensor10_data)                           
    return dict(x=x10,y=y10)
    
def daata11():
    y11.appendleft(sensor11_data)                           
    return dict(x=x11,y=y11)
    
def daata12():
    y12.appendleft(sensor12_data)                           
    return dict(x=x12,y=y12)
    
def daata13():
    y13.appendleft(sensor13_data)                           
    return dict(x=x13,y=y13)
    
def daata14():
    y14.appendleft(sensor14_data)                           
    return dict(x=x14,y=y14)
    
def daata15():
    y15.appendleft(sensor15_data)                           
    return dict(x=x15,y=y15)
    
def daata16():
    y16.appendleft(sensor16_data)                           
    return dict(x=x16,y=y16)
#--------------------------------------------------------------

#--------- Make Data to ColumnDataSource For Bokeh -------------------------

source_data1 = ColumnDataSource(data=dict(x=x, y=y))
source_data2 = ColumnDataSource(data=dict(x=x2, y=y2))
source_data3 = ColumnDataSource(data=dict(x=x3, y=y3))
source_data4 = ColumnDataSource(data=dict(x=x4, y=y4))
source_data5 = ColumnDataSource(data=dict(x=x5, y=y5))
source_data6 = ColumnDataSource(data=dict(x=x6, y=y6))
source_data7 = ColumnDataSource(data=dict(x=x7, y=y7))
source_data8 = ColumnDataSource(data=dict(x=x8, y=y8))
source_data9 = ColumnDataSource(data=dict(x=x9, y=y9))
source_data10 = ColumnDataSource(data=dict(x=x10, y=y10))
source_data11 = ColumnDataSource(data=dict(x=x11, y=y11))
source_data12 = ColumnDataSource(data=dict(x=x12, y=y12))
source_data13 = ColumnDataSource(data=dict(x=x13, y=y13))
source_data14 = ColumnDataSource(data=dict(x=x14, y=y14))
source_data15 = ColumnDataSource(data=dict(x=x15, y=y15))
source_data16 = ColumnDataSource(data=dict(x=x16, y=y16))

source_data17 = ColumnDataSource(data=dict(x=xxx, y=yyy))
source_data18 = ColumnDataSource(data=dict(x=xxx2, y=yyy2))
source_data19 = ColumnDataSource(data=dict(x=xxx3, y=yyy3))
source_data20 = ColumnDataSource(data=dict(x=xxx4, y=yyy4))
source_data21 = ColumnDataSource(data=dict(x=xxx5, y=yyy5))
source_data22 = ColumnDataSource(data=dict(x=xxx6, y=yyy6))
source_data23 = ColumnDataSource(data=dict(x=xxx7, y=yyy7))
source_data24 = ColumnDataSource(data=dict(x=xxx8, y=yyy8))
source_data25 = ColumnDataSource(data=dict(x=xxx9, y=yyy9))
source_data26 = ColumnDataSource(data=dict(x=xxx10, y=yyy10))
source_data27 = ColumnDataSource(data=dict(x=xxx11, y=yyy11))
source_data28 = ColumnDataSource(data=dict(x=xxx12, y=yyy12))
source_data29 = ColumnDataSource(data=dict(x=xxx13, y=yyy13))
source_data30 = ColumnDataSource(data=dict(x=xxx14, y=yyy14))
source_data31 = ColumnDataSource(data=dict(x=xxx15, y=yyy15))
source_data32 = ColumnDataSource(data=dict(x=xxx16, y=yyy16))


source_data40 = ColumnDataSource(data=dict(x=aika, y=aika1))

#------------------------------------------------------------------------------------

def graafit(sensor_number_enable, graph_type_number, graph_number, title, y_range_min, y_range_max, plot_height_nro, plot_width_nro, line_width_nro, source_data_line, source_data_bar, line_color_):
    global y_scale_max6   
    if (sensor_number_enable == "yes" and graph_type_number == "Line"):
        graph_number = figure(title=title, y_range=((y_range_min), (y_range_max)), plot_height=plot_height_nro, plot_width=plot_width_nro)
        graph_number.line(line_width=line_width_nro, source = source_data_line,x='x',y='y', line_color=line_color_)
        graph_number.sizing_mode = 'scale_width'
        labels = LabelSet(x=10, y=10, text='y', y_units='screen', x_units='screen', level='glyph', source=source_data_bar)
        graph_number.add_layout(labels)
        print (y_range_max)
    elif (sensor_number_enable == "yes" and graph_type_number == "Bar"):
        graph_number = figure(title=title, y_range=((y_range_min), (y_range_max)), plot_height=plot_height_nro, plot_width=plot_width_nro)
        graph_number.vbar(width='x', source = source_data_bar,x='y', color=line_color_, top='y', line_width=line_width_nro)
        graph_number.sizing_mode = 'scale_width'
        labels = LabelSet(x=10, y=10, text='y', y_units='screen', x_units='screen', level='glyph', source=source_data_bar)
        graph_number.add_layout(labels)
        graph_number.xaxis.visible = False
    elif (sensor_number_enable == "no"):
        graph_number = figure(plot_height=0, plot_width=0)
        graph_number.axis.visible = False
        graph_number.grid.visible = False
        graph_number.background_fill_color = None
        graph_number.border_fill_color = None
        graph_number.outline_line_color = None
    return graph_number
    
graph1 = graafit(sensor1_enable, graph_type0, 'graph1', 'Temperature', y_scale_min0, y_scale_max0, y_size0, x_size0, line_width0, source_data1, source_data17, graph_color0)
graph2 = graafit(sensor2_enable, graph_type1, 'graph2', 'Humidity', y_scale_min1, y_scale_max1, y_size1, x_size1, line_width1, source_data2, source_data18, graph_color1) 
graph3 = graafit(sensor3_enable, graph_type2, 'graph3', 'Pressure', y_scale_min2, y_scale_max2, y_size2, x_size2, line_width2, source_data3, source_data19, graph_color2) 
graph4 = graafit(sensor4_enable, graph_type3, 'graph4', 'Not_Connected', y_scale_min3, y_scale_max3, y_size3, x_size3, line_width3, source_data4, source_data20, graph_color3) 
graph5 = graafit(sensor5_enable, graph_type4, 'graph5', 'Temperature2', y_scale_min4, y_scale_max4, y_size4, x_size4, line_width4, source_data5, source_data21, graph_color4) 
graph6 = graafit(sensor6_enable, graph_type5, 'graph6', 'Not_connected', y_scale_min5, y_scale_max5, y_size5, x_size5, line_width5, source_data6, source_data22, graph_color5) 
graph7 = graafit(sensor7_enable, graph_type6, 'graph7', 'Pressure2', y_scale_min6, y_scale_max6, y_size6, x_size6, line_width6, source_data7, source_data23, graph_color6) 
graph8 = graafit(sensor8_enable, graph_type7, 'graph8', 'Not_connected', y_scale_min7, y_scale_max7, y_size7, x_size7, line_width7, source_data8, source_data24, graph_color7)
graph9 = graafit(sensor9_enable, graph_type8, 'graph9', 'Sensor9', y_scale_min8, y_scale_max8, y_size8, x_size8, line_width8, source_data9, source_data25, graph_color8)
graph10 = graafit(sensor10_enable, graph_type9, 'graph10', 'Humidity2"', y_scale_min9, y_scale_max9, y_size9, x_size9, line_width9, source_data10, source_data26, graph_color9) 
graph11 = graafit(sensor11_enable, graph_type10, 'graph11', 'Sensor11', y_scale_min10, y_scale_max10, y_size10, x_size10, line_width10, source_data11, source_data27, graph_color10) 
graph12 = graafit(sensor12_enable, graph_type11, 'graph12', 'Sensor12', y_scale_min11, y_scale_max11, y_size11, x_size11, line_width11, source_data12, source_data28, graph_color11) 
graph13 = graafit(sensor13_enable, graph_type12, 'graph13', 'Sensor13', y_scale_min12, y_scale_max12, y_size12, x_size12, line_width12, source_data13, source_data29, graph_color12) 
graph14 = graafit(sensor14_enable, graph_type13, 'graph14', 'Sensor14', y_scale_min13, y_scale_max13, y_size13, x_size13, line_width13, source_data14, source_data30, graph_color13) 
graph15 = graafit(sensor15_enable, graph_type14, 'graph15', 'Sensor15', y_scale_min14, y_scale_max14, y_size14, x_size14, line_width14, source_data15, source_data31, graph_color14)
graph16 = graafit(sensor16_enable, graph_type15, 'graph16', 'Sensor16', y_scale_min15, y_scale_max15, y_size15, x_size15, line_width15, source_data16, source_data32, graph_color15)  
          

# --- Time graph ----

graph20 = figure(x_axis_type='datetime', title="Systemtime", y_range=(0, 7), plot_height=60, plot_width=220)
piilotettava = graph20.vbar(width = 1, source = source_data40, x='y', color="blue", top='y', line_width=15)							# Tehdään graafista muuttuja joka voidaan piilottaa..
#graph20.sizing_mode = 'scale_width'
labels = LabelSet(x=8, y=8, text='x', y_units='screen', x_units='screen', level='glyph', source=source_data40)
graph20.add_layout(labels)
graph20.xgrid.grid_line_color = None 				# Piilotetaan x-grid
graph20.ygrid.grid_line_color = None				# Piilotetaan y-grid
piilotettava.visible = False						# Piilotetaan Graafi
graph20.xaxis.visible = False						# Piilotetaan x-akseli
graph20.yaxis.visible = False						# Piilotetaan y-akseli
#------------------------------------------------------------------------------------------------------------



grid = gridplot([[graph20],[graph1, graph2, graph3, graph4], [ graph5, graph6, graph7, graph8], [graph9, graph10, graph11, graph12], [graph13, graph14, graph15, graph16]], toolbar_location=None) #, plot_width=1000, plot_height=1000)

#------------ Show The Graphs ----------------------------------------------------------------------

curdoc().add_root(row(grid))
curdoc().title = "JMS"
# --------------------------------------------

# ----------- Updates ... --------------------
@count()
def update(t):
    if (sensor1_enable):
        source_data1.data = daata1()
        source_data17.data = dada1()
    if (sensor2_enable):
        source_data2.data = daata2()
        source_data18.data = dada2()
    if (sensor3_enable):
        source_data3.data = daata3()
        source_data19.data = dada3()
    if (sensor4_enable):
        source_data4.data = daata4()
        source_data20.data = dada4()
    if (sensor5_enable):
        source_data5.data = daata5()
        source_data21.data = dada5()
    if (sensor6_enable):
        source_data6.data = daata6()
        source_data22.data = dada6()
    if (sensor7_enable):
        source_data7.data = daata7()
        source_data23.data = dada7()
    if (sensor8_enable):
        source_data8.data = daata8()
        source_data24.data = dada8()
    if (sensor9_enable):
        source_data9.data = daata9()
        source_data25.data = dada9()
    if (sensor10_enable):
        source_data10.data = daata10()
        source_data26.data = dada10()
    if (sensor11_enable):
        source_data11.data = daata11()
        source_data27.data = dada11()
    if (sensor12_enable):
        source_data12.data = daata12()
        source_data28.data = dada12()
    if (sensor13_enable):
        source_data13.data = daata13()
        source_data29.data = dada13()
    if (sensor14_enable):
        source_data14.data = daata14()
        source_data30.data = dada14()
    if (sensor15_enable):
        source_data15.data = daata15()
        source_data31.data = dada15()
    if (sensor16_enable):
        source_data16.data = daata16()
        source_data32.data = dada16()
    

    
@count()
def update_time(t):
    source_data40.data = time()


curdoc().add_periodic_callback(update, livedata_delay0) # Update in milliseconds
curdoc().add_periodic_callback(update_time, 1000) # Clock Update Every Second
curdoc().title = "JMS"
#------------------------------------------------------------------------------------------------------------