# coding=utf-8

from collections import deque
import json
import sqlite3 as lite
from time import strftime
from time import sleep
import threading
import memcache
import minimalmodbus

# --------    Modbus setup  -----------------


def modbus_setup(SlaveNumber, baudrate):
    instrument = minimalmodbus.Instrument('/dev/ttyAMA0', SlaveNumber)  # Port, Slave Address
    instrument.serial.baudrate = baudrate
    return instrument

# -------------------------------------------

# -------------- Config Path Setup ----------------

def config(json_path):
    with open(json_path, 'r') as f:
        config = json.load(f)
        f.close()
        return config

# -------------------------------------------

# ------------- Get config files to variables ----------------------------------

module1 = modbus_setup(1, 9600)
module2 = modbus_setup(2, 9600)

json_config_1 = config('/home/maintenance/jms/jms/data/jms_config_1.json')
json_config_2 = config('/home/maintenance/jms/jms/data/jms_config_2.json')
json_config_3 = config('/home/maintenance/jms/jms/data/jms_config_3.json')
json_config_4 = config('/home/maintenance/jms/jms/data/jms_config_4.json')
json_config_5 = config('/home/maintenance/jms/jms/data/jms_config_5.json')
json_config_6 = config('/home/maintenance/jms/jms/data/jms_config_6.json')
json_config_7 = config('/home/maintenance/jms/jms/data/jms_config_7.json')
json_config_8 = config('/home/maintenance/jms/jms/data/jms_config_8.json')
json_config_9 = config('/home/maintenance/jms/jms/data/jms_config_9.json')
json_config_10 = config('/home/maintenance/jms/jms/data/jms_config_10.json')
json_config_11 = config('/home/maintenance/jms/jms/data/jms_config_11.json')
json_config_12 = config('/home/maintenance/jms/jms/data/jms_config_12.json')
json_config_13 = config('/home/maintenance/jms/jms/data/jms_config_13.json')
json_config_14 = config('/home/maintenance/jms/jms/data/jms_config_14.json')
json_config_15 = config('/home/maintenance/jms/jms/data/jms_config_15.json')
json_config_16 = config('/home/maintenance/jms/jms/data/jms_config_16.json')

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

livedata_delay0 = int(json_config_1['livedata_delay']) * 1000  # livedata_delay in seconds
historydata_delay0 = int(json_config_1['historydata_delay']) * 1000 * 60 # Historydata delay in minutes

# ------------------------------------------------------------------------

# ---------------- Function to check if configs has changed, checks every minute -----

def check_config():
    while True:
        json_config_1 = config('/home/maintenance/jms/jms/data/jms_config_1.json')
        json_config_2 = config('/home/maintenance/jms/jms/data/jms_config_2.json')
        json_config_3 = config('/home/maintenance/jms/jms/data/jms_config_3.json')
        json_config_4 = config('/home/maintenance/jms/jms/data/jms_config_4.json')
        json_config_5 = config('/home/maintenance/jms/jms/data/jms_config_5.json')
        json_config_6 = config('/home/maintenance/jms/jms/data/jms_config_6.json')
        json_config_7 = config('/home/maintenance/jms/jms/data/jms_config_7.json')
        json_config_8 = config('/home/maintenance/jms/jms/data/jms_config_8.json')
        json_config_9 = config('/home/maintenance/jms/jms/data/jms_config_9.json')
        json_config_10 = config('/home/maintenance/jms/jms/data/jms_config_10.json')
        json_config_11 = config('/home/maintenance/jms/jms/data/jms_config_11.json')
        json_config_12 = config('/home/maintenance/jms/jms/data/jms_config_12.json')
        json_config_13 = config('/home/maintenance/jms/jms/data/jms_config_13.json')
        json_config_14 = config('/home/maintenance/jms/jms/data/jms_config_14.json')
        json_config_15 = config('/home/maintenance/jms/jms/data/jms_config_15.json')
        json_config_16 = config('/home/maintenance/jms/jms/data/jms_config_16.json')
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
        sleep(60)

