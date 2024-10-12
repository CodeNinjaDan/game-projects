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
    "water": 700,
    "milk": 300,
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
    change = 0

    start_coffee_machine = True
    while start_coffee_machine:
        choice = input("What would you like? (espresso/latte/cappuccino ar a report):").lower()
        print("Please insert your coins.")
        quarter = float(input("How many quarters?: ")) * 0.25
        dime = float(input("How many dimes?: ")) * 0.10
        nickel = float(input("How many nickels?: ")) * 0.05
        penny = float(input("How man pennies?: ")) * 0.01

        money += quarter + dime + nickel + penny
        print(f"$",money)
        if choice == "espresso":
            if money >= espresso_cost:
                if money > espresso_cost:
                    change += money - espresso_cost
                    print(f"Your change is {change}")

                if resources["water"] >= espresso_water and resources["coffee"] >= espresso_coffee:
                    resources["water"] -= espresso_water
                    resources["coffee"] -= espresso_coffee
                    print(f"Here is your {choice} ☕ enjoy.")

                else:
                    print(f"There is not enough {'water' if resources['water'] < espresso_water else 'coffee'}")
                    start_coffee_machine = False

            else:
                print(f"Money is not enough. ${money} refunded")

        elif choice == "latte":
            if money >= latte_cost:
                if money > latte_cost:
                    change += money - latte_cost
                    print(f"Your change is {change}")

                if resources["water"] >= latte_water and resources["coffee"] >= latte_coffee and\
                        resources["milk"] >= latte_milk:
                    resources["water"] -= latte_water
                    resources["coffee"] -= latte_coffee
                    resources["milk"] -= latte_milk
                    print(f"Here is your {choice} ☕ enjoy.")

                else:
                    print(f"There is not enough {'water' if resources['water'] < latte_water\
                        else 'coffee' if resources["coffee"] < latte_coffee else 'milk'}, sorry.")
                    start_coffee_machine = False
            else:
                print(f"Money is not enough. ${money} refunded")

        elif choice == "cappuccino":
            if money >= cappuccino_cost:
                if money > latte_cost:
                    change += money - cappuccino_cost
                    print(f"Your change is {change}")

                if resources["water"] >= cappuccino_water and resources["coffee"] >= cappuccino_coffee and\
                        resources["milk"] >= cappuccino_milk:
                    resources["water"] -= cappuccino_water
                    resources["coffee"] -= cappuccino_coffee
                    resources["milk"] -= cappuccino_milk
                    print(f"Here is your {choice} ☕ enjoy.")

                else:
                    print(f"There is not enough {'water' if resources['water'] < cappuccino_water \
                        else 'coffee' if resources["coffee"] < cappuccino_coffee else 'milk'}, sorry.")
                    start_coffee_machine = False
            else:
                print(f"Money is not enough. ${money} refunded")

        elif choice == "off":
            print("Power off. Goodbye.")
            start_coffee_machine = False

        elif choice == "report":
            print(f"Water: {resources["water"]}ml\nMilk:{resources["milk"]}ml\nCoffee:\
{resources["coffee"]}gm\nMoney: ${money}.")

        else:
            print(f"{choice} is not sold here, sorry.")
            start_coffee_machine = False
user_input()
