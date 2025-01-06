# from multipledispatch import dispatch 
from Package.ArmyCreatorModule import promptCreation, Skibidi
import numpy as np

def main():
    print("yahallo! construct ur skibidi army!!!!")
    

if __name__ == "__main__":
    soldiers = int(input("how many skibidi do u want to construct? \n"))
    armyArr: list[Skibidi] = []
    for _ in range(soldiers):
        armyArr.append(promptCreation())