

class FactInventory:
    def __init__(self, player):
        self.info = []
        self.owner = player

    def add_info(self, fact_string):
        if not fact_string in self.info:
            self.info.append(fact_string)
            self.owner.send_evidence(fact_string)

    def get_info(self):
        return self.info

