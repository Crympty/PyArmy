import Python.Package.army_creator as acm
from Python.Package.army_creator import Skibidi
from typing import Union
from enum import Enum

class stats(Enum):
    NAME = 1
    SPEED = 2
    HP = 3    

def prompt_state_choice():
    try:
        choice = int(input('''Which stat do you want to know or the total of?
              \t1. Type/Name
              \t2. Speed
              \t3. Health Points(HP)
              '''))
    except Exception:
        print("not a possible response stupid")
    return Stats(choice)

def calcMaxStat() -> Union[str, float, int]:
    