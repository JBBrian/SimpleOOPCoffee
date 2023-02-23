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

power = "on"
machine_money = 0.00


def check_resources():
    global order
    global user_money
    if resources["water"] < MENU[order]["ingredients"]["water"]:
        print("Sorry there's not sufficient water")
    elif resources["milk"] < MENU[order]["ingredients"]["milk"]:
        print("Sorry insufficient milk")
    elif resources["coffee"] < MENU[order]["ingredients"]["coffee"]:
        print("Sorry insufficient coffee")
    else:
        quarters = float(input("How many quarters? "))
        dimes = float(input("How many dimes? "))
        nickles = float(input("How many nickles? "))
        pennies = float(input("How many pennies? "))
        user_money = (0.25 * quarters) + (0.10 * dimes) + (0.05 * nickles) + (0.01 * pennies)


def process_order():
    global order
    global user_money
    change = user_money - MENU[order]["cost"]
    if user_money > MENU[order]["cost"]:
        print(f"Here is ${change} in change.")
        print(f"Here is your {order} ☕️.Enjoy!")
    elif user_money < MENU[order]["cost"]:
        print("Sorry that's not enough money. Money refunded.")


while power == "on":
    order = input("What would you like? (espresso/latte/cappuccino): ")
    if order == "off":
        power = "off"
    elif order == "report":
        print("Resources available:")
        print(f"Water: {resources['water']}ml")
        print(f"Milk: {resources['milk']}ml")
        print(f"Coffee: {resources['coffee']}ml")
        print(f"Money: ${machine_money}")
    elif order == "espresso":
        check_resources()
        user_money -= 1.50
        machine_money += 1.50
        resources["water"] -= 50
        resources["milk"] -= 0
        resources["coffee"] -= 18
        process_order()
    elif order == "latte":
        check_resources()
        user_money -= 2.50
        machine_money += 2.50
        resources["water"] -= 200
        resources["milk"] -= 150
        resources["coffee"] -= 24
        process_order()
    elif order == "cappuccino":
        check_resources()
        user_money -= 3.00
        machine_money += 3.00
        resources["water"] -= 250
        resources["milk"] -= 100
        resources["coffee"] -= 24
        process_order()


