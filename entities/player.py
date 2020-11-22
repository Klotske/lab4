from entities import entity


class Player(entity.Entity):
    def __init__(self, name, health=100):
        self.name = name
        self.health = health
        self.heal_rate = 10
        self.base_damage = 5

    def __repr__(self):
        return "Player: {}, Health: {}, Equipped: {}".format(
            self.name, self.health, self.equipped
        )
