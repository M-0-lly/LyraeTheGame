from classes import Player

pl = Player(name="Hivor", sname=" von Donarstad", wpn="Claymore", mag="Blitze", hp=30, maxhp=40, sp=15,
                        maxsp=15, ma=5, maxma=5, gld=4, magdam=1000, wpndam=15)

healavbl = 0

def heal():
    global healavbl
    if healavbl > 0:
        pl.hp += 10
        pl.statchk()
        healavbl -= 1
        return pl.hp
    return pl.hp

def store(pl):
    global healavbl
    inprog = 0
    while inprog == 0:
        print("Willkommen im Shop")
        cho = input("Was darf es sein?")
        if cho.lower() == "heiltrank" and pl.gld >= 5:
            healavbl += 1
            pl.gld -= 5
            return healavbl
        elif cho.lower() == "heiltrank" and pl.gld <= 4:
            print("Wo ist meine Kohle?")
            print("Raus hier!")
            return healavbl

store(pl)
heal()
print(pl.hp)
print(healavbl)