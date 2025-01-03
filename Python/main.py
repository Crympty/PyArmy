from multipledispatch import dispatch

class Skibidi:
    @dispatch(str, float, int)
    def __init__(self, type: str, speed: float, hp: int):
        self.type = type
        self.speed = speed
        self.hp = hp

    
def promptCreation() -> Skibidi:
    type = input("type of skibidi: ")
    speed = float(input("speed of skibidi: "))
    hp = int(input("hp of skibidi: "))
    skibidi = Skibidi(type, speed, hp)

    return Skibidi(type, speed, hp)


if __name__ == "__main__":
    print("yahallo! construct ur skibidi army!!!!")
    soldiers = int(input("how many skibidi do u want to construct? "))
    armyArr: Skibidi = []
    for i in range(soldiers):
        armyArr.append(promptCreation())