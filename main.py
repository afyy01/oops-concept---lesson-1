class Dog:
    def __init__(self, name="", life_expectancy="12 - 16 years", breed_type="West Highland White Terrier", 
                 family="Scottish Terrier", food_it_eats="kibble", color="white"):
        self.name = name
        self.life_expectancy = life_expectancy
        self.breed_type = breed_type
        self.family = family
        self.food_it_eats = food_it_eats
        self.color = color
        print(f"Creating a new dog: {self.name}")

    def display_details(self):
        print("Details of the dog are:")
        print(f"Name: {self.name}")
        print(f"Life Expectancy: {self.life_expectancy}")
        print(f"Breed Type: {self.breed_type}")
        print(f"Family: {self.family}")
        print(f"Food it eats: {self.food_it_eats}")
        print(f"Color: {self.color}")
       

    def change_details(self):
        self.name = input("Please enter the dog's name: ")
        self.life_expectancy = input("Enter the life expectancy: ")
        self.breed_type = input("Enter the breed type: ")
        self.family = input("Enter the family: ")
        self.food_it_eats = input("Enter the food it eats: ")

# Creating dog instances
Logan = Dog("Logan")

# Displaying details
Logan.display_details()
