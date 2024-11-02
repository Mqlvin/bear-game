from game.player import Player


# Function to launch a thread-blocking vote
def do_blocking_vote(player_objs, convicted_idx, accuser_idx):
    do_vote_announcement(player_objs, convicted_idx, accuser_idx)
    results = query_player_votes(player_objs, convicted_idx, accuser_idx)
    final_result = do_vote_results(player_objs, results)
    return final_result


# Function to query each player for their vote, returns the result
def query_player_votes(player_objs, convicted_idx, accuser_idx):
    question = player_objs[accuser_idx].name + " is convicting " + player_objs[convicted_idx].name + " of being the murderer. Do you agree? "
    options = ["Yes, I think " + player_objs[convicted_idx].name + " is the murderer", "No, I don't think " + player_objs[convicted_idx].name + " is the murderer, or I'm not certain yet"]

    responses = []
    for player in player_objs:
        # here we do allow the murderer to vote for themself

        if player_objs[accuser_idx] == player:
            responses.append(True)
            continue

        response = player.query(question, options)
        responses.append(response == 0)
        # TODO: Say what each player voted here?

    return responses


# Function to announce a vote has been launched
def do_vote_announcement(player_objs, convicted_idx, accuser_idx):
    Player.broadcast_str(player_objs, "newline")
    Player.broadcast_str(player_objs, "A vote has been launched to accuse a bear of being the murderer. Be prepared to make a quick decision!")
    

# Function to broadcast vote results
def do_vote_results(player_objs, results):
    if results.count(True) > len(results) / 2:
        Player.broadcast_str(player_objs, "newline")
        Player.broadcast_str(player_objs, "Over half the voters agreed, and so the bear has been convicted...")
        return True
    else:
        Player.broadcast_str(player_objs, "newline")
        Player.broadcast_str(player_objs, "Less than, or half the voters agreed, and so the bear has not been convicted. Try gather more evidence and share it amongst yourselves.")
        return False
