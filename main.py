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
    "coffee": 100,
    "money": 0
}
def getInput(prompt):
    command = True
    while command:
        Finput = input(prompt)
        if Finput == "off":
            sys.exit()
        if Finput == "report":
            print(f"Water: {resources['water']}ml")
            print(f"Milk: {resources['milk']}ml")
            print(f"Coffee: {resources['coffee']}g")
            print(f"Money: {resources['money']}$")
        else:
            command = False
    return Finput


def checkResources(coffee):
    efficient = True
    for ingredient in MENU[coffee]['ingredients'].keys():
        if resources[ingredient] < MENU[coffee]['ingredients'][ingredient]: # Compares resources with the required ingredients
            efficient = False
            return efficient, ingredient
    return efficient, ingredient

def processOrder(resources,coffee):
    efficient, ingredient = checkResources('espresso')

    if not efficient:
        print(f"Sorry, There is not enough {ingredient}")
        return

    print("Please insert the coins")
    quarters = float(getInput("How many quarters? ")) * 0.25
    dimes = float(getInput("How many dimes? ")) * 0.10
    nickles = float(getInput("How many nickles? ")) * 0.05 
    pennies = float(getInput("How many pennies? ")) * 0.01
    resources["money"] = quarters + dimes + nickles + pennies
    if resources["money"] < MENU[coffee]["cost"]:
        print("Sorry that's not enough money. Money refunded")
    
    # Deduct resources values
    for ingredient in MENU[coffee]['ingredients'].keys():
        resources[ingredient] -= MENU[coffee]['ingredients'][ingredient]


# ----- Main Loop -----
while True:
    coffee = getInput("​What would you like? (espresso/latte/cappuccino): ")
    efficient = True
    if coffee == "espresso":
        processOrder(resources,"espresso")
