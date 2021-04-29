import random
import os
import sqlite3
from inventory import *
import pickle

dang = None
s= None


class Character:

    def __init__(self, clas):
        self.name = "you"
        self.mani = 200
        self.level = 1
        self.levelUP =0 
        self.defense = 1
        if clas == "1":
            self.clas = "warrior"
            self.name = input("Введите имя персонажа: ")
            self.maxHP = (self.level * 200)
            self.hp = 180
            self.stats = 10
            self.weapon = fist()
            self.inventory = [item("potion"), item("potion") ]

        if clas == "2":
            self.clas = "magican"
            self.name = input("Введите имя персонажа: ")
            self.hp = 120
            self.stats = 25
            self.weapon = 45
            self.inventory = [item("armor")]
    
        if clas == "3":
            self.clas = "archer"
            self.name = input("Введите имя персонажа: ")
            self.hp = 100
            self.stats = 30
            self.weapon = 50
            self.inventory = [item("armor")]

    def MenuCharacter(self):
        #print("\nСила: " + str(self.stats))
        print("Жизни:" + str(self.hp))
        print("Оружие: " + str(self.weapon.name))
        print("Дамаг оружия: " + str(self.weapon.damage))
        print("Уровень: " + str(self.level) + "\n")

    def Inventory(self):
        print("\nВаш инвентарь: " )
        self.inventory = sorted(self.inventory, key=lambda x: x.cost, reverse=True)
        for i in self.inventory:
            print(i.name + "    стоимость: "+ str(i.cost))
        print("\n   Ваши деньги:" + str(self.mani))
    
    def Help(self):
        print("\nstate - статы, \nclose - вернуться \n 1 - спустится в шахту \n re - перековать руду в слитки\n store - пойти в магазин \n ")
    
    def checkWeapon(self):
        try:
            o = []
            for i in self.inventory:
                if i.type == "weapon":
                    o.append(i)
            o = sorted(o, key=lambda x: x.damage, reverse=True)
            self.weapon = o[0]
        except BaseException:
            self.weapon = fist() 

    def bash(self, enemy):
        self.checkWeapon()
        dmg = random.randint(int(self.weapon.damage * (self.level * 0.9)), int(self.weapon.damage * self.level))
        enemy.hp -= dmg
        print("ты нанёс " + str(dmg)+ "урона ")

    def defens(self):
        self.defense = 0.5

    def healPotion(self):
        p = 0
        for i in self.inventory:
            if i.item == "potion" or i.item == "meat":
                if self.maxHP > self.hp:
                    self.hp += i.ragen    
                    self.inventory.pop(p)
                    break
                else: print("У вас максимальное каличество хп")
            p += 1
        print("у вас нету лечилок")        


class Mine:
    def __init__(self, level):
        self.level = level
        if level == "1":
            print("Вы спустились на 1 уровень щахты! ")

        if level == "2":
            print("Вы спустились на 2 уровень шахты! ")

        if level == "3":
            print("Вы спустились на 3 уровень шахты! ")

    def randomBattle(self, player, dif):
        rand = random.randint(0, 100)
        if rand >0 and rand <31:
            b = battle()
            b.battle(player, dif)

    def Booty(self, player):

        ore = random.randint(0, 100)
        if self.checkPick(player) != True: 
            print("У вас нету кирки, купите её в магазине")
            return 1 
        if self.level == "1":
            if ore >= 10 and ore < 50:
                self.randomBattle(player, 1)
                player.inventory.append(item("iron"))
                print("Вы получили Железную руду ")
      
        if self.level == "2":
            if ore >= 10 and ore < 50:
                self.randomBattle(player, 2)
                print("Вы получили Железную руду ")
                player.inventory.append(item("iron"))
            elif ore >= 51 and ore < 78:
                self.randomBattle(player, 2)
                print("Вы получили Серебро ")
                player.inventory.append(item("silver"))

        if self.level == "3":
            if ore>= 35 and ore < 58:
                self.randomBattle(player, 3)
                print("Вы получили Железную руду ")
                player.inventory.append(item("iron"))
            if ore>= 51 and ore < 71:
                self.randomBattle(player, 3)
                print("Вы получили Серебро ")
                player.inventory.append(item("silver"))
            if ore>= 66 and ore < 88:
                self.randomBattle(player, 3)
                print("Вы получили Золото ")
                player.inventory.append(item("gold"))

    def checkPick(self, player):
        for i in player.inventory:
            if i.name == "Pick":
                return True
            else: continue

    
class store:
    
    def __init__(self):
        self.coof = 1.5
        self.pul = [item("gold"),item("pick"), item("pick"), item("dagger"), item("knuckle"), 
                    item("potion"), item("potion"), item("potion"), item("potion"), item("potion"), item("potion") ]

    def bay(self, player):
        while 1:

            print("\nВы можете купить: ")
            for i in self.pul:
                print(i.name + "    стоимость: "+ str(int(i.cost* self.coof)))
            print("У вас есть:"+str(player.mani)+"    монет")
            inp = input("\n\n введите то что хотите купить: \n")
            p=0
            if inp.lower() == "exit":
                break

            for i in self.pul:
                if i.item == inp.lower():
                    if player.mani >= int(i.cost * self.coof):

                        player.mani -=int(i.cost * self.coof)
                        player.inventory.append(i)
                        self.pul.pop(p)
                        break
                p +=1
            
    def sell(self, player):
        while 1:
            player.inventory = sorted(player.inventory, key=lambda x: x.cost, reverse=True)
            print("Что хотите продать???")
            player.Inventory()
            print("У вас есть:"+str(player.mani)+"    монет")
            inp = input("\n\n введите то что хотите продать: \n")
            p=0
            if inp.lower() == "exit":
                break

            for i in player.inventory:
                if i.item == inp.lower():
                    player.inventory.pop(p)
                    player.mani += int(i.cost)
                    break
                p +=1
            

