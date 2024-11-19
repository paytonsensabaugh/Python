# defining the Pet class
class Pet:
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

# create three Pet objects 
pet1 = Pet()
pet1.set_kind("Dog")
pet1.set_breed("Golden Retriever")
pet1.set_name("Buddy")

pet2 = Pet()
pet2.set_kind("Cat")
pet2.set_breed("Siamese")
pet2.set_name("Whiskers")

pet3 = Pet()
pet3.set_kind("Parrot")
pet3.set_breed("Macaw")
pet3.set_name("Polly")

# calling the print_details method for each pet object
pet1.print_details()
pet2.print_details()
pet3.print_details()

# demonstrating the __name__ special method
# display the name of the class
print(f"The name of the class is: {Pet.__name__}")