# -------------------------------------------------------------------------------

# ----------------- Start config check to background ----------------------------

config_threat = threading.Thread(target=check_config)
config_threat.start()

# -------------------------------------------------------------------------------

# ------------- Setup sensor FIFO´s and data ------------------------------------

sensor_data_fifo1 = deque(11 * [0], 10)
sensor_data_fifo2 = deque(11 * [0], 10)
sensor_data_fifo3 = deque(11 * [0], 10)
sensor_data_fifo4 = deque(11 * [0], 10)
sensor_data_fifo5 = deque(11 * [0], 10)
sensor_data_fifo6 = deque(11 * [0], 10)
sensor_data_fifo7 = deque(11 * [0], 10)
sensor_data_fifo8 = deque(11 * [0], 10)
sensor_data_fifo9 = deque(11 * [0], 10)
sensor_data_fifo10 = deque(11 * [0], 10)
sensor_data_fifo11 = deque(11 * [0], 10)
sensor_data_fifo12 = deque(11 * [0], 10)
sensor_data_fifo13 = deque(11 * [0], 10)
sensor_data_fifo14 = deque(11 * [0], 10)
sensor_data_fifo15 = deque(11 * [0], 10)
sensor_data_fifo16 = deque(11 * [0], 10)

sensor1_data = 0
sensor2_data = 0
sensor3_data = 0
sensor4_data = 0
sensor5_data = 0
sensor6_data = 0
sensor7_data = 0
sensor8_data = 0
sensor9_data = 0
sensor10_data = 0
sensor11_data = 0
sensor12_data = 0
sensor13_data = 0
sensor14_data = 0
sensor15_data = 0
sensor16_data = 0

# -----------------------------------------------------------------------------

# ---------------------  Function to read serial from modbus slaves -----------

def lue_serial(Module, Sensor_number, Digits, Round, fifo_number, memcache_sensor_number):
    try:
        sensor_data_raw = round(Module.read_register(Sensor_number, Digits, 3, True), Round)
        fifo_number.appendleft(sensor_data_raw)
        sensor_data = round(sum(fifo_number) / len(fifo_number), Round)
        data_from_sensors = memcache.Client(['127.0.0.1:11211'], debug=0)
        data_from_sensors.set(memcache_sensor_number, sensor_data)
        return sensor_data
    except:  # Exception as e: print(e) 											#
        pass

# ----------------------------------------------------------------------------

# ---------------  Serial Read loop ------------------------------------------

def serial():
    while True:
        try:
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
            sensor1_data = lue_serial(module2, 0, 2, 1, sensor_data_fifo1, 'sensor1')
            sensor2_data = lue_serial(module2, 1, 2, 1, sensor_data_fifo2, 'sensor2')
            sensor3_data = lue_serial(module2, 2, 2, 1, sensor_data_fifo3, 'sensor3')
            sensor4_data = lue_serial(module2, 3, 2, 1, sensor_data_fifo4, 'sensor4')
            sensor5_data = lue_serial(module2, 4, 2, 1, sensor_data_fifo5, 'sensor5')
            sensor6_data = lue_serial(module2, 5, 2, 1, sensor_data_fifo6, 'sensor6')
            sensor7_data = lue_serial(module2, 6, 2, 1, sensor_data_fifo7, 'sensor7')
            sensor8_data = lue_serial(module2, 7, 2, 1, sensor_data_fifo8, 'sensor8')
            sensor9_data = lue_serial(module1, 0, 2, 1, sensor_data_fifo9, 'sensor9')
            sensor10_data = lue_serial(module1, 1, 2, 1, sensor_data_fifo10, 'sensor10')
            sensor11_data = lue_serial(module1, 2, 2, 1, sensor_data_fifo11, 'sensor11')
            sensor12_data = lue_serial(module1, 3, 2, 1, sensor_data_fifo12, 'sensor12')
            sensor13_data = lue_serial(module1, 0, 2, 1, sensor_data_fifo13, 'sensor13')
            sensor14_data = lue_serial(module1, 1, 2, 1, sensor_data_fifo14, 'sensor14')
            sensor15_data = lue_serial(module1, 2, 2, 1, sensor_data_fifo15, 'sensor15')
            sensor16_data = lue_serial(module1, 3, 2, 1, sensor_data_fifo16, 'sensor16')
            sleep(livedata_delay0 / 1000)
        except:  # Exception as e: print(e)
            continue

 # ----------------------------------------------------------------------------------


