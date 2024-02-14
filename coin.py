import random
class Coin:
    def __init__(self):
        self.side=None
    def flip(self):
        self.side=random.choices(["Head","Tail"])
    def __str__(self):
        if self.side:
            return f"the coin landed on: {self.side}"
        else:
            return "the coin hasn't been flipped yet"

        # the child class
class Childcoin(Coin):
    def __init__(self,tos):
        super().__init__()
        self.tos=tos
    def flip(self):
        if random.random() > self.tos:
            self.side="Head"
        else:
            self.side="Tail"
coin1=Coin()
child=Childcoin(0.7) #for the head
coin1.flip()
child.flip()
print("regular coin")
print(coin1)
print("------------")
print("\n child coin")
print(child)

class Car:
    def __init__(self,brand, model):
        self.brand=brand
        self.model=model
    def move(self):
        print("drive")
class Boat:
    def __init__(self,brand, model):
        self.brand=brand
        self.model=model
    def move(self):
        print("sail")
class Plane:
    def __init__(self,brand,model):
        self.brand=brand
        self.model=model
    def move(self):
        print("fly")
car1=Car("ford", "mustang")
boat1=Boat("st. maria", "Touring 23")
plane1=Plane("Boeing","747")
for x in (car1,boat1,plane1):
    x.move()
    





















