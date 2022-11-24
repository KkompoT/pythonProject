class Auto:

    def __init__(self, brand, age: int, color, mark, weight):
        self.brand = brand
        self.age = int(age)
        self.color = color
        self.mark = mark
        self.weight = weight

    def move(self):
        print("move")

    def birthday(self):
        self.age += 1


    def stop(self):
        print("stop")


    def show_birthday(self):
        print(self.age)


car1 = Auto("vw", 10, "black", "pas", "2")
car1.move()
car1.birthday()
car1.stop()

