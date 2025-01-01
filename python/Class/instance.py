class Dog:
    species = "Canis familiaris" 

    def __init__(self, name, breed):
        self.name = name   # instance variable
        self.breed = breed

# creating instances
dog1 = Dog("Rex", "Labrador")
dog2 = Dog("Bella", "Bulldog")

# All instaance reflect the change
print(dog1.species)  # Output: "Canis lupus familiaris"
print(dog2.species)  # Output: "Canis lupus familiaris"
