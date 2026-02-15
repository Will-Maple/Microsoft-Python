class Dog:
    def __init__(self, name, breed):
        self.name = name
        self.breed = breed

    def bark(self):
        print("Woof! my name is " + self.name + " and I'm a " + self.breed)

my_dog = Dog("Maple", "Mutt")

my_dog.bark()