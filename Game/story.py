from rich.console import Console
from rich.markdown import Markdown
import classes
console = Console()

'''
In dieser Datei befinden sich sämtliche Storyelemente
'''

ttlcrd = Markdown("""
### Lyrae the Game
""")


prl1 = Markdown("""
~~~
Du bewegst dich durch die eisigen Weiten
des großen Grallbag-Gebirges, auf der Spitze Lyraes. 
In sehnsucht nach Wärme suchst du schon seit einem Tag
nach einen Unterschlupf.
Was sollst du nur tun?
~~~ 
""")

prl2 = Markdown("""
~~~
Hinter einer dichten Winddecke kannst du Licht in der 
Ferne erkennen. Du bekommst Hoffnung auf Obdach.
~~~
""")

prl3 = Markdown(f"""
~~~
Die Lichter werden dir immer näher. Ist es ein Dorf? Ein Lager?
Ein Feuer scheint es zumindest zu geben.
~~~
""")

prl4 = Markdown("""
~~~
Es ist ein Dorf! Entlang eines verschneiten Weges konntest du
ein Schild erkennen: Morghorn.
~~~
""")
prologue = [prl1, prl2, prl3, prl4]

def storyprologue(pl):
    console.print(ttlcrd)
    for i in prologue:
        console.print("Prolog", style="bold underline yellow")
        console.print(i)
        classes.action1(pl)