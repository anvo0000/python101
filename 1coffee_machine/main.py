from math import remainder

from machine_data import MENU, resources

class CoffeeMachine:
    """
    This project based on requirements of Udemy course "100days of Python code"
    Created by: An Vo
    Created date: 2025-01-31
    """
    money: int

    def __init__(self):
        self.system_resources = resources
        self.money = 0

    def generate_report(self):
        current_resources = self.system_resources
        for item, amount in current_resources.items():
            unit = 'ml' if item in ['milk', 'water'] else 'g'
            print(f"{item.title()}: {amount}{unit}")
        print(f"Money: ${self.money}")

    def check_resources(self, drink:str):
        current_resources = self.system_resources
        user_drink_ingredients = MENU[drink]["ingredients"]

        for item  in user_drink_ingredients:
            enough_resource = current_resources[item] >= user_drink_ingredients[item]
            if not enough_resource:
                print(f"Sorry there is not enough {item}.")
                return False
        return True

    def process_coins(self, quarters, dimes, nickel, pennies):
        total = quarters*0.25 + dimes*0.1 + nickel*0.05 + pennies*0.01
        return total

    def check_transaction(self, user_input_coins, drink_cost):
        if user_input_coins < drink_cost:
            print(f"Sorry that's not enough money. Money refunded ${round(user_input_coins,2)}.")
            return False
        elif user_input_coins == drink_cost:
            self.money += drink_cost
            print(f"enough money")
        else:
            self.money += drink_cost
            print(f"Here is ${round(user_input_coins - drink_cost,2)} in change.")
        return True


    def make_coffee(self, drink):
        current_resources = self.system_resources
        user_drink_ingredients = MENU[drink]["ingredients"]

        for item in user_drink_ingredients:
            remainder_resource = current_resources[item] - user_drink_ingredients[item]
            self.system_resources[item] = remainder_resource
        return self.system_resources

    def main(self):
        while True: # keep the machine running
            choose_menu: str = input("What would you like? (espresso/latte/cappuccino): ")

            if choose_menu =="off":
                print("Turning off the coffee machine. Goodbye!")
                break
            elif choose_menu == "report":
                self.generate_report()
            elif choose_menu in MENU.keys():
                if self.check_resources(drink=choose_menu):
                    print(f"A cup of {choose_menu.title()} cost ${MENU[choose_menu]['cost']}\nPlease insert coins.")
                    quarters = int(input("How many quarters? ") or "0")
                    dimes = int(input("how many dimes? ") or "0")
                    nickles = int(input("how many nickles? ") or "0")
                    pennies = int(input("how many pennies? ") or "0")
                    total_user_input_coins = self.process_coins(quarters, dimes, nickles, pennies)
                    checked_transaction = self.check_transaction(user_input_coins=total_user_input_coins,
                                                                 drink_cost=MENU[choose_menu]['cost'])
                    if checked_transaction:
                        rs = self.make_coffee(drink=choose_menu)
                        print(f"Here is your {choose_menu} ☕️. Enjoy!")
            else:
                print("Invalid option. Please choose a valid drink or command.")


if __name__ == '__main__':
    cf = CoffeeMachine()
    cf.main()
