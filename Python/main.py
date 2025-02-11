from Package.army_creator import prompt_creation, Skibidi
from Package import army_manager
import numpy as np

def main():
    print("yahallo! construct ur skibidi army!!!!")
    

if __name__ == "__main__":
    main()
    soldiers = int(input("how many skibidi do u want to construct? \n"))
    army_arr: list[Skibidi] = []
    for _ in range(soldiers):
        army_arr.append(prompt_creation())
    
    end_condition: bool = False
    
    while not end_condition:
        choice = int(input('''Which of the following would you like to do? (Type number; ex: "1") 
              \t 1. Get Stats
              \t 2. Fight battle
              \t 3. Idfk
              '''))
        
        match choice:
            case 1:
                army_manager.calcMaxStat(army_manager.prompt_stat_choice())
                
                pass
            case 2:
                end_condition = True
                #insert battle method
            case _:
                print("That was NOT a choice, pls try number option from the choices.")