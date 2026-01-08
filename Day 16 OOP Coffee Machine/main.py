
from menu import Menu
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine
# The packages used are provided by the instructor for practise of OOP, not designed by me.

menu_card = Menu()
coffee_maker = CoffeeMaker()
money_machine = MoneyMachine()

while True:
    order = input(f"Choose Your drink {menu_card.get_items()} - ")
    if order == "report":
        print("Printing report....")
        coffee_maker.report()
        money_machine.report()
        continue

    if order == "off":
        print("Turning Off....")
        break

    order_details = menu_card.find_drink(order)
    if coffee_maker.is_resource_sufficient(order_details) and money_machine.make_payment(order_details.cost):
        coffee_maker.make_coffee(order_details)