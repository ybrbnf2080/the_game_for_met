import random

class item():

    def __init__ (self, item):
        self.type = "pop"
        if item == "armor":
            self.item = item
            self.name = "armor"
            self.defens = 50
            self.cost = 100

        elif item == "potion":
            self.item = item
            self.name = "Potion"
            self.ragen = 60
            self.cost = 5

        elif item == "knuckle":
            self.type = "weapon"
            self.item = item
            self.name = "Knuckle"
            self.damage = 20
            self.cost = 100
        elif item == "sword":
            self.type = "weapon"
            self.item = item
            self.name = "Sword"
            self.damage = 70
            self.cost = 500

        elif item == "dagger":
            self.type = "weapon"
            self.item = item
            self.name = "Dagger"
            self.damage = 200
            self.cost = 1000
        
        elif item == "katana":
            self.type = "weapon"
            self.item = item
            self.name = "Katana"
            self.damage = 700
            self.cost = 5000

        elif item == "  ":
            self.item = item
            self.name = "krea"
            self.damage = 50
            self.cost = 100

        elif item == "meat":
            self.item = item
            self.name = "Meat"
            self.ragen = 200
            self.cost = 300

        elif item == "pick":
            self.item = item
            self.name = "Pick"
            self.damage = 15
            self.cost = 50

        elif item == "iron":
            self.type = "ore"
            self.item = item
            self.name = "iron"
            self.cost = 15

        elif item == "silver":
            self.type = "ore"
            self.item = item
            self.name = "silver"
            self.cost = 60

        elif item == "gold":
            self.type = "ore"
            self.item = item
            self.name = "gold"
            self.cost = 120

        elif item == "ironbar":
            self.item = item
            self.name = "ironbar"
            self.cost = 50

        elif item == "silverbar":
            self.item = item
            self.name = "silverbar"
            self.cost = 100

        elif item == "goldbar":
            self.item = item
            self.name = "goldbar"
            self.cost = 500
        else: 
            self.item = "kosachoks"
            self.name = "Kosachok"
            self.cost = 99999 

class fist():
    def __init__(self):
        self.type = "weapon"
        self.name = "Fist"
        self.damage = 5


class mobs:
    
    def __init__(self, name = "lol", player = "lol"):
        self.mobeList1 = ["slime"]
        self.mobeList2 = ["goblin"]
        self.mobeList3 = ["ork"]
        if name == "slime":
            self.level = 1
            self.name = name
            self.damage = 10 * (player.level * 1.1)
            self.mani = 30
            self.hp = 50 * (player.level * 1.5)
            self.range = [item("silver"), item("potion")]
            self.backEXP = 20

        if name == "goblin":
            self.level = 2
            self.name = name
            self.damage = 40 * (player.level * 0.5)
            self.mani = 100
            self.hp = 150 * (player.level * 1.5)
            self.range = [item("silver"), item("potion"), item("meat")]
            self.backEXP = 50

        if name == "ork":
            self.level = 3
            self.name = name
            self.damage = 100 * (player.level * 0.5)
            self.mani = 700
            self.hp = 500 * (player.level * 1.5)
            self.range = [item("gold"), item("silver"), item("meat")]
            self.backEXP = 300

    def attack(self, player):
        dmg = int(random.uniform(self.damage *  0.9, self.damage * 1.3 ) * player.defense)
        player.hp -= dmg
        print(self.name + " нанес вам: " + str(dmg) + " урона")