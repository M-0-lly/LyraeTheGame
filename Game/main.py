
'''
Main-Datei des Spiels
'''

# Import
from rich.console import Console
from rich import print
console = Console()
console.print("rich loaded", style="green")
import time
console.print("classes loaded", style="green")
import story
console.print("story loaded", style="green")
from classes import *
import classes
console.print("classes loaded", style="green")
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
