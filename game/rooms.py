from enum import Enum


# Basic room enum
class Room(Enum):
    HALL = 0
    KITCHEN = 1
    DINING_ROOM = 2
    LIVING_ROOM = 3
    GARAGE = 4
    BEDROOM = 5
    ENSUITE = 6


    # Function to return enum as a formatted string
    def __str__(self):
        return self.name.replace("_", " ").title()


    # Function to return possible moves from a given room
    def get_moves(self):
        if self == Room.HALL:
            return [Room.KITCHEN, Room.LIVING_ROOM, Room.BEDROOM, Room.GARAGE]

        if self == Room.KITCHEN:
            return [Room.DINING_ROOM, Room.HALL]

        if self == Room.DINING_ROOM:
            return [Room.KITCHEN]

        if self == Room.LIVING_ROOM:
            return [Room.HALL]

        if self == Room.GARAGE:
            return [Room.HALL]

        if self == Room.BEDROOM:
            return [Room.ENSUITE, Room.HALL]

        if self == Room.ENSUITE:
            return [Room.BEDROOM]

        return [Room.HALL]
