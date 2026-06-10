from rich.console import Console
from rich import print
from rich.markdown import Markdown
console = Console()
import time
import random


'''
In dieser Datei finden sich alle Klassen und Funktionen des Projekts
'''



#Spielerklasse
class Player:
    def __init__(self, name, sname, wpn, mag, hp, maxhp, sp, maxsp, ma, maxma, gld, magdam, wpndam, heal, pwr, pot):
        self.name = name
        self.sname = sname
        self.wpn = wpn
        self.mag = mag
        self.hp = hp
        self.maxhp = maxhp
        self.sp = sp
        self.maxsp = maxsp
        self.ma = ma
        self.maxma = maxma
        self.gld = gld
        self.magdam = magdam
        self.wpndam = wpndam
        self.heal = heal
        self.pwr = pwr
        self.pot = pot

    # Methode zum Überprüfen, ob der Maximalwert für HP, SP u. MA überschritten wurde und überschreibung
    def statchk(self):
        if self.hp > self.maxhp:
            self.hp = self.maxhp
        if self.sp > self.maxsp:
            self.sp = self.maxsp
        if self.ma > self.maxma:
            self.ma = self.maxma
        return

    # Methode zum Ausgeben der Spielerstats
    def stats(self):
        print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
        print("")
        console.print(f"Stats",style="underline")
        time.sleep(0.2)
        console.print(        f"   Name:     {self.name}{self.sname}", style="bold")
        time.sleep(0.2)
        console.print(        f"   Waffe:    {self.wpn} - {self.wpndam} physischer Schaden")
        time.sleep(0.2)
        console.print(        f"   Magie:    {self.mag} - {self.magdam} magischer Schaden")
        time.sleep(0.2)
        console.print(        f"   Kraft:    {self.hp}hp")
        time.sleep(0.2)
        console.print(        f"   Ausdauer: {self.sp}sp")
        time.sleep(0.2)
        console.print(        f"   Mana:     {self.ma}ma")
        time.sleep(0.2)
        console.print(        f"   Gold:     {self.gld}gld")
        time.sleep(0.2)
        if self.heal <= 1:
            console.print(f"   Heiltränke:              {self.heal} Trank", style = "blue")
        elif self.heal > 1:
            console.print(f"   Heiltränke:              {self.heal} Tränke", style= "blue")
        time.sleep(0.2)
        if self.pwr  <= 1:
            console.print(f"   Ausdauertränke:          {self.pwr} Trank", style = "yellow")
        elif self.pwr > 1:
            console.print(f"   Ausdauertränke:          {self.pwr} Tränke", style="yellow")
        if self.pot <= 1:
            console.print(f"   Manatränke:              {self.pot} Trank", style="magenta")
        elif self.pot > 1:
            console.print(f"   Manatränke:              {self.pot} Tränke", style="magenta")

    def healing(self):
        if self.heal > 0:
            self.hp += 10
            self.statchk()
            self.heal -= 1
            console.print(f"{self.name} spürt ein kitzeln auf der Haut, und der Schmerz ist weg.")
            console.print(f"+ 10hp", style = "green")
            return self.hp, self.heal
        else:
            print("Du hast keine Heiltränke mehr!")
            return self.hp

    def sp_up(self):
        if self.sp >= 0:
            diff = self.maxsp - self.sp
            self.sp = self.maxsp
            self.statchk()
            self.pwr -= 1
            console.print(f"{self.name} fühlt sich, als würde man nie wieder Müde werden.")
            console.print(f"+ {diff}sp", style = "green")
            return self.sp
        else:
            print("Du hast keine Ausdauertränke mehr!")
            return self.sp

    def ma_up(self):
        if self.ma >= 0:
            self.ma += 20
            self.statchk()
            self.pot -= 1
            console.print(f"{self.name} Gedanken beruhigen sich augenblicklig.")
            console.print(f"+ 20ma", style = "green")
            return self.ma
        else:
            print("Du hast keine Ausdauertränke mehr!")
            return self.ma

    def use_item(self):
            ongoing = True
            while ongoing:
                console.print(f"+------------------------------------+")
                console.print(f"|   Wähle das zunutzende Item:       |")
                console.print(f"|       Heiltrank:      {self.heal}  |")
                console.print(f"|       Ausdauertrank:  {self.pwr}   |")
                console.print(f"|       Manatrank:      {self.pot}  |")
                console.print(f"+------------------------------------+")
                item = input(f"{self.name} trinkt einen... : ")
                if item == "":
                    console.print("Wie bitte?", style = "red")
                if item.lower() == "heiltrank":
                    self.healing()
                    ongoing = False
                    return self.heal, self.pwr, self.pot, self.hp, self.sp, self.ma
                elif item.lower() == "ausdauertrank":
                    self.sp_up()
                    ongoing = False
                    return self.heal, self.pwr, self.pot, self.hp, self.sp, self.ma
                elif item.lower() == "manatrank":
                    self.ma_up()
                    ongoing = False
                    return self.heal, self.pwr, self.pot, self.hp, self.sp, self.ma
                else:
                    console.print("Wie bitte?", style="red")

    time.sleep(0.2)
    print("")
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~")

    # Methode zum Ausruhen (Nur einmal pro Zug einsetzbar)
    def rest(self):
        self.hp += 5
        self.sp += 10
        self.ma += 1
        self.statchk()
        print(f"{self.name} hat sich ausgeruht")
        time.sleep(0.2)
        console.print("+ 5hp", style = "green")
        time.sleep(0.2)
        console.print("+ 10sp", style = "green")
        time.sleep(0.2)
        console.print("+ 1ma", style="green")

    # Gegnerklasse
