import random
import json #per leggere un json
import pprint
import sys #per leggere l'imput
from this import s
# input utente 
#import sys
# i = " ".join(sys.argv[1:])
# io devo concvettire una stringa in una fatta di emoji. devo fare un dizionario con le emoji. me lo metto in un file a parte e mi scrivo tutto l'afabeto
#ora devo fare una funzione una volta che funziona in riga fi terminale possiamo postarla su vercel per creare un interfaccia.
data = {
    "a": "🅰",
    "b": "🅱",
    "c": "©️",
    "d": "🍙",
    "e": "🥨",
    "f": "🏳️",
    "g": "💽",
    "h": "💾",
    "i": "💡",
    "j": "🧜🏻‍♀️",
    "k": "🤾🏼‍♀️",
    "l": "🏒",
    "m": "⛰️",
    "n": "📈",
    "o": "🎱",
    "p": "🌪️",
    "q": "🌤️",
    "r": "®️",
    "s": "🐍",
    "t": "🍄",
    "u": "🪱",
    "v": "✔️",
    "w": "🤼‍♂",
    "x": "⚔️",
    "y": "✌🏻",
    "z": "💤"
}


def main():
    i = "".join(sys.argv[1:]) #prendi dal primo in poi
    o = emojify(i)
    print(o)

def emojify():
    string= string.upper
    #rimpiazzo 


app = FastAPI()
app.add_middle