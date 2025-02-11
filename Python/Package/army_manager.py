from Package import army_creator as acm
from .army_creator import Skibidi
from typing import Union
from enum import Enum

class stats(Enum):
    NAME = 1
    SPEED = 2
    HP = 3    

def prompt_stat_choice():
    try:
        choice = int(input('''Which stat do you want to know or the total of?
              \t1. Type/Name
              \t2. Speed
              \t3. Health Points(HP)
              '''))
    except Exception:
        print("not a possible response")
    return Stats(choice)

def calcMaxStat(arr: list[Skibidi], stat: stats) -> Union[str, float, int]:
    match stat:
        case stats.NAME:
            calculate(stats.NAME, arr)
        case stats.SPEED:
            calculate(stats.SPEED, arr)
        case stats.HP:
            calculate(stats.HP, arr)



    def calculate(stat: stats, arr: list[Skibidi]) -> Union[str, int, float]:
        rLst = []
        if (stat == stats.NAME):
            rLst = [Skibidi.name for Skibidi in arr]
            return rLst
        if (stat == stats.HP):
            return sum([Skibidi.hp for Skibidi in arr])
        if (stat == stats.SPEED):
            return sum([Skibidi.speed for Skibidi in arr])