# ------------ Database Functions ------

def update_db():
    con = lite.connect('/home/maintenance/jms/jms/data/measure.db')           # Create SQLite Connection

    def db_1():
        value = sensor1_data
        aika = strftime("%Y-%m-%d %H:%M:%S")                                  # Time for the Database ...
        with con:                                                             # Connect to database ...
            cur = con.cursor()                                                #
            cur.execute(
                "CREATE TABLE IF NOT EXISTS measure1(aika TEXT, value INT)")  # Create table if not exest
            cur.execute("INSERT INTO measure1 (aika, value) VALUES(?,?)",
                        (aika, value))                                        # Put files to table

    def db_2():
        value = sensor2_data
        aika = strftime("%Y-%m-%d %H:%M:%S")
        with con:
            cur = con.cursor()
            cur.execute("CREATE TABLE IF NOT EXISTS measure2(aika TEXT, value INT)")
            cur.execute("INSERT INTO measure2 (aika, value) VALUES(?,?)", (aika, value))

    def db_3():
        value = sensor3_data
        aika = strftime("%Y-%m-%d %H:%M:%S")
        with con:
            cur = con.cursor()
            cur.execute("CREATE TABLE IF NOT EXISTS measure3(aika TEXT, value INT)")
            cur.execute("INSERT INTO measure3 (aika, value) VALUES(?,?)", (aika, value))

    def db_4():
        value = sensor4_data
        aika = strftime("%Y-%m-%d %H:%M:%S")
        with con:
            cur = con.cursor()
            cur.execute("CREATE TABLE IF NOT EXISTS measure4(aika TEXT, value INT)")
            cur.execute("INSERT INTO measure4 (aika, value) VALUES(?,?)", (aika, value))

    def db_5():
        value = sensor5_data
        aika = strftime("%Y-%m-%d %H:%M:%S")
        with con:
            cur = con.cursor()
            cur.execute("CREATE TABLE IF NOT EXISTS measure5(aika TEXT, value INT)")
            cur.execute("INSERT INTO measure5 (aika, value) VALUES(?,?)", (aika, value))

    def db_6():
        value = sensor6_data
        aika = strftime("%Y-%m-%d %H:%M:%S")
        with con:
            cur = con.cursor()
            cur.execute("CREATE TABLE IF NOT EXISTS measure6(aika TEXT, value INT)")
            cur.execute("INSERT INTO measure6 (aika, value) VALUES(?,?)", (aika, value))

    def db_7():
        value = sensor7_data
        aika = strftime("%Y-%m-%d %H:%M:%S")
        with con:
            cur = con.cursor()
            cur.execute("CREATE TABLE IF NOT EXISTS measure7(aika TEXT, value INT)")
            cur.execute("INSERT INTO measure7 (aika, value) VALUES(?,?)", (aika, value))

    def db_8():
        value = sensor8_data
        aika = strftime("%Y-%m-%d %H:%M:%S")
        with con:
            cur = con.cursor()
            cur.execute("CREATE TABLE IF NOT EXISTS measure8(aika TEXT, value INT)")
            cur.execute("INSERT INTO measure8 (aika, value) VALUES(?,?)", (aika, value))

    def db_9():
        value = sensor9_data
        aika = strftime("%Y-%m-%d %H:%M:%S")
        with con:
            cur = con.cursor()
            cur.execute("CREATE TABLE IF NOT EXISTS measure9(aika TEXT, value INT)")
            cur.execute("INSERT INTO measure9 (aika, value) VALUES(?,?)", (aika, value))

    def db_10():
        value = sensor10_data
        aika = strftime("%Y-%m-%d %H:%M:%S")
        with con:
            cur = con.cursor()
            cur.execute("CREATE TABLE IF NOT EXISTS measure10(aika TEXT, value INT)")
            cur.execute("INSERT INTO measure10 (aika, value) VALUES(?,?)", (aika, value))

    def db_11():
        value = sensor11_data
        aika = strftime("%Y-%m-%d %H:%M:%S")
        with con:
            cur = con.cursor()
            cur.execute("CREATE TABLE IF NOT EXISTS measure11(aika TEXT, value INT)")
            cur.execute("INSERT INTO measure11 (aika, value) VALUES(?,?)", (aika, value))

    def db_12():
        value = sensor12_data
        aika = strftime("%Y-%m-%d %H:%M:%S")
        with con:
            cur = con.cursor()
            cur.execute("CREATE TABLE IF NOT EXISTS measure12(aika TEXT, value INT)")
            cur.execute("INSERT INTO measure12 (aika, value) VALUES(?,?)", (aika, value))

    def db_13():
        value = sensor13_data
        aika = strftime("%Y-%m-%d %H:%M:%S")
        with con:
            cur = con.cursor()
            cur.execute("CREATE TABLE IF NOT EXISTS measure13(aika TEXT, value INT)")
            cur.execute("INSERT INTO measure13 (aika, value) VALUES(?,?)", (aika, value))

    def db_14():
        value = sensor14_data
        aika = strftime("%Y-%m-%d %H:%M:%S")
        with con:
            cur = con.cursor()
            cur.execute("CREATE TABLE IF NOT EXISTS measure14(aika TEXT, value INT)")
            cur.execute("INSERT INTO measure14 (aika, value) VALUES(?,?)", (aika, value))

    def db_15():
        value = sensor15_data
        aika = strftime("%Y-%m-%d %H:%M:%S")
        with con:
            cur = con.cursor()
            cur.execute("CREATE TABLE IF NOT EXISTS measure15(aika TEXT, value INT)")
            cur.execute("INSERT INTO measure15 (aika, value) VALUES(?,?)", (aika, value))

    def db_16():
        value = sensor16_data
        aika = strftime("%Y-%m-%d %H:%M:%S")
        with con:
            cur = con.cursor()
            cur.execute("CREATE TABLE IF NOT EXISTS measure16(aika TEXT, value INT)")
            cur.execute("INSERT INTO measure16 (aika, value) VALUES(?,?)", (aika, value))


    while True:
        if (sensor1_enable):
            db_1()
        if (sensor2_enable):
            db_2()
        if (sensor3_enable):
            db_3()
        if (sensor4_enable):
            db_4()
        if (sensor5_enable):
            db_5()
        if (sensor6_enable):
            db_6()
        if (sensor7_enable):
            db_7()
        if (sensor8_enable):
            db_8()
        if (sensor9_enable):
            db_9()
        if (sensor10_enable):
            db_10()
        if (sensor11_enable):
            db_11()
        if (sensor12_enable):
            db_12()
        if (sensor13_enable):
            db_13()
        if (sensor14_enable):
            db_14()
        if (sensor15_enable):
            db_15()
        if (sensor16_enable):
            db_16()
        sleep(historydata_delay0 / 1000)


# ------------------------------------------------

# -------------  Functions to background ---------

serial_threat = threading.Thread(target=serial)
db_threat = threading.Thread(target=update_db)

serial_threat.start()
db_threat.start()

# ------------------------------------------------