from game.game import Game
from game.player import Player
from threading import Thread
import json


# Class to manage socket connections and start game on separate thread when necessary
class ClientManager:
    def __init__(self):
        self.players = []
        self.sock_lookup = {}
        self.game = None

    
    # Class func to add a client + check and start game if necessary
    def add_client(self, sock):
        pl = Player(sock)
        self.players.append(pl)
        self.sock_lookup[id(sock)] = pl
        
        # this probably could have detrimental consequences
        # anything the game object accesses NEEDS to be passed into the game object
        # and cloned or else who knows what chaos will ensue with the threads
        if len(self.players) == 4:
            thread = Thread(target = self.start_game)
            thread.start()
        elif len(self.players) > 4:
            print("Warning! Client connected beyond 4 player limit - hence, ignored.")


    # Class func to pass socket data down to game
    def dispatch_response(self, sock, data):
        if id(sock) in self.sock_lookup:
            self.sock_lookup[id(sock)].buffer.append(json.loads(data))
        else:
            print("Err: Received data from unregistered socket")


    # Class func to create the game object, hence init-ing game
    def start_game(self):
        self.game = Game(self.players)
        
