# Class of SuperClass and Polimorphy
class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        pass

    def move(self):
        pass

# Mixin for animals that can fly
class Flyer:
    def fly(self):
        return f"{self.name} is flying."

# Mixin for animals that can swim
class Swimmer:
    def swim(self):
        return f"{self.name} is swimming"

# Subclass Dog that overrides the speak and move methods
class Dog(Animal):
    def speak(self):
        return "Woof!"

    def move(self):
        return f"{self.name} is walking."

# Subclass Cat that overrides the speak and move methods
class Cat(Animal):
    def speak(self):
        return "Meow!"

    def move(self):
        return f"{self.name} is walking."

# Subclass Cow that overrides the speak and move methods
class Cow(Animal):
    def speak(self):
        return "Moo!"

    def move(self):
        return f"{self.name} is walking."

# Subclass Duck that inherits from Animal, Flyer, and Swimmer
class Duck(Animal, Flyer, Swimmer):

    def speak(self):
        return "Quack!"

    def move(self):
        return f"{self.walk()}, {self.swim()} AND {self.fly()}"

    def walk(self):
        return f"{self.name} is walking"

class Alligator(Animal, Swimmer):
    def move(self):
        return f"{self.walk()} AND  {self.swim()}"

    def walk(self):
        return f"{self.name} is walking"

# Function that uses polymorphism to call the speak method
def make_sound(animal):
    return animal.speak()

# Function that uses polymorphism to call the move method
def make_move(animal):
    return animal.move()

# Instances of the classes
dog = Dog('Lug')
cat = Cat('Snowball')
cow = Cow('Daisy')
duck = Duck("Donald Duck")
alligator = Alligator('Totodyle')

# Calling the polymorphic methods
print(make_sound(dog))   # Output: Woof!
print(make_sound(cat))   # Output: Meow!
print(make_sound(cow))   # Output: Moo!
print(make_sound(duck))  # Output: Quack!
print()
print(make_move(dog))    # Output: Lug is walking.
print(make_move(cat))    # Output: Snowball is walking.
print(make_move(cow))    # Output: Daisy is walking.
print(make_move(duck))   # Output: Donald Duck is walking, Donald Duck is swimming AND Donald Duck is flying.
print(make_move(alligator)) # Output: The Totodyle is walking and swimming
