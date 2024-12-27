class Skibidi:
    def __init__(self, type: str, speed: int):
        self.type = type
        self.speed = speed

    

demon1: Skibidi = Skibidi("SpeedDemon", 500)
print(demon1.type)