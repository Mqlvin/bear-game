import uuid
from util import serialize_dict
from game.characteristics import CharacteristicManager
from game.rooms import Room
from game.inventory import FactInventory

# Basic player info + player handling class
class Player:
    def __init__(self, sock):
        self.sock = sock
        self.buffer = []
        self.uuid = uuid.uuid4()
        self.name = "" # populated by game
        self.is_murderer = False
        self.characteristics = CharacteristicManager()
        self.current_room = Room.HALL
        self.fact_inventory = FactInventory(self)


    # Function to put text on the client terminal
    def send_text(self, text):
        self.sock.send(serialize_dict({"event_type":"display", "text":text}))


    # Function to send the client a question and receive a response, is thread blocking
    def query(self, question, options):
        token = str(uuid.uuid4())

        self.sock.send(serialize_dict({"event_type":"take_input", "options":options, "question":question, "token":token}))

        while len(self.buffer) == 0:
            continue

        client_response = self.buffer.pop()

        if client_response["token"] != token:
            print("Error - client provided invalid transaction token")
            return None

        return client_response["response"]


    # Function to register a piece of evidence on the client
    def send_evidence(self, fact_string):
        self.sock.send(serialize_dict({"event_type":"evidence", "fact_string":fact_string}))
    

    # Static function to broadcast a given dict to all clients
    @staticmethod
    def broadcast(players, data_dict):
        serialized = serialize_dict(data_dict)
        for player in players:
            player.sock.send(serialized)


    # Static method to broadcast a send_text event on all clients
    @staticmethod
    def broadcast_str(players, str):
        for player in players:
            player.send_text(str)



