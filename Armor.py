class Armor(object):
    self.durability
    self.ArClModifier

class RustyIronArmor(Armor):
    def __init__(self):
        self.durability = 20
        self.ArClModifier = 4


class NewIronArmor(Armor):
    def __init__(self):
        self.durability = 35
        self.ArClModifier = 8
