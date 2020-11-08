class Dog:
    def __init__(self, happy=50, hungry=50, tired=50):
        self.happy = happy
        self.hungry = hungry
        self.tired = tired
        self.sleeping = False

    def change_happiness(self, amount):
        self.happy += amount

    def change_hunger(self, amount):
        self.hungry += amount

    def change_tiredness(self, amount):
        self.tired += amount

    def get_stats(self):
        return {
            "happy": self.happy,
            "hungry": self.hungry,
            "tired": self.tired,
        }
