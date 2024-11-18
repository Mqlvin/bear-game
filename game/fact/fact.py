import random
from game.rooms import Room

foods = ["salmon", "berries", "nuts", "honey", "fruits"]
furs = ["short", "long"]
colours = ["grey", "black", "brown", "blonde"]
genders = ["male", "female", "female", "female", "female"] # bias female


# couldn't be bothered to use pythons ABC system
# abstract class inherited by story facts below
class StoryFact:
    def __init__(self):
        self.is_incriminating = True
        self.fact_string = ""

    # override this in impl to modify fact_string
    def gen(self, char_obj):
        pass


#
# List of facts below, all represented as classes.
# Each class can create a bears characteristics and the fact is returned
# If the bear has pre-existing characteristics and they're fitting with the fact, the fact is returned, else None
#

class FactKitchen1(StoryFact):
    def __init__(self):
        self.is_incriminating = False

    def gen(self, char_obj):
        if not char_obj.likes_food:
            char_obj.likes_food = random.choice(foods)

        self.fact_string = "A " + random.choice(["food processor", "blender"]) + " has been left on nearby, blending a delicious mix of " + char_obj.likes_food + " and " + random.choice(foods) + "... Maybe this bear was interrupted by the murder."
        return self


class FactKitchen2(StoryFact):
    def gen(self, char_obj):
        if not char_obj.height:
            char_obj.height = random.randint(120, 160)
        elif char_obj < 120:
            return None

        self.fact_string = "You check the shelf by the " + random.choice(["oven", "sink", "cupboards"]) + ", and you notice an empty jar of honey covered in blood is on the top shelf... Maybe the murderer is tall?"
        return self
            

class FactKitchen3(StoryFact):
    def __init__(self):
        self.is_incriminating = False

    def gen(self, char_obj):
        if not char_obj.likes_food:
            char_obj.likes_food = random.choice(foods)

        self.fact_string = "Some " + char_obj.likes_food + " has been left burning" + (" on the stove" if random.getrandbits(1) == 0 else " in the oven") + "... Maybe this bear was interrupted by the murder."
        return self


class FactKitchen4(StoryFact):
    def gen(self, char_obj):
        if not char_obj.likes_food:
            char_obj.likes_food = random.choice(foods)

        self.fact_string = "You notice a freshly made smoothie. Upon further inspection, it smells of " + char_obj.likes_food + " and blood... Is this a drink of the murderer?"
        return self


class FactKitchen5(StoryFact):
    def gen(self, char_obj):
        if not char_obj.colour:
            char_obj.colour = random.choice(colours)

        if not char_obj.fur_length:
            char_obj.fur_length = random.choice(furs)

        self.fact_string = "You notice a tea-towel covered in bloody paw prints. As you take a closer look you notice " + (char_obj.colour if random.getrandbits(1) == 0 else char_obj.fur_length) + " fur stuck to the towel... Could this be the fur of the murderer?"
        return self


class FactGarage1(StoryFact):
    def gen(self, char_obj):
        if not char_obj.age:
            char_obj.age = random.randint(18, 40)
        elif char_obj.age < 18:
            return None

        self.fact_string = "You notice the " + random.choice(["car handle", "steering wheel", "window"]) + " is covered in blood... Maybe the murderer was trying to drive away?"
        return self


class FactGarage2(StoryFact):
    def __init__(self):
        self.is_incriminating = False

    def gen(self, char_obj):
        if not char_obj.age:
            char_obj.age = random.randint(18, 40)
        elif char_obj.age < 18:
            return None

        self.fact_string = "As you enter the garage, you notice a set of tools - spanners, screwdrivers, even a saw... Could this have been the murderer?"
        return self


class FactGarage3(StoryFact):
    def __init__(self):
        self.is_incriminating = False

    def gen(self, char_obj):
        self.fact_string = "There is a driving license on the floor... it appears to belong to the murdered bear."
        return self


class FactGarage4(StoryFact):
    def gen(self, char_obj):
        if not char_obj.gender:
            char_obj.gender = "female"
        elif char_obj == "male":
            return None

        self.fact_string = "As you explore the garage, you notice a floral scent around the blood... Maybe this is the scent of the murderer?"
        return self


class FactLounge1(StoryFact):
    def gen(self, char_obj):
        if not char_obj.fur_length:
            char_obj.fur_length = random.choice(furs)

        if not char_obj.colour:
            char_obj.colour = random.choice(colours)

        item = random.choice(["pillow", "sofa", "armchair"]) 
        self.fact_string = "As you look around the lounge, you notice a lashed " + item + ", covered in blood and fur. Upon further inspection, the " + item + " is covered in " + (char_obj.fur_length.lower() if random.getrandbits(1) == 0 else char_obj.colour.lower()) + " fur... Could this be the fur of the murderer?"
        return self


