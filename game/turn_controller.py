import random

# wrapper controlling turns for the players..
# the players are given turns in order, but the intial determined order is random
class TurnController:
    # init function creates a list with random order of numbers between 0 -> num of clients - 1
    def __init__(self, players):
        self.num_players = len(players)

        self.turn_order = list(range(0, self.num_players))
        random.shuffle(self.turn_order)

        self.turn_idx = -1


    # Function to return next number in turn_order
    def get_next_turn_idx(self):
        self.turn_idx += 1

        return self.turn_order[self.turn_idx % self.num_players]


    # Function to move turn back one
    def reset_turn(self):
        self.turn_idx -= 1


    # Function to return string for turn query
    def get_turn_query(self):
        return "It's your turn! What would you like to do?"


    # Function to return innocent turn options
    def get_innocent_options(self):
        return ["Move room...", "Make an accusation...", "Share your evidence..."]


    # Function to return murderer turn options
    def get_murderer_options(self):
        return ["Move room...", "Make an accusation...", "Share fake evidence..."]

