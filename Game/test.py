from classes import Player

pl = Player(name="Hivor", sname=" von Donarstad", wpn="Claymore", mag="Blitze", hp=30, maxhp=999999, sp=15,
                        maxsp=15, ma=5, maxma=5, gld=10, magdam=1000, wpndam=15, heal = 0, pwr = 1, pot = 0)


def healpot():
    if pl.heal > 0:
        pl.hp += 10
        pl.statchk()
        pl.heal -= 1
        return pl
    else:
        print("Keine Tränke mehr!")
        return pl

def store():
    inprog = 0
    while inprog == 0:
        print("Willkommen im Shop")
        print(f"{pl.gld}gld")
        cho = input("Was darf es sein?")
        if cho.lower() == "heiltrank" and pl.gld >= 5:
            pl.heal += 1
            pl.gld -= 5
        elif cho.lower() == "heiltrank" and pl.gld <= 4:
            print("Wo ist meine Kohle?")
            print("Raus hier!")
            inprog += 1
            return pl
        elif cho.lower() == "gehen":
            print(f"{pl.name} geht.")
            inprog += 1
            return pl
        else:
            print("Wie bitte?")
store()

while pl.heal >= 0:
    if pl.heal > 0:
        healpot()
    elif pl.heal == 0:
        "Keine Tränke mehr!"
        break
    print(f"{pl.hp} HP")