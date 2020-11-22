from items import item


class Weapon(item.Item):
    prefix = ""
    damage = 0
    attack_speed = 16
    mana_consumption = 0

    def __init__(self):
        self.type = "weapon"

    def __repr__(self):
        return "{0}, dmg: {1}".format(" ".join([self.prefix, self.name]), self.damage)

    def get_text(self):
        return (
            f"Weapon: {0} {1}, Damage: {2}, Attack Speed: {3}",
            self.prefix,
            self.name,
            self.damage,
            self.attack_speed,
        )


class WoodenSword(Weapon):
    def __init__(self):
        self.name = "Wooden Sword"
        self.prefix = ""
        self.damage = 7


class Zenith(Weapon):
    def __init__(self):
        self.name = "Zenith"
        self.prefix = "Godly"
        self.damage = 190


class TerraBlade(Weapon):
    def __init__(self):
        self.name = "Zenith"
        self.prefix = "Legendary"
        self.damage = 172


class LastPrism(Weapon):
    def __init__(self):
        self.name = "Last Prism"
        self.prefix = "Demonic"
        self.attack_speed = 10
        self.damage = 100