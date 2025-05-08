MENU = {
    "expresso": {
        "ingredients": {
            "water": 50,
            "cofee": 10,
        },
        "cost": 1.5,
    },
    
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "cofee": 24,
        },
        "cost": 2.5,
    },
    
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "cofee": 100,
        },
        "cost": 3.0,
    },
}
profit = 0
resources = {
    "water": 300,
    "milk": 200,
    "cofee": 100,
}

def is_resource_sufficiemt(order_ingredients):
    is_enough = True
    
    for item in order_ingredients:
        if order_ingredients[item] >= resources[item]:
            print(f"Sorry ther is not enough {item}.")
            is_enough = False
            
    return is_enough 

def process_coin():
    print("Please insert coins.")
    total = int(input("how many quarters?: ")) * 0.25
    total += int(input("how many dimes?: ")) * 0.1
    total += int(input("how many nickels?: ")) * 0.05
    total += int(input("how many pennies?: ")) * 0.01
    
    return total

def is_transaction_successful(money_recieved, drink_cost):
    if money_recieved >= drink_cost:
        change = round(money_recieved - drink_cost, 2)
        print(f"Here is ${change} in change.")
        global profit
        profit += drink_cost
        return True
    else:
        print("Sorry, that's not enough money, Money refunded")
        return False
    
def make_cofee(drink_name, order_ingredients):
    for item in order_ingredients:
        resources[item] -= order_ingredients[item]
    print(f"Here is your {drink_name}🍵")

is_on = True

while is_on:
    choice = input("What would you like? (expresso/latte/cappiccino): ").lower()
    if choice == "off":
        is_on = False
    elif choice == "report":
        for key, value in resources.items():
            print(f"{key}: {value}")
        print(f"Money: ${profit}")
    else:
        drink = MENU[choice]
        if is_resource_sufficiemt(drink["ingredients"]):
            payment = process_coin()
            if is_transaction_successful(payment, drink["cost"]):
                make_cofee(choice, drink["ingredients"])
