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
            "water": 300,
            "milk": 200,
            "coffee": 100,
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

def getInput(prompt):
    while True:
        Finput = input(prompt)
        if Finput == "off":
            sys.exit()
        if Finput == "report":
            print(f"Water: {resources['water']}ml")
            print(f"Milk: {resources['milk']}ml")
            print(f"Coffee: {resources['coffee']}g")
            print(f"Money: {resources['money']}$")
            continue
        else:  
            return Finput

def checkResources(coffee):
    efficient = True
    for ingredient in MENU[coffee]['ingredients'].keys():
        if resources[ingredient] < MENU[coffee]['ingredients'][ingredient]: # Compares resources with the required ingredients
            efficient = False
            print(f"Sorry, There is not enough {ingredient}.")
            return efficient
    return efficient

def processOrder(coffee):
    efficient = checkResources(coffee)
    if not efficient:
        return
    userMoney = 0
    print("Please insert the coins")
    quarters = float(getInput("How many quarters? ")) * 0.25
    dimes = float(getInput("How many dimes? ")) * 0.10
    nickles = float(getInput("How many nickles? ")) * 0.05 
    pennies = float(getInput("How many pennies? ")) * 0.01
    userMoney = quarters + dimes + nickles + pennies
    if userMoney < MENU[coffee]["cost"]:
        print("Sorry that's not enough money. Money refunded")
    else:
        print(f"Here is ${round(userMoney - MENU[coffee]["cost"], 2)} dollars in change.")
        # Deduct resources values
        for ingredient in MENU[coffee]['ingredients'].keys():
            resources[ingredient] -= MENU[coffee]['ingredients'][ingredient]
        resources['money'] += MENU[coffee]["cost"] # add profit to machine report

        print(f"Here is your {coffee}. Enjoy!")
    


# ----- Main Loop -----
while True:
    coffee = getInput("​What would you like? (espresso/latte/cappuccino): ")
    efficient = True
    if coffee == "espresso":
        processOrder("espresso")
    if coffee == "latte":
        processOrder("latte")
    if coffee == "cappuccino":
        processOrder("cappuccino")
