"""
Author - Philip Favour Boluwatife
Date - 8th December, 2025
Pset Name - Grocery List
Pset Detail - implement a program that prompts the user for items, one per line, until the user inputs control-d (which is a common way of ending one’s input to a program). Then output the user’s grocery list in all uppercase, sorted alphabetically by item, prefixing each line with the number of times the user inputted that item. No need to pluralize the items. Treat the user’s input case-insensitively.
"""

def main():
    print(grocery_list())

def grocery_list():
    groceries = {}
    while True:
        try:
            item = input("").strip().lower()
            if item in groceries:
                groceries[item] += 1
            else:
                groceries[item] = 1
        except EOFError:
            for item, count in sorted(groceries.items()):
                return "\n".join(f"{count} {item.upper()}" for item, count in sorted(groceries.items()))
                
if __name__ == "__main__":
    main()
