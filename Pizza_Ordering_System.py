import csv
from datetime import datetime

menu = open("menu.txt", "w", encoding="utf-8")
menu.write("please choose a pizza:\n1: Classic\n2: Margarita\n3: Plain\n4: Pepperoni\n")
menu.write("=================================\n")
menu.write("please choose a pizza sauce:\n1: Mushroom\n2: Onion\n3: Meat\n4: Corn\n5: Sausage")
menu.close()

database = open("Orders_Database.csv", "a", encoding="utf-8")
database.close()


class Pizza:
    def __init__(self, description, cost):
        self.description = description
        self.cost = cost

    def get_description(self):
        return self.description

    def get_cost(self):
        return self.cost


class Classic(Pizza):
    def __init__(self):
        super().__init__("Classic", 60)


class Margarita(Pizza):
    def __init__(self):
        super().__init__("Margarita", 55)


class Plain(Pizza):
    def __init__(self):
        super().__init__("Plain", 50)


class Pepperoni(Pizza):
    def __init__(self):
        super().__init__("Pepperoni", 55)


class Decorator(Pizza):
    def __init__(self, component):
        self.component = component

    def get_cost(self):
        return self.component.get_cost() + self.cost

    def get_description(self):
        return self.component.get_description() + ' ' + self.description


class Mushroom(Decorator):
    def __init__(self, component):
        super().__init__(component)
        self.description = "Mushroom"
        self.cost = 7


class Onion(Decorator):
    def __init__(self, component):
        super().__init__(component)
        self.description = "Onion"
        self.cost = 5


class Meat(Decorator):
    def __init__(self, component):
        super().__init__(component)
        self.description = "Meat"
        self.cost = 10


class Corn(Decorator):
    def __init__(self, component):
        super().__init__(component)
        self.description = "Corn"
        self.cost = 4


class Sausage(Decorator):
    def __init__(self, component):
        super().__init__(component)
        self.description = "Sausage"
        self.cost = 8


if __name__ == "__main__":

    with open("Menu.txt", "r") as menu:
        print(menu.read())

    while True:
        p = input("Enter a pizza number: ")
        if p == "1":
            pizza = Classic()
            break
        elif p == "2":
            pizza = Margarita()
            break
        elif p == "3":
            pizza = Plain()
            break
        elif p == "4":
            pizza = Pepperoni()
            break
        else:
            print("Incorrect character, please try again")
            with open("Menu.txt", "r") as menu:
                print(menu.read())

    while True:
        s = input("Enter a sauce number: ")
        if s == "1":
            sauce = Mushroom(pizza)
            break
        elif s == "2":
            sauce = Onion(pizza)
            break
        elif s == "3":
            sauce = Meat(pizza)
            break
        elif s == "4":
            sauce = Corn(pizza)
            break
        elif s == "5":
            sauce = Sausage(pizza)
            break
        else:
            print("Incorrect character, please try again")
            with open("Menu.txt", "r") as menu:
                print(menu.read())

    invoice = sauce.get_cost()
    print("Invoice: ", invoice, "TL")

    name = input("Name: ")
    surname = input("Surname: ")
    tc = input("TC identification number: ")
    card_no = input("Credit card number: ")
    card_password = input("Card password: ")
    print("Your order has been received.")

    with open("Orders_Database.csv", "a", newline='') as database:
        writer = csv.writer(database)
        writer.writerow([name, surname, tc, card_no, card_password, sauce.get_description(), invoice, datetime.now().strftime("%d/%m/%Y %H:%M:%S")])
