import random

class CharacteristicManager:
    def __init__(self):
        self.height = None
        self.age = None
        self.gender = None
        self.colour = None
        self.fur_length = None
        self.likes_food = None

    # called by game object to fill in rest of unassigned characteristics
    def fill_characteristics(self, murderer_characteristics, is_murderer):
        if is_murderer:
            self.gen_murderer_characteristics()
        else:
            self.gen_innocent_characteristics(murderer_characteristics)


    # generates characteristics for the murderer, generally random
    def gen_murderer_characteristics(self):
        if not self.age:
            self.age = random.randint(1, 40)

        if not self.height:
            self.height = max(15, self.age) * random.randint(3, 4)

        if not self.gender:
            self.gender = random.choice(["male", "female"])

        if not self.colour:
            self.colour = random.choice(["grey", "black", "brown", "blonde"])

        if not self.fur_length:
            self.fur_length = random.choice(["short", "long"])

        if not self.likes_food:
            self.likes_food = random.choice(["salmon", "berries", "nuts", "honey", "fruits"])


    # generates characteristics for the innocents, using an algorithm against the murderer's characteristics
    # 3-5 features should be similar, the rest should be opposing
    def gen_innocent_characteristics(self, murderer_characteristics):
        # first get list of characteristics that have been set
        set_characteristics = [attr for attr in vars(self) if not getattr(self, attr, None) == None]
        print("already set characteristics for " + ": " + str(set_characteristics))


        # next get list of characteristics that are similar to murderer
        similar_characteristics = []
        if self.age and abs(murderer_characteristics.age - self.age) < 5:
            similar_characteristics.append("age")

        if self.height and abs(murderer_characteristics.height - self.height) < 20:
            similar_characteristics.append("height")

        if self.gender and self.gender == murderer_characteristics.gender:
            similar_characteristics.append("gender")

        if self.colour and self.colour == murderer_characteristics.colour:
            similar_characteristics.append("colour")

        if self.fur_length and self.fur_length == murderer_characteristics.fur_length:
            similar_characteristics.append("fur_length")

        if self.likes_food and self.likes_food == murderer_characteristics.likes_food:
            similar_characteristics.append("likes_food")


        # using the length of similar characteristics to murderer, we know how many more similar to make
        # match between 3 and 5 characteristics similar to murderer
        set_characteristics = [attr for attr in vars(self) if not getattr(self, attr, None) == None]
        should_match_n = 6 - len(set_characteristics)


        if should_match_n >= len(similar_characteristics):
            for i in range(0, should_match_n - len(similar_characteristics) + 1):
                unset_characteristic = None

                if not "gender" in set_characteristics:
                    unset_characteristic = "fur_length"
                elif not "colour" in set_characteristics:
                    unset_characteristic = "colour"
                elif not "fur_length" in set_characteristics:
                    unset_characteristic = "fur_length"

                while unset_characteristic is None:
                    random_characteristic = random.choice(vars(self))
                    if not random_characteristic in set_characteristics:
                        unset_characteristic = random_characteristic

                if unset_characteristic == "age":
                    setattr(self, unset_characteristic, murderer_characteristics.age - 5 + random.randint(1, 10))
                elif unset_characteristic == "height":
                      setattr(self, unset_characteristic, murderer_characteristics.height - 20 + random.randint(1, 40))
                elif unset_characteristic == "gender":
                      setattr(self, unset_characteristic, murderer_characteristics.gender)
                elif unset_characteristic == "colour":
                      setattr(self, unset_characteristic, murderer_characteristics.colour)
                elif unset_characteristic == "fur_length":
                      setattr(self, unset_characteristic, murderer_characteristics.fur_length)


        # now all similar characteristics are done, filled the rest of characteristics
        # with opposing values of the murderer
        if not self.age:
            new_age = random.randint(1, 40)
            while abs(murderer_characteristics.age - new_age) < 10:
                new_age = random.randint(1, 40)

            self.age = new_age

        if not self.height:
            new_height = random.randint(60, 160)
            while abs(murderer_characteristics.height - new_height) < 30:
                new_height = random.randint(60, 160)

            self.height = new_height

        if not self.gender:
            self.gender = "male" if (murderer_characteristics.gender == "female" and random.getrandbits(1) == 0) else "male"

        if not self.colour:
            new_colour = random.choice(["grey", "black", "brown", "blonde"])
            while new_colour == murderer_characteristics.colour:
                new_colour = random.choice(["grey", "black", "brown", "blonde"])

            self.colour = new_colour

        if not self.fur_length:
            self.fur_length = "short" if murderer_characteristics.fur_length == "long" else "long"

        if not self.likes_food:
            new_food = random.choice(["salmon", "berries", "nuts", "honey", "fruits"])
            while new_food == murderer_characteristics.likes_food:
                new_food = random.choice(["salmon", "berries", "nuts", "honey", "fruits"])

            self.likes_food = new_food


    # debugging function to print characteristic object
    def dbg_print(self):
        print("printing debug characteristic object:")
        print(f"age: {self.age}")
        print(f"height: {self.height}")
        print(f"gender: {self.gender}")
        print(f"fur length: {self.fur_length}")
        print(f"colour: {self.colour}")
        print(f"likes food: {self.likes_food}")