class FactLounge2(StoryFact):
    def __init__(self):
        self.is_incriminating = False

    def gen(self, char_obj):
        if not char_obj.age:
            char_obj.age = random.randint(1, 40)

        if char_obj.age > 14:
            self.fact_string = "You notice on one of the sofas a book tossed aside. It appears to be a childrens book... Maybe this young bear was interrupted by the murder?"
        else:
            self.fact_string = "You notice on one of the sofas a book tossed aside, next to a pair of glasses thick glasses... Maybe this elder bear was interrupted by the murder?"

        return self


class FactLounge3(StoryFact):
    def __init__(self):
        self.is_incriminating = False

    def gen(self, char_obj):
        if not char_obj.age:
            char_obj.age = random.randint(1, 18)
        elif char_obj.age > 18:
            return None

        self.fact_string = "As you walk into the lounge, you see an idle game of " + random.choice(["Mario Kart Wii", "Wii Sports", "Wii Sports Resort", "Animal Crossing: City Folk"]) + ", with a remote on the floor... Maybe this young bear was interrupted by the murder?"
        return self


class FactLounge4(StoryFact):
    def gen(self, char_obj):
        if not char_obj.colour:
            char_obj.colour = random.choice(colours)

        self.fact_string = "You notice bloody gloves strewn on the lounge floor. You cautiously take a look inside, and notice " + char_obj.colour + "fur... Could these be the murderer's gloves?"
        return self


class FactDiningRoom1(StoryFact):
    def __init__(self):
        self.is_incriminating = False

    def gen(self, char_obj):
        if not char_obj.likes_food:
            char_obj.likes_food = random.choice(foods)

        if not char_obj.age:
            char_obj.age = random.randint(1, 40)

        self.fact_string = "As you enter the dining room you notice a plate of half eaten " + char_obj.likes_food + " on the table, aside it a glass of " + ("wine" if char_obj.age > 18 else "fruit juice") + "... This bear seems to have been interrupted by the murder, when eating their meal."
        return self


class FactDiningRoom2(StoryFact):
    def __init__(self):
        self.is_incriminating = False

    def gen(self, char_obj):
        if not char_obj.age:
            char_obj.age = random.randint(30, 40)
        elif char_obj.age < 18:
            return None

        self.fact_string = "A smashed whiskey glass is on the floor and you notice a tatty newspaper upon the table next to it... Was this bear interrupted by the murder?"
        return self


class FactDiningRoom3(StoryFact):
    def gen(self, char_obj):
        if not char_obj.age:
            char_obj.age = random.randint(18, 40)
        elif char_obj.age < 18:
            return None

        self.fact_string = "As you enter the dining room, you notice a plate of food next to an empty bottle of vodka. Taking a closer look, there is no knife with the food... Maybe the murderer was drunk?"
        return self


class FactBedroom1(StoryFact):
    def gen(self, char_obj):
        if not char_obj.age:
            char_obj.age = random.randint(1, 14)
        elif char_obj.age > 14:
            return None

        self.fact_string = "Upon entering the bedroom, you notice a torn stuffed " + random.choice(["bear", "animal", "toy"]) + "... Maybe the murderer was a psychotic young bear?"
        return self


class FactBedroom2(StoryFact):
    def __init__(self):
        self.is_incriminating = False

    def gen(self, char_obj):
        if not char_obj.age:
            char_obj.age = random.randint(1, 40)

        if char_obj.age > 14:
            self.fact_string = "You notice on the bed there is a book left open. It appears to be a childrens book... Maybe this young bear was interrupted by the murder?"
        else:
            self.fact_string = "You notice on the bed there is a book left open, next to a pair of glasses thick glasses... Maybe this elder bear was interrupted by the murder?"

        return self


class FactBedroom3(StoryFact):
    def gen(self, char_obj):
        if not char_obj.gender:
            char_obj.gender = "female"
        elif char_obj.gender == "male":
            return None

        self.fact_string = "You decide to look in the drawers, noticing a jewellery box covered in blood. To your surprise, opening it reveals a small dagger... Maybe the murderer likes jewellery?"
        return self


class FactBedroom4(StoryFact):
    def gen(self, char_obj):
        if not char_obj.gender:
            char_obj.gender = "female"
        elif char_obj.gender == "male":
            return None

        self.fact_string = "You take a look in the closet. You notice a dress with blood stains, and upon further inspection a knife has been slipped into the dress pocket... Maybe the murderer wears this dress?"
        return self


class FactBathroom1(StoryFact):
    def gen(self, char_obj):
        if not char_obj.fur_length:
            char_obj.fur_length = random.choice(furs)

        if not char_obj.colour:
            char_obj.colour = random.choice(colours)

        self.fact_string = "As you take a look in the ensuite, you notice the bathtub is pooled with blood. You lean in to take a closer look, noticing strands of " + (char_obj.fur_length if random.getrandbits(1) == 0 else char_obj.colour) + " fur stuck to the tub... Maybe the murderer washed their paws here?"
        return self


