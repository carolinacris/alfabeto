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
    "a": "đ°",
    "b": "đą",
    "c": "ÂŠī¸",
    "d": "đ",
    "e": "đĨ¨",
    "f": "đŗī¸",
    "g": "đŊ",
    "h": "đž",
    "i": "đĄ",
    "j": "đ§đģââī¸",
    "k": "đ¤žđŧââī¸",
    "l": "đ",
    "m": "â°ī¸",
    "n": "đ",
    "o": "đą",
    "p": "đĒī¸",
    "q": "đ¤ī¸",
    "r": "ÂŽī¸",
    "s": "đ",
    "t": "đ",
    "u": "đĒą",
    "v": "âī¸",
    "w": "đ¤ŧââ",
    "x": "âī¸",
    "y": "âđģ",
    "z": "đ¤"
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