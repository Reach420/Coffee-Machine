import sys

MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 10,
    "money": 0
}

def checkResources(coffee):
    efficient = None
    for ingredient in MENU[coffee]['ingredients'].keys():
        if resources[ingredient] < MENU[coffee]['ingredients'][ingredient]: # Compares resources with the required ingredients
            efficient = False
            return efficient, ingredient
    return efficient, ingredient

# ----- Main Loop -----
off = False
while not off:
    coffee = input("​What would you like? (espresso/latte/cappuccino): ")

    efficient = None
    if coffee == "espresso":
        efficient, ingredient = checkResources('espresso')

    if efficient:
        print("Please insert the coins")
        quarters = input("How many quarters? ")
        dimes = input("How many dimes? ")
        nickles = input("How many nickles? ")
        pennies = input("How many pennies? ")
        # # Deduct resources values
        # for ingredient in MENU[coffee]['ingredients'].keys():
        #     resources[ingredient] -= MENU[coffee]['ingredients'][ingredient]
    elif not efficient:
        print(f"Sorry, There is not enough {ingredient}")

# ----- All time commands ------
    if coffee == "off":
        sys.exit()
    if coffee == "report":
        print(f"Water: {resources['water']}ml")
        print(f"Milk: {resources['milk']}ml")
        print(f"Coffee: {resources['coffee']}g")
        print(f"Money: {resources['money']}$")