class FactBathroom2(StoryFact):
    def gen(self, char_obj):
        if not char_obj.fur_length:
            char_obj.fur_length = random.choice(furs)

        if not char_obj.colour:
            char_obj.colour = random.choice(colours)

        if not char_obj.gender:
            char_obj.gender = random.choice(genders)

        self.fact_string = "As you walk into the ensuite, a red, bloody towel catches your eye. Taking a closer look, you notice " + (char_obj.fur_length if random.getrandbits(1) == 0 else char_obj.colour) + " fur covering the " + ("pink, flowery" if char_obj.gender == "female" else "navy blue")  + " bathtowel... Maybe the murderer washed their paws here?"
        return self


class FactBathroom3(StoryFact):
    def __init__(self):
        self.is_incriminating = False

    def gen(self, char_obj):
        if not char_obj.gender:
            char_obj.gender = "female"
        elif char_obj.gender == "male":
            return None

        self.fact_string = "As you walk into the ensuite, you notice a makeup kit knocked into the sink - a brush knocked onto the floor... What happened here?"
        return self


# List of rooms, class mapping of rooms and associated facts
rooms = [Room.KITCHEN, Room.DINING_ROOM, Room.LIVING_ROOM, Room.GARAGE, Room.BEDROOM, Room.ENSUITE]
class_map = {Room.KITCHEN:[FactKitchen1, FactKitchen2, FactKitchen3, FactKitchen4, FactKitchen5], Room.GARAGE:[FactGarage1, FactGarage2, FactGarage3, FactGarage4], Room.LIVING_ROOM:[FactLounge1, FactLounge2, FactLounge3, FactLounge4], Room.DINING_ROOM:[FactDiningRoom1, FactDiningRoom2, FactDiningRoom3], Room.BEDROOM:[FactBedroom1, FactBedroom2, FactBedroom3, FactBedroom4], Room.ENSUITE:[FactBathroom1, FactBathroom2, FactBathroom3]}


# Basic class to handle the facts of the story, the herrings of the story, and the murderer's fake evidence
class StoryManager:
    def __init__(self):
        self.facts = []
        self.herrings = []
        self.fake_evidences = []


    # Gets the room enum given a StoryFact inheriting class
    def get_instance_enum(self, instance):
        for room_enum, classes in class_map.items():
            if any(isinstance(instance, class_type) for class_type in classes):
                return room_enum

        print("Err: No instance found of " + str(instance) + " for enum type")
        exit(1)


    # Returns all the facts and herrings within a room
    def get_info_in_room(self, room):
        infos = []

        for fact in self.facts:
            if self.get_instance_enum(fact) == room:
                infos.append(fact)

        for herring in self.herrings:
            if self.get_instance_enum(herring) == room:
                infos.append(herring)

        random.shuffle(infos)
        return infos
        

    # Generates random, unique facts for the rooms
    def generate_facts(self, murderer_characteristics):
        while len(self.facts) < 3:
            random_room = random.choice(rooms)
            random_fact = random.choice(class_map[random_room])

            # make sure we don't already have the fact
            if any(isinstance(fact, random_fact) for fact in self.facts):
                continue

            # make sure the fact is incriminating
            if not random_fact().is_incriminating:
                continue

            random_fact_obj = random_fact()
            random_fact_obj = random_fact_obj.gen(murderer_characteristics)

            if random_fact_obj:
                self.facts.append(random_fact_obj)

        #for fact in self.facts:
        #    print(fact.fact_string)

    
    # Generates random, unique herrings for the rooms
    def generate_herrings(self, innocent_bears):
        # rooms with facts
        fact_rooms = []
        for fact in self.facts:
            fact_rooms.append(fact.__class__.__name__[4:-1].lower())

        while len(self.herrings) < 4:
            room = ""
            # random element, num of tries before allowing herring to be in same room as fact
            tries_before_same_room = 2
            while True:
                rand_room = random.choice(rooms)
                if not room in fact_rooms:
                    room = rand_room
                    break

                tries_before_same_room -= 1
                if tries_before_same_room == 0:
                    room = rand_room
                    break

            random_herring = random.choice(class_map[room])

            if any(isinstance(herring, random_herring) for herring in self.herrings):
                continue

            if random_herring().is_incriminating:
                continue

            random_herring_obj = random_herring()
            random_herring_obj = random_herring_obj.gen(random.choice(innocent_bears).characteristics)

            if random_herring_obj:
                self.herrings.append(random_herring_obj)


        #for herring in self.herrings:
        #    print(herring.fact_string)

    
    # Generates murderer's fake evidence and retains in a list
    def generate_other_evidence(self, innocent_bears):
        for _, classes in class_map.items():
            for clazz in classes:
                for herring in self.herrings:
                    if type(herring) == type(clazz):
                        break
                else: # for else weirdness
                    if clazz().is_incriminating:
                        continue

                    evidence = clazz()
                    evidence = evidence.gen(random.choice(innocent_bears).characteristics)

                    if not evidence:
                        continue

                    self.fake_evidences.append(evidence)
            
        #for fe in self.fake_evidences:
        #    print(fe.fact_string)
