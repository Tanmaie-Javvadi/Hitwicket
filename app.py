from flask import Flask
from flask_socketio import SocketIO

app = Flask(__name__)
socketio = SocketIO(app)

@socketio.on('connect')
def handle_connect():
    print('A player connected')

@socketio.on('disconnect')
def handle_disconnect():
    print('Player disconnected')

if __name__ == '__main__':
    socketio.run(app, port=3000, allow_unsafe_werkzeug=True)

