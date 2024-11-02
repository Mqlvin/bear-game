from util import serialize_dict
import random
import uuid
import json

from game.player import Player
from game.turn_controller import TurnController
from game.vote_controller import do_blocking_vote
from game.fact.fact import StoryManager


# Class to handle the game loop and clients
class Game:
    def __init__(self, players):
        self.players = players # shells initialised by socket_server
        self.turn_controller = TurnController(self.players)
        self.story_manager = StoryManager()
        
        # assign bear names
        colours = ["Scarlett", "Brown", "Beige", "Mustard", "Violet", "Teal", "Jade", "Noir"]
        for player in players:
            player.name = colours.pop(random.randint(0, len(colours) - 1)) + " Bear"

        # choose murderer
        self.murderer_index = random.randint(0, len(self.players) - 1)
        self.players[self.murderer_index].is_murderer = True
        
 
        # dispatches the roles of each player to the respective clients
        self.dispatch_client_roles()


        # generates characteristics and hence facts of the game
        self.story_manager.generate_facts(self.players[self.murderer_index].characteristics)
        self.story_manager.generate_herrings(list(filter(lambda x: not x.is_murderer, self.players)))

        # assign murderer, then players, any other characteristics
        self.players[self.murderer_index].characteristics.fill_characteristics(None, True)
        for player in self.players:
            if player == self.players[self.murderer_index]:
                continue
            player.characteristics.fill_characteristics(self.players[self.murderer_index].characteristics, False)

        print()
        print()
        self.story_manager.generate_other_evidence(list(filter(lambda x: not x.is_murderer, self.players)))
        print()
        print()

        self.dispatch_bear_characteristics()

        # start the game
        self.launch_game()
        

    # Function to start game loop, handles the three game loop options
    def launch_game(self):
        game_ended = False

        # main game loop
        while not game_ended:
            player_idx = self.turn_controller.get_next_turn_idx()
            player = self.players[player_idx]
            chose = 0
            if player.is_murderer:
                chose = player.query(self.turn_controller.get_turn_query(), self.turn_controller.get_murderer_options())
            else:
                chose = player.query(self.turn_controller.get_turn_query(), self.turn_controller.get_innocent_options())
            if chose == 0:
                self.do_room_move(player)


            if chose == 1: # accusation
                options = []
                for pl_it in self.players:
                    if player == pl_it:
                        options.append("Accuse the " + pl_it.name + " (you)")
                        continue
                        
                    options.append("Accuse the " + pl_it.name)
                
                accused_idx = player.query("Who would you like to accuse?", options)
                result = do_blocking_vote(self.players, accused_idx, player_idx)

                if result:
                    if accused_idx == self.murderer_index:
                        Player.broadcast_str(list(filter(lambda pl: not pl.is_murderer, self.players)), "You guessed the murderer correctly... You win!")
                        self.players[self.murderer_index].send_text("You were convicted... You lost!")
                    else:
                        Player.broadcast_str(list(filter(lambda pl: not pl.is_murderer, self.players)), "...You convicted an innocent bear. You lose!")
                        self.players[self.murderer_index].send_text("An innocent bear was convicted, so you got away with the murder... You win!")

                    # TODO
                    # Not all players get the same message - the murderer needs an opposing you win you lose

                    exit(0)
                    
                


            if chose == 2:
                if player.is_murderer:
                    random.shuffle(self.story_manager.fake_evidences)

                    fake_evidence_options = self.story_manager.fake_evidences[0:3]
                    player.send_text("newline")
                    for option in range(0, len(fake_evidence_options)):
                        player.send_text("Option " + str(option + 1) + ": " + fake_evidence_options[option].fact_string)

                    fe_idx = player.query("Which fact would you like to fake?", [(x.fact_string[0:80] + "...") for x in fake_evidence_options])
                    fe = fake_evidence_options[fe_idx]
                    
                    player_options = []
                    for pl_it in self.players:
                        if player == pl_it:
                            continue
                        player_options.append(pl_it)

                    friend = player_options[player.query("Who would you like to share this with?", [pl.name for pl in player_options])]

                    player.send_text("newline")
                    player.send_text("You shared the fact '" + fe.fact_string + "' with the " + friend.name)
                    friend.fact_inventory.add_info(fe.fact_string)
                    friend.send_text("newline")
                    friend.send_text(player.name + " shared some information with you: " + fe.fact_string)

                else:
                    player_knowledge = player.fact_inventory.get_info()
                    if len(player_knowledge) == 0:
                        player.send_text("newline")
                        player.send_text("You have no knowledge of the crime scene yet.")
                        self.turn_controller.reset_turn()
                        continue
                    
                    fact_options = [(fact[0:100] + "...") for fact in player_knowledge]
                    fact_idx = player.query("Which fact would you like to share?", fact_options)
                    fact = player_knowledge[fact_idx]

                    player_options = []
                    for pl_it in self.players:
                        if player == pl_it:
                            continue
                        player_options.append(pl_it)

                    friend = player_options[player.query("Who would you like to share this with?", [pl.name for pl in player_options])]

                    player.send_text("newline")
                    player.send_text("You shared the fact '" + fact[0:30] + "...' with the " + friend.name)
                    friend.fact_inventory.add_info(fact)
                    friend.send_text("newline")
                    friend.send_text(player.name + " shared some information with you: " + fact)



    # Function to handle the player move turn
    def do_room_move(self, player):
        # move the players room
        rooms = [room_enum for room_enum in player.current_room.get_moves()]
        response = player.query("Which room would you like to move to?", [str(room_name) for room_name in rooms])
        player.current_room = rooms[response]
        player.send_text("You moved to the " + str(player.current_room) + " and take a look around...")

        # do the search
        room_info = self.story_manager.get_info_in_room(player.current_room)
        if len(room_info) == 0:
            player.send_text("You couldn't find any incriminating evidence.")
        else:
            for item in room_info:
                player.send_text("newline")
                player.send_text(item.fact_string)
                player.fact_inventory.add_info(item.fact_string)

        return None

           



    
    # Function to do the initial dispatch of client roles (murderer, innocent) and sends each client respective instructions
    def dispatch_client_roles(self):
        for player in self.players:
            player.sock.send(serialize_dict({"event_type":"game_init", "player_name":player.name, "is_murderer":player.is_murderer}))

            if player.is_murderer:
                player.send_text("You are the murderer!")
                player.send_text("Your objective is to trick players into convicting an innocent bear. You will play as if an innocent bear, except you can communicate fake evidence!")
            else:
                player.send_text("You are an innocent!")
                player.send_text("Your objective is to find whom the murderer is. Search the house for clues, and share evidence alongside other innocents. Once you're confident on your knowledge, use your turn to convict the murderer!")
    


    # Function to send the bear characteristics to each bear for the bear viewer feature
    def dispatch_bear_characteristics(self):
        bears = []

        for player in self.players:
            bears.append({"name":player.name, "characteristics":{"gender":player.characteristics.gender.title(), "age":str(player.characteristics.age) + " y/o", "height":str(player.characteristics.height) + " cm tall", "fur_length":player.characteristics.fur_length.title() + " Fur", "colour":player.characteristics.colour.title() + " Fur", "likes_food":"Likes " + player.characteristics.likes_food}})

        Player.broadcast(self.players, {"event_type":"serve_characteristics", "bears":bears})
            

