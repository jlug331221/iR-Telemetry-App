from flask_socketio import SocketIO, emit

DEBUG = False

def check_iRacing(iR_sdk, iR_state):
    """
    Check if there is a connection to iRacing so that we can
    gather telemetry data.
    """

    if iR_state.iR_connected and not (iR_sdk.is_initialized and iR_sdk.is_connected):
        iR_state.set_iR_connected(False)
        iR_state.set_last_car_setup_tick(-1)

        iR_sdk.shutdown()

        print('\niRacing disconnected\n')

    elif not iR_state.iR_connected and iR_sdk.startup() and iR_sdk.is_initialized and iR_sdk.is_connected:
        iR_state.set_iR_connected(True)
        print('\niRacing connected\n')

    elif not iR_state.iR_connected:
        if(DEBUG):
            print('\nWaiting on iRacing...\n')

def start_iR_telemetry(iR_sdk, iR_state, socketio):
    """
    Begin gathering iRacing telemetry data and send the data
    to the client.
    """

    try:
        print('Attempting to connect to iRacing...\n')

        while True:
            check_iRacing(iR_sdk, iR_state)

            if iR_state.iR_connected:
                if iR_sdk['SessionTime']:
                    print('\nServer -> Session time: ' +  str(iR_sdk['SessionTime']) + '\n')
                    
                    socketio.emit('iR_data', {'sessionTime': iR_sdk['SessionTime']})

            socketio.sleep(1)
            
    except KeyboardInterrupt:
        # use Ctrl+c to exit
        pass
