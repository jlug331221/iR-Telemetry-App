import irsdk

import eventlet
eventlet.monkey_patch()

from iR_state import IRState
from iR_telemetry import start_iR_telemetry

from flask import Flask, render_template
from flask_socketio import SocketIO, emit

app = Flask(__name__)

# Flask app has now become a Flask-SocketIO app
socketio = SocketIO(app, async_mode='eventlet')

iR_sdk = irsdk.IRSDK()
iR_state = IRState()

thread = None

@app.route('/')
def index():
    return render_template('index.html')

def send_iR_data_to_client():
    """
    Send iRacing data to the client.
    """

    start_iR_telemetry(iR_sdk, iR_state, socketio)

@socketio.on('connect')
def on_connect():
    print('\nServer -> Client is connected.\n')

    global thread
    if thread is None:
        thread = socketio.start_background_task(target=send_iR_data_to_client)

@socketio.on('disconnect')
def on_disconnect():
    print('\nServer -> Client is disconnected.\n')

if __name__ == '__main__':
    socketio.run(app)
