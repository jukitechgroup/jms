#!/bin/bash
source /home/jms/JMS/virtuaalijms/bin/activate
export FLASK_APP=/home/jms/JMS/jms.py
export FLASK_DEBUG=1
/home/jms/JMS/virtuaalijms/bin/flask run --host=192.168.1.202
