from flask import Flask
from flask_socketio import SocketIO

jms = Flask(__name__)
jms.config['DEBUG'] = True
socketio = SocketIO(jms)

from jms import routes
