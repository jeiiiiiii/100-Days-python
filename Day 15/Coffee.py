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

money = {
    "value": 0,
}

def report():
    print(f"Water: {resources['water']}ml")
    print(f"Milk: {resources['milk']}ml")
    print(f"Coffee: {resources['coffee']}g")
    print(f"Money: ${money['value']}")
    
def coins():
    print("Please insert coins.")
    quarters = int(input("How many quarters?: ")) * .01
    dimes = int(input("How many dimes?: ")) * .10
    nickles = int(input("How many nickles?: ")) *.05
    penny = int(input("How many pennies?: ")) *.25
    
    total_money = penny + dimes + nickles + quarters
    
    return total_money

    
def ask_what_coffee():
    
    while True:
        what_coffee = str(input("What would you like? (espresso/latte/cappuccino): ")).lower()

        if what_coffee == "report":
            report()
            continue
        
        if what_coffee == "off":
            break
        
        how_much = float(coins())
        
        # espresso
        if what_coffee == "espresso":
            cost = 1.5
            if resources["water"] < 50:
                print("Sorry, there is not enough water.")
                break
            if resources["coffee"] < 18:
                print("Sorry, there is not enough coffee.")
                break
            if how_much < cost:
                print("Not enough money")
            elif how_much >= cost:
                resources["water"] -= 50
                resources["coffee"] -= 18
                money["value"] += cost
                print("Here is your espresso! Enjoy!!!")
                if how_much > cost:
                    change = how_much - cost
                    print(f"Here is ${change:.2f} in change")
                
        # latte
        if what_coffee == "latte":
            cost = 2.5
            if resources["water"] < 250:
                print("Sorry, there is not enough water.")
                break
            if resources["milk"] < 150:
                print("Sorry, there is not enough milk.")
                break
            if resources["coffee"] < 24:
                print("Sorry, there is not enough coffee.")
                break
            if how_much < cost:
                print("Not enough money")
            elif how_much >= cost:
                resources["water"] -= 250
                resources["milk"] -= 150
                resources["coffee"] -= 24
                money["value"] += cost
                print("Here is your latte! Enjoy!!!")
                if how_much > cost:
                    change = how_much - cost
                    print(f"Here is ${change:.2f} in change")
                
        # cappuccino
        if what_coffee == "cappuccino":
            cost = 3.0
            if resources["water"] < 250:
                print("Sorry, there is not enough water.")
                break
            if resources["milk"] < 100:
                print("Sorry, there is not enough milk.")
                break
            if resources["coffee"] < 24:
                print("Sorry, there is not enough coffee.")
                break
            if how_much < cost:
                print("Not enough money")
            elif how_much >= cost:
                resources["water"] -= 250
                resources["milk"] -= 100
                resources["coffee"] -= 24
                money["value"] += cost
                print("Here is your cappuccino! Enjoy!!!")
                if how_much > cost:
                    change = how_much - cost
                    print(f"Here is ${change:.2f} in change")
                
        another = str(input("Do you want another drink? Y or N: ")).lower()
        if another == "n":
            break

ask_what_coffee()

