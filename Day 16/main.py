from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

menu = Menu()
coffeemaker = CoffeeMaker()
Money = MoneyMachine()


while True:

    what_coffee = input(f"What would you like? ({menu.get_items()}): ").lower()
    if what_coffee == "report":
        Money.report()
        coffeemaker.report()
        continue
        
    if what_coffee == "latte":
        what_coffee = menu.menu[0]
        if coffeemaker.is_resource_sufficient(what_coffee):
            if Money.make_payment(cost=2.5):
                coffeemaker.make_coffee(what_coffee)
                
    if what_coffee == "espresso":
        espresso = menu.menu[1]
        if coffeemaker.is_resource_sufficient(espresso):
            if Money.make_payment(cost=1.5):
                coffeemaker.make_coffee(espresso)

    if what_coffee == "cappuccino":
        cappuccino = menu.menu[2]
        if coffeemaker.is_resource_sufficient(cappuccino):
            if Money.make_payment(cost=1.5):
                coffeemaker.make_coffee(cappuccino)
    
    if what_coffee == "off":
        break
                
    another = str(input("Do you want another drink? Y or N: ")).lower()
    if another == "n":
        break
        
