from coffee_machine_data import MENU, resources
# TODO: 2. Check resources sufficient to make drink order.


def check_resources(ingredients):
    """Returns a boolean value if certain conditions for the ingredients are met"""
    for item in ingredients:
        if ingredients[item] >= resources[item]:
            print(f"Sorry there is not enough {item}.")
            return False
    return True


profit = 0
is_ordering = True
while is_ordering:
    coffee_request = input("What would you like? (espresso/latte/cappuccino): ")
    if coffee_request == 'report':
        # TODO: 1. Print report of all coffee machine
        print(f"Water: {resources["water"]}ml")
        print(f"Milk: {resources['milk']}ml")
        print(f"Coffee: {resources['coffee']}g")
        print(f"Money: ${profit}")
    elif coffee_request == 'off':
        is_ordering = False
    else:
        drink = MENU[coffee_request]
        if check_resources(drink["ingredients"]):
            # TODO: 3. Print Coins.
            print("Please insert coins.")
            quart = int(input("How many quarters?: ")) * 0.25
            dime = int(input("How many dimes?: ")) * 0.10
            nickle = int(input("How many nickles?: ")) * 0.05
            penny = int(input("How many pennies?: ")) * 0.01
            cost = quart + dime + nickle + penny
            cost = round(cost, 2)
            # TODO: 4. Check transaction successful.
            if cost < drink["cost"]:
                print("Sorry that's not enough money. Money refunded.")
            else:
                # TODO: 5. Make Coffee
                if cost > drink["cost"]:
                    change = round(cost - drink["cost"], 2)
                    print(f"Here is ${change} in change.")
                print(f"Here is your {coffee_request} ☕ Enjoy!")
                profit += drink["cost"]
                for items in drink["ingredients"]:
                    resources[items] -= drink["ingredients"][items]
