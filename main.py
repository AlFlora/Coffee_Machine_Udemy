from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine


menu = Menu()
coffee_maker = CoffeeMaker()
money_machine = MoneyMachine()


machine_is_on = True


while machine_is_on:
    choice = input(f"What would you like? {menu.get_items()}")
    if choice == "off":
        machine_is_on = False
    elif choice == "report":
        coffee_maker.report()
        money_machine.report()
    else:
        item = menu.find_drink(choice)
        if item is not None:
            if coffee_maker.is_resource_sufficient(item):
                if money_machine.make_payment(item.cost):
                    coffee_maker.make_coffee(item)


