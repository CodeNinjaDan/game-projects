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

# espresso_water = MENU["espresso"]["ingredients"]["water"]
# espresso_coffee = MENU["espresso"]["ingredients"]["coffee"]
# espresso_cost = MENU["espresso"]["cost"]
#
# latte_water = MENU["latte"]["ingredients"]["water"]
# latte_milk = MENU["latte"]["ingredients"]["milk"]
# latte_coffee = MENU["latte"]["ingredients"]["coffee"]
# latte_cost = MENU["latte"]["cost"]
#
# cappuccino_water = MENU["cappuccino"]["ingredients"]["water"]
# cappuccino_milk = MENU["cappuccino"]["ingredients"]["milk"]
# cappuccino_coffee = MENU["cappuccino"]["ingredients"]["coffee"]
# cappuccino_cost = MENU["cappuccino"]["cost"]
#
# #SCOPE
#
# def user_input():
#     money = 0
#     change = 0
#
#     start_coffee_machine = True
#     while start_coffee_machine:
#         choice = input("What would you like? (espresso/latte/cappuccino ar a report):").lower()
#         print("Please insert your coins.")
#         quarter = float(input("How many quarters?: ")) * 0.25
#         dime = float(input("How many dimes?: ")) * 0.10
#         nickel = float(input("How many nickels?: ")) * 0.05
#         penny = float(input("How man pennies?: ")) * 0.01
#
#         money += quarter + dime + nickel + penny
#         print(f"$",money)
#         if choice == "espresso":
#             if money >= espresso_cost:
#                 if money > espresso_cost:
#                     change += money - espresso_cost
#                     print(f"Your change is {change}")
#
#                 if resources["water"] >= espresso_water and resources["coffee"] >= espresso_coffee:
#                     resources["water"] -= espresso_water
#                     resources["coffee"] -= espresso_coffee
#                     print(f"Here is your {choice} ☕ enjoy.")
#
#                 else:
#                     print(f"There is not enough {'water' if resources['water'] < espresso_water else 'coffee'}")
#                     start_coffee_machine = False
#
#             else:
#                 print(f"Money is not enough. ${money} refunded")
#
#         elif choice == "latte":
#             if money >= latte_cost:
#                 if money > latte_cost:
#                     change += money - latte_cost
#                     print(f"Your change is {change}")
#
#                 if resources["water"] >= latte_water and resources["coffee"] >= latte_coffee and\
#                         resources["milk"] >= latte_milk:
#                     resources["water"] -= latte_water
#                     resources["coffee"] -= latte_coffee
#                     resources["milk"] -= latte_milk
#                     print(f"Here is your {choice} ☕ enjoy.")
#
#                 else:
#                     print(f"There is not enough {'water' if resources['water'] < latte_water\
#                         else 'coffee' if resources["coffee"] < latte_coffee else 'milk'}, sorry.")
#                     start_coffee_machine = False
#             else:
#                 print(f"Money is not enough. ${money} refunded")
#
#         elif choice == "cappuccino":
#             if money >= cappuccino_cost:
#                 if money > latte_cost:
#                     change += money - cappuccino_cost
#                     print(f"Your change is {change}")
#
#                 if resources["water"] >= cappuccino_water and resources["coffee"] >= cappuccino_coffee and\
#                         resources["milk"] >= cappuccino_milk:
#                     resources["water"] -= cappuccino_water
#                     resources["coffee"] -= cappuccino_coffee
#                     resources["milk"] -= cappuccino_milk
#                     print(f"Here is your {choice} ☕ enjoy.")
#
#                 else:
#                     print(f"There is not enough {'water' if resources['water'] < cappuccino_water \
#                         else 'coffee' if resources["coffee"] < cappuccino_coffee else 'milk'}, sorry.")
#                     start_coffee_machine = False
#             else:
#                 print(f"Money is not enough. ${money} refunded")
#
#         elif choice == "off":
#             print("Power off. Goodbye.")
#             start_coffee_machine = False
#
#         elif choice == "report":
#             print(f"Water: {resources["water"]}ml\nMilk:{resources["milk"]}ml\nCoffee:\
# {resources["coffee"]}gm\nMoney: ${money}.")
#
#         else:
#             print(f"{choice} is not sold here, sorry.")
#             start_coffee_machine = False
# user_input()

#****************************************************  OR *************************************************************
def is_resource_sufficient(order_ingredients):
    """Returns True when order can be made, False if ingredients are insufficient."""
    for item in order_ingredients:
        if order_ingredients[item] > resources[item]:
            print(f"Sorry there is not enough {item}.")
            return False
    return True


def process_coins():
    """Returns the total calculated from coins inserted."""
    print("Please insert coins.")
    total = int(input("how many quarters?: ")) * 0.25
    total += int(input("how many dimes?: ")) * 0.1
    total += int(input("how many nickles?: ")) * 0.05
    total += int(input("how many pennies?: ")) * 0.01
    return total


def is_transaction_successful(money_received, drink_cost):
    """Return True when the payment is accepted, or False if money is insufficient."""
    if money_received >= drink_cost:
        change = round(money_received - drink_cost, 2)
        print(f"Here is ${change} in change.")
        global profit
        profit += drink_cost
        return True
    else:
        print("Sorry that's not enough money. Money refunded.")
        return False


def make_coffee(drink_name, order_ingredients):
    """Deduct the required ingredients from the resources."""
    for item in order_ingredients:
        resources[item] -= order_ingredients[item]
    print(f"Here is your {drink_name} ☕️. Enjoy!")


is_on = True

while is_on:
    choice = input("What would you like? (espresso/latte/cappuccino): ")
    if choice == "off":
        is_on = False
    elif choice == "report":
        print(f"Water: {resources['water']}ml")
        print(f"Milk: {resources['milk']}ml")
        print(f"Coffee: {resources['coffee']}g")
        print(f"Money: ${profit}")
    else:
        drink = MENU[choice]
        if is_resource_sufficient(drink["ingredients"]):
            payment = process_coins()
            if is_transaction_successful(payment, drink["cost"]):
                make_coffee(choice, drink["ingredients"])