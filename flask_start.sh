#!/bin/bash
source /home/maintenance/jms/virtuaalijms/bin/activate
export FLASK_APP=~/jms/jms.py
export FLASK_DEBUG=1
/home/maintenance/jms/virtuaalijms/bin/flask run --host=192.168.44.111
