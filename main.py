
'''
Main-Datei des Spiels
'''

# Import
from rich.console import Console
console = Console()
import story
from classes import *
import classes
print("")
print("")

#Titelcard
console.print("Lyrae The Game", style="bold underline yellow")
console.print("by Tom Steinbach", style="italic magenta")
print("")

# Charakterwahl
pl = classes.character()
console.print("Bestätigt", style="green")
time.sleep(1)
print("")

# PROLOG
time.sleep(1)
story.storyprologue(pl)
