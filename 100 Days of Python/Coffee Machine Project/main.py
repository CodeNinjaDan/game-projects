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
}

espresso_water = MENU["espresso"]["ingredients"]["water"]
espresso_coffee = MENU["espresso"]["ingredients"]["coffee"]
espresso_cost = MENU["espresso"]["cost"]

latte_water = MENU["latte"]["ingredients"]["water"]
latte_milk = MENU["latte"]["ingredients"]["milk"]
latte_coffee = MENU["latte"]["ingredients"]["coffee"]
latte_cost = MENU["latte"]["cost"]

cappuccino_water = MENU["cappuccino"]["ingredients"]["water"]
cappuccino_milk = MENU["cappuccino"]["ingredients"]["milk"]
cappuccino_coffee = MENU["cappuccino"]["ingredients"]["coffee"]
cappuccino_cost = MENU["cappuccino"]["cost"]

#SCOPE

def user_input():
    money = 0
    espresso_resources = {"water": 50,
            "coffee": 18}

    latte_resources = {"water": 200,
            "milk": 150,
            "coffee": 24}

    cappuccino_resources = {"water": 250,
            "milk": 100,
            "coffee": 24}
    values_espresso_resources = espresso_resources.values()
    values_latte_resources = latte_resources.values()
    values_cappuccino_resources = cappuccino_resources.values()

    start_coffee_machine = True
    while start_coffee_machine:
        choice = input("What would you like? (espresso/latte/cappuccino ar a report):").lower()
        if choice == "espresso":
            if resources["water"] >= espresso_water and resources["coffee"] >= espresso_coffee:
                resources["water"] -= espresso_water
                resources["coffee"] -= espresso_coffee

            else:
                print(f"There is not enough {'water' if resources['water'] < espresso_water else 'coffee'}")
                start_coffee_machine = False

        elif choice == "latte":
            resources["water"] -= latte_water
            resources["coffee"] -= latte_coffee
            resources["milk"] -= latte_milk

        elif choice == "cappuccino":
            resources["water"] -= cappuccino_water
            resources["coffee"] -= cappuccino_coffee
            resources["milk"] -= cappuccino_milk

        elif choice == "off":
            print("Power off. Goodbye.")
            start_coffee_machine = False

        elif choice == "report":
            print(f"Water: {resources["water"]}ml\nMilk:{resources["milk"]}ml\nCoffee:\
{resources["coffee"]}gm\nMoney: ${money}.")

user_input()
