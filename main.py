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
    efficient = True
    for ingredient in MENU[coffee]['ingredients'].keys():
        if resources[ingredient] < MENU[coffee]['ingredients'][ingredient]:
            efficient = False
            return efficient, ingredient
    return efficient, ingredient

# ----- Main Loop -----
off = False
efficient = True
while not off:
    coffee = input("​What would you like? (espresso/latte/cappuccino): ")

    if coffee == "espresso":
        efficient, ingredient = checkResources('espresso')

    if not efficient:
        print(f"Sorry, There is not enough {ingredient}")

# ----- All time commands ------
    if coffee == "off":
        sys.exit()
    if coffee == "report":
        print(f"Water: {resources['water']}ml")
        print(f"Milk: {resources['milk']}ml")
        print(f"Coffee: {resources['coffee']}g")
        print(f"Money: {resources['money']}$")
