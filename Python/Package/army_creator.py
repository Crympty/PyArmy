class Skibidi: 
    def __init__(self, name = "default", speed = 20.0, hp = 100):
        self.type = name
        self.speed = speed
        self.hp = hp

    @classmethod
    def intInit(cls, type: str, speed: int, hp: int):
        return cls(type, speed, hp)


def prompt_creation() -> Skibidi:
    default:bool = input("want use default? True if yes, anything else is no").strip().lower() == "true" 
    if(default == True):
        return Skibidi.intInit("default", 20, 100)

    name = input("name of skibidi: ")
    speed = float(input("speed of skibidi: "))
    hp = int(input("hp of skibidi: "))

    return Skibidi(name, speed, hp)

if __name__ == "__main__":
    print("uh oh, something went wrong");