class Enemy:
    def __init__(self, enname, enhp, endam, engld):
        self.enname = enname
        self.enhp = enhp
        self.endam = endam
        self.engld = engld

    # Methode zum Ausgeben der Gegnerstats
    def enstats(self):
        console.print(f"Enemy Stats",style="underline")
        time.sleep(0.2)
        console.print(        f"   Name:     {self.enname}", style="bold")
        time.sleep(0.2)
        console.print(        f"   Kraft:    {self.enhp}hp")
        time.sleep(0.2)
        console.print(f"   Schaden:    {self.endam} Schaden")
        print("")
        print("~~~~~~~~~~~~~~")


# Funktion zur Charakterwahl
def character():
    chch = Markdown("""~~~
    Wie ist dein Name? 

        - Hivor
        - Said
        - Tilara
        - Khazo
    
    """)
    console.print(chch)
    chara = 0
    while chara == 0:
        print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
        char = input("")
        print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
        print("")
        if char.lower() == "hivor":
            pl = Player(name="Hivor", sname=" von Donarstad", wpn="Claymore", mag="Blitze", hp=30, maxhp=30, sp=15,
                        maxsp=15, ma=5, maxma=5, gld=50, magdam=1000, wpndam=15, heal = 3, pwr = 1, pot = 0)
            pl.stats()
            confirm = str(input("Bestätigen? (y/n): "))
            if confirm.lower() == "y":
                return pl
            else:
                console.print("Abgebrochen", style="red")
        elif char.lower() == "said":
            pl = Player(name="Said", sname=" Nahti", wpn="Bernstein-Zepter", mag="Wasser", hp=25, maxhp=25, sp=25,
                        maxsp=25, ma=30, maxma=30, gld=20, magdam=20, wpndam=5, heal = 3, pwr = 1, pot = 0)
            pl.stats()
            confirm = str(input("Bestätigen? (y/n): "))
            if confirm.lower() == "y":
                return pl
            else:
                console.print("Abgebrochen", style="red")
        elif char.lower() == "khazo":
            pl = Player(name="Khazo", sname=" Khan", wpn="2 Kiliçlar", mag="Feuer", hp=30, maxhp=30, sp=30,
                        maxsp=30, ma=15, maxma=15, gld=0, magdam=40, wpndam=20, heal = 3, pwr = 1, pot = 0)
            pl.stats()
            confirm = input("Bestätigen? (y/n): ")
            if confirm.lower() == "y":
                return pl
            else:
                console.print("Abgebrochen", style="red")
        elif char.lower() == "tilara":
            pl = Player(name="Tilara", sname="", wpn="Streitkolben", mag="Erdebeben", hp=25, maxhp=25, sp=40,
                        maxsp=40, ma=10, maxma=10, gld=40, magdam=30, wpndam=20, heal = 3, pwr = 1, pot = 0)
            pl.stats()
            confirm = str(input("Bestätigen? (y/n): "))
            if confirm.lower() == "y":
                return pl
            else:
                console.print("Abgebrochen", style="red")
        elif char.lower() == "debug":
            pl = Player(name="John", sname=" Lyrae", wpn="Fäuste", mag="Glock19", hp=int(input("HP: ")),
                        maxhp= 9999999, sp=int(input("SP: ")),
                        maxsp=9999999, ma=int(input("MANA: ")), maxma=9999999,
                        gld=int(input("Gold: ")), magdam=int(input("Mag. Schaden: ")),
                        wpndam=int(input("Phy. Schaden: ")), heal = 999999, pwr = 999999, pot = 999999)
            pl.stats()
            confirm = str(input("Bestätigen? (y/n): "))
            if confirm.lower() == "y":
                return pl
            else:
                console.print("Abgebrochen", style="red")
        else:
            console.print("Wie bitte?", style="red")
            print("")
            console.print(chch)
            continue

# Funktion zum Generieren eines Gegners
def get_enemy1():
        en = random.randint(1, 3)
        if en == 1:
            enemy = Enemy(enname="Bandit", enhp=20, endam=random.randint(5, 8), engld=random.randint(5, 10))
            return enemy
        elif en == 2 or 3:
            enemy = Enemy(enname="Perlschwein", enhp=10, endam=random.randint(7, 8), engld=random.randint(1, 2))
            return enemy

