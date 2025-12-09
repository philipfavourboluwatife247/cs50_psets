"""
Author - Philip Favour Boluwatife
Date - 3rd December, 2025
Pset Name - Felipe’s Taqueria
Pset Details - implement a program that enables a user to place an order, prompting them for items, one per line, until the user inputs control-d (which is a common way of ending one’s input to a program). After each inputted item, display the total cost of all items inputted thus far, prefixed with a dollar sign ($) and formatted to two decimal places. Treat the user’s input case insensitively. Ignore any input that isn’t an item. Assume that every item on the menu will be titlecased.
"""

def main():
    menu = {
    "Baja Taco": 4.25,
    "Burrito": 7.50,
    "Bowl": 8.50,
    "Nachos": 11.00,
    "Quesadilla": 8.50,
    "Super Burrito": 8.50,
    "Super Quesadilla": 9.50,
    "Taco": 3.00,
    "Tortilla Salad": 8.00
    }
    mealorder_calculator(menu)

def mealorder_calculator(menuitems):
    total = 0
    while True:
        try:
            order = input("Item: ").strip().title()
            if order not in menuitems:
                continue
            total += menuitems[order]
            print(f"Total: ${total:.2f}")
        except EOFError:
            print(f"\nTotal: ${total:.2f}")
            return

if __name__ == "__main__":
    main()
