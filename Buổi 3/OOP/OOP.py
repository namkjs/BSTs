class Animal:
    def __init__(self, name, species, sound):
        self.name = name
        self.species = species
        self.sound = sound

    def make_sound(self):
        print(f"{self.name} the {self.species} says {self.sound}!")

dog = Animal("DoDo", "dog", "Gâu Gâu")
cat = Animal("Apple Meow Meow", "cat", "meow")

dog.make_sound()
cat.make_sound()