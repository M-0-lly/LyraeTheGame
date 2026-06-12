import classes
from classes import *
console = Console()

'''
In dieser Datei befinden sich sämtliche Storyelemente
'''

ttlcrd = Markdown("""
### Lyrae the Game
""")


prl1 = ("""+--------------------------------------------------------+
| Du bewegst dich durch die eisigen Weiten               |
| des großen Grallbag-Gebirges, auf der Spitze Lyraes.   |
| In sehnsucht nach Wärme suchst du schon seit einem Tag |
| nach einen Unterschlupf.                               |
| Was sollst du nur tun?                                 |
+--------------------------------------------------------+\n""")

prl2 = ("""+-------------------------------------------------------+\n
| Hinter einer dichten Winddecke kannst du Licht in der |\n
| Ferne erkennen. Du bekommst Hoffnung auf Obdach.      |\n
+-------------------------------------------------------+\n""")

prl3 = (f"""+-----------------------------------------------------------------+\n
| Die Lichter werden dir immer näher. Ist es ein Dorf? Ein Lager? |\n
| Ein Feuer scheint es zumindest zu geben.                        |\n
+-----------------------------------------------------------------+\n""")

prl4 = ("""+-----------------------------------------------------------------+\n
| Es ist ein Dorf! Entlang eines verschneiten Weges konntest du   |\n
| ein Schild erkennen: Morghorn.                                  |\n
+-----------------------------------------------------------------+\n""")
prologue = [prl1, prl2, prl3, prl4]


def storyprologue(pl):
    console.print(ttlcrd)
    event = 0
    eventchance = random.randint(1, 4)
    for i in prologue:
        time.sleep(0.1)
        console.print("Prolog", style="bold underline yellow")
        console.print(i)
        classes.action1(pl)
        event += 1
        if event == eventchance:
            time.sleep(0.1)
            console.print("Aus dem eisigen Nebel siehst du eine Sillhouette hervortreten...", style="blue")
            time.sleep(0.1)
            wanderer(pl)