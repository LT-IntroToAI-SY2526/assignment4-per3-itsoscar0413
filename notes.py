# object oriented programming

# (define-struct dog [fur_color name age favorite_food])

# a class is a blueprint, describing what it is, while an object is what makes it unique/individual with specific traits

class Dog:
    """
    a simple dog class to learn object oriented program

    attribute:
        fur_col: color of the fur
        name: the name of the dog
        age: how old a dog is
        favorite_food: the favorite food of the dog
    """
    def __init__(self, fur_color="black", name="no name", age = 1, favorite_food="kibbles"): # self word means "this" (current object)
        """initialize a new Dog with fur_color, name, age and favorite food"""
        self.fur_color = fur_color
        self.name = name
        self.age = age
        self.favorite_food = favorite_food

    def __str__(self):
        """this is going to return a string representation of a Dog"""
        return f"{self.name} is a {self.age} year old {self.fur_color} dog who loves {self.favorite_food}"
    
    def bark(self):
        """make the dog bark"""
        # user-made function
        return f"{self.name} says Woof, Woof!!"
    
    def sleep(self):
        """practicing, to make the dog sleep"""
        return f"{self.name} went to sleep! Sweet dreams :)"
    
    def birthday(self):
        """make the age increase by 1
            celebrate the dog's birthday!!"""
        self.age+=1
        print(f"celebrating {self.name}'s birthday, they are now {self.age} years old!")

    def change_favorite_food(self, new_food): #manipulator? to change the variable value with method
        """changing the dog's favorite food"""
        old_food = self.favorite_food
        self.favorite_food = new_food
        print(f"{self.name} used to love {old_food} and now loves {self.favorite_food}")



my_dog = Dog("black", "logan", 9, "salmon")
enggy_dog = Dog("black and white", "petuchini", 13, "rice")
random_dog = Dog("yellow", "bennyboy", 3, "kibble")
default_dog = Dog()
aaron_dog = Dog("peach and white", "dumbo", favorite_food="anything edible")

print()

print(my_dog)
print(enggy_dog)
print(random_dog)
print(default_dog)
print(aaron_dog)

print()

print(enggy_dog.bark())
print(my_dog.bark())

print()

print(enggy_dog.sleep())
print(random_dog.sleep())
print(default_dog.sleep())

print()

aaron_dog.birthday()
print(aaron_dog)

print()

random_dog.change_favorite_food("steak")
print(random_dog)