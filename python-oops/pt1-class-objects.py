class Dog:
    #constructor - automatically called when we create an object or instance outside class
    def __init__(self, name, breed, owner):
        # these are the attributes of the class 
        self.name = name 
        self.breed = breed
        self.owner = owner
    
    #method
    def bark(self):
        print("whoof whoof!")

class Owner:
    #constructor
    def __init__(self, name, address, contact_number):
        self.name = name
        self.address = address
        self.phone_number = contact_number

#main
owner1 = Owner("Danny", "34-A silicon", "999-888")
dog1 = Dog("Marshal", "German-Shephard", owner1)
print(dog1.owner.name)
        