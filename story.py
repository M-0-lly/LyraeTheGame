import classes
from classes import *
console = Console()

'''
In dieser Datei befinden sich sämtliche Storyelemente
'''


prl1 = ("""+--------------------------------------------------------+
| Du bewegst dich durch die eisigen Weiten               |
| des großen Grallbag-Gebirges, auf der Spitze Lyraes.   |
| In sehnsucht nach Wärme suchst du schon seit einem Tag |
| nach einem Unterschlupf.                               |
| Außer weiterzugehen, bleiben dir nicht viele Optionen. |
+--------------------------------------------------------+\n""")

prl2 = ("""+--------------------------------------------------------+
| Entlang des Weges findest du einen Wegweiser mit       |
| einer Weisung: "Morghorn".                             |
| Der Frost auf deinem Körper treibt dich an,            |
| die Richtung einzuschlagen. Die Reflexion der Sonne im |
| Schnee brennt in deinen Augen, während du versuchst    |
| den Weg im Schnee zu finden.                           |
+--------------------------------------------------------+\n""")

prl3 = (f"""+--------------------------------------------------------+
| Fern durch den Nebel erkennst du flackernde Lichter.   |
| Endlich findest du die Zuversicht nicht zu erfrieren!  |
| Und natürlich ist das nicht dein Ende, du bist         |
| immerhin der Protagonist!                              |
+--------------------------------------------------------+\n""")

prl4 = ("""+--------------------------------------------------------+
| Morghorn ist nicht mehr weit, dennoch hast du ein      |
| unwohles Gefühl, als würde bald etwas passieren.       |
| Du bleibst fest auf Grund und Stelle stehen, um dich   |
| umzusehen, aber: nichts.                               |
| Vor dir siehst du nur einen Hügel.                     |  
+--------------------------------------------------------+\n""")
prologue = [prl1, prl2, prl3, prl4]


def storyprologue(pl):
    console.print(f"                    Lyrae The Game", style = "red")
    event = 0
    eventchance = random.randint(1, 4)
    for i in prologue:
        time.sleep(0.1)
        console.print("                         Prolog", style="bold underline yellow")
        console.print(i)
        classes.action1(pl)
        event += 1
        if event == eventchance:
            wanderer(pl)
    prologue_boss(pl)