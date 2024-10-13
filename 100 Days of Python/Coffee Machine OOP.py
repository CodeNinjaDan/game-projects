from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

menu = Menu() #Setting the Class tto the Object --> An Object is declared
coffee_maker = CoffeeMaker()
money_machine = MoneyMachine()

is_on = True

while is_on:
    options = menu.get_items() #get_items()
    # Returns all the names of the available menu items as a concatenated string. Set it to a variable and add an
    # f string to print the values
    choice = input(f"What would you like? ({options}): ")
    if choice == "off":
        is_on = False
    elif choice == "report":
        #Print out the report of the available resources
        coffee_maker.report()
        money_machine.report()
    else:
        # find_drink(order_name) --> Takes in the name of the choice of the drink by the user
        # and searches the Menu for it, if it exists it returns it and if it doesn't then return None
        drink = menu.find_drink(choice)
        # is_resource_sufficient(drink) --> Checks the selected drink's ingredients against the available resources
        # to check if the drink can be made
        if coffee_maker.is_resource_sufficient(drink) and money_machine.make_payment(drink.cost):
            coffee_maker.make_coffee(drink)
        #If the amount of money inserted is enough then the drink will be made.
        #Return False if the amount of money isn't enough