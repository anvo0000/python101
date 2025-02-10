from menu import Menu
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

def main():
    coffee_maker =  CoffeeMaker()
    money_machine = MoneyMachine()
    menu = Menu()

    while True:
        option = menu.get_items()
        choice = input(f"What would you like? ({option})")
        if choice == "off":
            print("Machine is turning off. Bye!")
            break
        elif choice == "report":
            coffee_maker.report()
            money_machine.report()
        elif menu.find_drink(order_name=choice):
            drink = menu.find_drink(order_name=choice)
            if coffee_maker.is_resource_sufficient(drink=drink):
                if money_machine.make_payment(cost=drink.cost):
                    coffee_maker.make_coffee(order=drink)
        else:
            print("Invalid option, try again")

if __name__ == '__main__':
    main()