class blacksmith:
    def __init__(self):
        pass

    def checkOre(self, ore, player):
        re = []
        p=0
        for i in player.inventory:
                if i.item == ore  :
                        re.append(p)
                        print(re)
                        if len(re) == 5:
                            player.inventory.append(item(i.item+"bar"))
                            print("перековал")
                            for ir in re:
                                p=0
                                for i in player.inventory:
                                    
                                    if i.item == ore:
                                        print(i.name)
                                        player.inventory.pop(p)
                                        print("уничтожил")
                                        break
                                    p +=1   
                            break

    def blacksmith(self, player):
        self.checkOre("iron", player)
        self.checkOre("silver", player)
        self.checkOre("gold", player)
        player.inventory = sorted(player.inventory, key=lambda x: x.cost, reverse=True)


class battle:

    def __init__(self):
        self.enemyList = []

    def killEnemy(self, enemy, player):
        print("Вы получаете: \n опыта: "+ str(enemy.backEXP))
        player.levelUP += enemy.backEXP
        print(" денег:" + str(enemy.mani))
        player.mani += enemy.mani
        mor = random.choice(enemy.range)
        print(" предмет: " + str(mor.name))
        player.inventory.append(mor)
        if player.levelUP > player.level * 100:
            player.level +=1   
            player.levelUP = 0
    
    def viewBattle(self, enemy, player):
        print(str(enemy.name)+ "\n жизни врага"+ str(enemy.hp)+ "\n жизни игрока"+ str(player.hp))    
        inp = input(" 1 - bash\n 2 - defens\n 3 - heal self\n 4 - run\n")
        return inp

    def inputPlayer(self, enemy, player):
        player.defense = 1
        while player.hp > 0 :
            
            inp = self.viewBattle(enemy, player)
            
            if inp == "1":
                player.bash(enemy)
            if inp == "2":
                player.defens()
            if inp == "3":
                player.healPotion()
            if inp == "4":
                print("Ты сбежал как трус")
                break
            if enemy.hp <= 0 :
                print("Ты победил : "+ enemy.name)
                self.killEnemy(enemy, player)
                break
            enemy.attack(player)
            if player.hp <= 0:
                print("!!!You dead!!!")
                exit()

    def battle(self, player, dificalty):

        print("START BATTLE")
        if dificalty < 2:
            enemy = mobs(random.choice(mobs().mobeList1), player)
            self.inputPlayer(enemy, player)

        if dificalty == 2:
            enemy = mobs(random.choice(mobs().mobeList1+ mobs().mobeList2), player)
            self.inputPlayer(enemy, player)

        if dificalty == 3:
            enemy = mobs(random.choice(mobs().mobeList1 + mobs().mobeList2 + mobs().mobeList2 + mobs().mobeList3), player)
            self.inputPlayer(enemy, player)

        
                      


if __name__ == "__main__":
    while 1 :
        try:
            print("\nДобро пожаловать искатель!")
            print("Выберите действие для начала игры!")
            print("\n1 - Продолжить игру")
            print("2 - Новая игра")
            choice = input(": ")
            if choice == "1":
                with open('save.game', 'rb') as f:
                    player = pickle.load(f)
                    break
            if choice == "2":
                player = Character(input("Выберите класс:  \n1-warrior \n2-magican \n3-archer \n"))
                print("\nПриветствую " + player.name + "\nВы выбрали класс " + player.clas)
                break
        except BaseException:
            continue

    while True:
        try:
            helpe = input("\nВведите команду help получения информации: ")
            if helpe == "help":
                player.Help()
            
            if helpe == "chk":
                player.checkWeapon()

            if helpe == "state":
                player.MenuCharacter()

            if helpe == "close":
                break

            if helpe == "inventory":
                player.Inventory()

            if helpe == "b":
                b = battle()
                b.battle(player, 3)
            if helpe == "heal":
                player.healPotion()

            if helpe == "get":
                player.inventory.append(item(input("select item")))

            if helpe == "chet":
                for r in range(0, 10):
                    player.inventory.append(item("gold"))
                for r in range(0, 10):
                    player.inventory.append(item("silver"))
                for r in range(0, 10):
                    player.inventory.append(item("iron"))
            
            if helpe == "1":
                dang = Mine("1")

            if dang != None:

                if helpe == "mine":
                    dang.Booty(player)

                if helpe == "exit":
                    dang = None

                if helpe == "2":
                    dang = Mine("2")

                if helpe == "3":
                    dang = Mine("3")    

            if helpe == "store":
                s = store()
                checkStore = input("1 - купить \n2-продать")
                if checkStore == "1":
                    s.bay(player)
                elif checkStore == "2":
                    s.sell(player)
            
            if helpe=="re":
                bl = blacksmith()
                bl.blacksmith(player)

            if helpe == "save":
                with open('save.game', 'wb') as f:
                    pickle.dump(player, f)
        except BaseException:
            print("error")