import json

class Toy:
    def __init__(self, name, category):
        self.name = name
        self.category = category

    def to_dict(self):
        return {
            "name": self.name,
            "category": self.category
        }

    @classmethod
    def from_dict(cls, data):
        return cls(data["name"], data["category"])

    def display(self):
        print(f"Name: {self.name}")
        print(f"Category: {self.category}")


class ToyBoxManager:
    def __init__(self, filename):
        self.filename = filename
        self.toys = []
        self.load_toys()

    def load_toys(self):
        try:
            with open(self.filename, 'r') as file:
                toys_data = json.load(file)
                self.toys = [Toy.from_dict(data) for data in toys_data]
        except FileNotFoundError:
            self.toys = []

    def save_toys(self):
        with open(self.filename, 'w') as file:
            toys_data = [toy.to_dict() for toy in self.toys]
            json.dump(toys_data, file, indent=2)

    def add_toy(self, name, category):
        toy = Toy(name, category)
        self.toys.append(toy)
        self.save_toys()
        print(f"{name} added to the toy box.")

    def remove_toy(self, name):
        for toy in self.toys:
            if toy.name == name:
                self.toys.remove(toy)
                self.save_toys()
                print(f"{name} removed from the toy box.")
                return
        print(f"{name} not found in the toy box.")

    def display_toys(self):
        if not self.toys:
            print("Toy box is empty.")
        else:
            print("\nToy Box:")
            for toy in self.toys:
                toy.display()
                print()

    def menu(self):
        while True:
            print("\nToy Box Menu:")
            print("1. Add Toy")
            print("2. Remove Toy")
            print("3. Display Toys")
            print("4. Exit")

            choice = input("Enter your choice (1-4): ")

            if choice == "1":
                name = input("Enter toy name: ")
                category = input("Enter toy category: ")
                self.add_toy(name, category)

            elif choice == "2":
                name = input("Enter toy name to remove: ")
                self.remove_toy(name)

            elif choice == "3":
                self.display_toys()

            elif choice == "4":
                print("Exiting Toy Box. Goodbye!")
                break

            else:
                print("Invalid choice. Please enter a number from 1 to 4.")

if __name__ == "__main__":
    toy_box_manager = ToyBoxManager("toy_box.json")
    toy_box_manager.menu()
