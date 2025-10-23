# object oriented programming

# (define-struct dog [fur_color name age favorite_food])

class Dog:
    """A simple Dog class to learn OOP
    
    Attributes:
    fur_col - color of the dog's fur
    name - name of the dog
    age - age of the dog
    fav_food - favorite food"""

    def __init__ (self, fur_color, name, age, fav_food):
        """initialize new zawg"""
        #python: instance var are done inside the constructor
        self.fur_color = fur_color
        self.name = name
        self.age = age
        self.fav_food = fav_food
    

    def __str__(self):
        """return a string representation of a dog"""
        return f"{self.name} is a {self.age} year old {self.fur_color} dog who loves {self.fav_food}"

    def bark(self):
        #make the dog bark
        return f"{self.name} says guau guau!!!"
    



myZawg = Dog("black and white", "hacker", 2, "tortillas")
myOtherZawg = Dog("peach and white", "dumbo", 1, "anything edible")
print(myZawg)
print(myOtherZawg)

print (f"{myZawg.bark()} \n {myOtherZawg.bark()}")



