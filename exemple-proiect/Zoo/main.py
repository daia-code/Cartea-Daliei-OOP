import json

class Animal:
    def __init__(self, name, species, hunger_level=0):
        self.name = name
        self.species = species
        self.hunger_level = hunger_level

    def feed(self):
        if self.hunger_level > 0:
            self.hunger_level -= 1
            print(f"{self.name} the {self.species} is fed.")
        else:
            print(f"{self.name} the {self.species} is not hungry right now.")

    def get_status(self):
        if self.hunger_level == 0:
            return f"{self.name} the {self.species} is not hungry."
        elif self.hunger_level == 1:
            return f"{self.name} the {self.species} is a bit hungry."
        else:
            return f"{self.name} the {self.species} is very hungry!"

    def to_dict(self):
        return {
            "name": self.name,
            "species": self.species,
            "hunger_level": self.hunger_level
        }

    @classmethod
    def from_dict(cls, data):
        return cls(data["name"], data["species"], data["hunger_level"])

class Zoo:
    def __init__(self, filename):
        self.filename = filename
        self.animals = []
        self.load_animals()

    def load_animals(self):
        try:
            with open(self.filename, 'r') as file:
                animals_data = json.load(file)
                self.animals = [Animal.from_dict(data) for data in animals_data]
        except FileNotFoundError:
            self.animals = []

    def save_animals(self):
        with open(self.filename, 'w') as file:
            animals_data = [animal.to_dict() for animal in self.animals]
            json.dump(animals_data, file, indent=2)

    def add_animal(self, animal):
        self.animals.append(animal)
        self.save_animals()

    def feed_animal(self, name):
        for animal in self.animals:
            if animal.name == name:
                animal.feed()
                self.save_animals()
                return
        print(f"{name} not found in the zoo.")

    def get_animal_status(self, name):
        for animal in self.animals:
            if animal.name == name:
                return animal.get_status()
        return f"{name} not found in the zoo."

    def display_animals(self):
        if not self.animals:
            print("The zoo is empty.")
        else:
            print("\nZoo Animals:")
            for animal in self.animals:
                print(f"{animal.name} the {animal.species} - {animal.get_status()}")

def main():
    zoo = Zoo("zoo.json")

    print("Welcome to the Virtual Zoo!")
    print("You can interact with tigers, lions, and elephants.")

    while True:
        print("\nZoo Menu:")
        print("1. Add Animal")
        print("2. Feed Animal")
        print("3. Check Animal Status")
        print("4. Display All Animals")
        print("5. Exit")

        choice = input("Enter your choice (1-5): ")

        if choice == "1":
            name = input("Enter animal's name: ")
            species = input("Enter animal's species (tiger/lion/elephant): ").lower()
            if species in ["tiger", "lion", "elephant"]:
                animal = Animal(name, species)
                zoo.add_animal(animal)
                print(f"{name} the {species} added to the zoo.")
            else:
                print("Invalid species. Please enter tiger, lion, or elephant.")

        elif choice == "2":
            name = input("Enter animal's name to feed: ")
            zoo.feed_animal(name)

        elif choice == "3":
            name = input("Enter animal's name to check status: ")
            status = zoo.get_animal_status(name)
            print(status)

        elif choice == "4":
            zoo.display_animals()

        elif choice == "5":
            print("Exiting Virtual Zoo. Goodbye!")
            break

        else:
            print("Invalid choice. Please enter a number from 1 to 5.")

if __name__ == "__main__":
    main()