# Funktion Kampfsystem
def fighting1(pl):
    enemy = get_enemy1()
    finished = 0
    while finished == 0:
        if enemy.enhp <= 0:
            time.sleep(0.2)
            console.print("Besiegt!", style="yellow")
            pl.gld += enemy.engld
            time.sleep(0.2)
            console.print(f"Du hast {enemy.engld}gld gefunden! Du hast nun {pl.gld}gld")
            print("")
            print("~~~~~~~~~~~~~~")
            return pl
        print(f"Ein {enemy.enname} attackiert dich!")
        time.sleep(0.2)
        pl.hp -= enemy.endam
        console.print(f"{enemy.endam} Schaden genommen", style="red")
        time.sleep(0.2)
        print("")
        pl.stats()
        reacted = 0
        if pl.hp <= 0:
            console.print("Gestorben", style="red")
            input()
            return exit()
        enemy.enstats()
        while reacted == 0:
            CHOICE = f"""
                            Wie wehrst du dich?
                                - {pl.wpn} (Phy) - 5sp
                                - {pl.mag} (Mag) - 5ma
                                - item
                            """
            chc = Markdown(CHOICE)
            print("~~~~~~~~~~~~~~")
            print(chc)
            print("~~~~~~~~~~~~~~")
            answer = input()
            print("")
            if answer.lower() == "phy" and pl.sp >= 1:
                enemy.enhp -= pl.wpndam
                pl.sp -= 5
                console.print(f"Du hast {pl.wpndam} Schaden gemacht!", style="green")
                print("")
                reacted = 1
            elif answer.lower() == "phy" and pl.sp <= 0:
                print("")
                print("Du hast keine Ausdauer und dein Angriff richtet keinerlei Schaden an")
            elif answer.lower() == "mag" and pl.ma >= 1:
                enemy.enhp -= pl.magdam
                pl.ma -= 5
                console.print(f"Du hast {pl.magdam} Schaden gemacht!", style="green")
                print("")
                reacted = 1
            elif answer.lower() == "item":
                pl.use_item()
            else:
                print("Tipp: Siehe Inhalt Klammern")

def wanderer(pl):
        console.print(f"+-------------------------+")
        console.print(f"| Der wandelnde Alchemist |")
        console.print(f"+-------------------------+")

        console.print("Hallo, Reisender. Ich habe\neiniges dabei... Was brauchst du?", style="yellow")
        console.print("")
        console.print(f"+------------------------+")
        console.print(f"| Heiltrank     (-10gld) |")
        console.print(f"| Ausdauertrank (-10gld) |")
        console.print(f"| Manatrank     (-20gld) |")
        console.print(f"+------------------------+")
        console.print(f" Dein Gold: {pl.gld}")
        inprog = True
        while inprog:
            cho = input("")
            if cho == "Heiltrank":
                console.print("Gekauft: Heiltrank", style="blue")
                console.print("")
                console.print("Ich danke für deinen Einkauf...", style="yellow")
                pl.heal += 1
                pl.gld -= 10
                return pl.heal, pl.gld
            elif cho == "Ausdauertrank":
                console.print("Gekauft: Ausdauertrank", style="yellow")
                console.print("")
                console.print("Ich danke für deinen Einkauf...", style="yellow")
                pl.pwr += 1
                pl.gld -= 10
                return pl.pwr, pl.gld
            elif cho == "Manatrank":
                console.print("Gekauft: Manatrank", style="magenta")
                console.print("")
                console.print("Ich danke für deinen Einkauf...", style="yellow")
                pl.pot += 1
                pl.gld -= 20
                return pl.pot, pl.gld
            else:
                console.print("Wie bitte?", style="red")
                continue

# Funktion zum Zug
def action1(pl):
        rested = 0
        act = 0
        while act == 0:
            console.print("Was möchtest du tun?", style="yellow")
            console.print(        "   - Weiter (Weitergehen)")
            time.sleep(0.2)
            console.print("   - Ausruhen (+5sp, +1ma)")
            time.sleep(0.2)
            console.print("   - Stats (Zeigt Stats)")
            time.sleep(0.2)
            console.print("   - Suizid (Beendet das Spiel)")
            print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
            choi = input()
            print("")
            if choi.lower() == "weiter":
                act = 1
                rando = random.randint(1, 3)
                if rando == 1 or 2:
                    fighting1(pl)
                elif rando == 3:
                    wanderer(pl)
            elif choi.lower() == "stats":
                pl.stats()
            elif choi.lower() == "ausruhen" and rested == 0:
                pl.rest()
                rested = 1
            elif choi.lower() == "ausruhen" and rested == 1:
                console.print("Es ist zu gefährlich, sich so lange auszuruhen", style = "red")
            elif choi.lower() == "suizid":
                exit()
            else:
                console.print("Wie bitte?", style="red")
                print("")