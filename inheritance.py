class Vehicle:
    def move(self):
        print("Moving")
class Car(Vehicle):
    def wheel(self):
        print("4 wheels")
c=Car()
c.move()
c.wheel()

