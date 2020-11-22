class Entity:
    name = ""
    status = "Alive"
    health = 0
    heal_rate = 0
    base_damage = 0
    equipped = None

    def heal(self):
        self.health += self.heal_rate

    def attack(self, enemy):
        if enemy.status == "Alive":
            if self.equipped is not None:
                damage = self.equipped.damage
            else:
                damage = self.base_damage
            enemy.health -= damage
            enemy.check()

    def check(self):
        if self.health <= 0:
            self.health = 0
            self.status = "Dead"

    def equip(self, item):
        self.equipped = item

    def __repr__(self):
        return "Entity: {}, Status: {}, Health: {}, Equipped: {}".format(
            self.name, self.status, self.health, self.equipped
        )
