from flask import Flask, send_from_directory
from flask_sock import Sock
import json
from client_manager import ClientManager
from util import serialize_dict

app = Flask(__name__, static_url_path='', static_folder="static/")
sock = Sock(app)

client_manager = ClientManager()

# Func to handle adding socket connect to client_manager
@sock.route('/game_socket')
def on_sock_connect(socket):
    client_manager.add_client(socket)

    while True:
        data = socket.receive()
        client_manager.dispatch_response(socket, data) # sends data to appropriate player buffer


# Func to serve static directory
@app.route('/static/<path:path>')
def serve(path):
    return send_from_directory("static", path)


# Func to serve '/' as '/index.html'
@app.route('/')
def home():
    # Serve index.html by default
    return send_from_directory('static', 'index.html')


if __name__ == "__main__":
    app.run(debug=True)
