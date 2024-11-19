# defining the Pet class
class Pet:
    # initialize the pet's attributes
    def __init__(self, kind, breed, name):
        self.kind = kind  # Type of pet (e.g., dog, cat)
        self.breed = breed  # Breed of the pet (e.g., Bulldog, Siamese)
        self.name = name  # Name of the pet

    # methods
    def get_kind(self):
        return self.kind

    def get_breed(self):
        return self.breed

    def get_name(self):
        return self.name

    # methods
    def set_kind(self, kind):
        self.kind = kind

    def set_breed(self, breed):
        self.breed = breed

    def set_name(self, name):
        self.name = name

    # method to print pet details
    def print_details(self):
        print(f"Pet Name: {self.name}")
        print(f"Kind: {self.kind}")
        print(f"Breed: {self.breed}")
        print("------")

# three Pet objects with different attributes
pet1 = Pet(kind="Dog", breed="Golden Retriever", name="Buddy")
pet2 = Pet(kind="Cat", breed="Siamese", name="Whiskers")
pet3 = Pet(kind="Parrot", breed="Macaw", name="Polly")

# calling the print_details method for each pet object
pet1.print_details()
pet2.print_details()
pet3.print_details()

#  __name__ special method
# display the name of the class
print(f"The name of the class is: {Pet.__name__}")
