from flask import Flask, render_template
from flask_socketio import SocketIO, emit
from game_logic import initialize_board
from game import move_character

app = Flask(__name__)
socketio = SocketIO(app)

game_board = initialize_board()

@socketio.on('move')
def handle_move(data):
    character = data['character']
    move = data['move']
    current_position = data['position']
    
    board = move_character(game_board, character, current_position, move)
    socketio.emit('update_board', board)

if __name__ == '__main__':
    socketio.run(app, port=3000, allow_unsafe_werkzeug=True)
