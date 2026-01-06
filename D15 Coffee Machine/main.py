import info

def report():
    return f"""Water - {info.resources["water"]}
    Milk - {info.resources["milk"]}
    Coffee - {info.resources["coffee"]}
    Money - {info.money}
    """
def check_resources(coffee):
    not_enough = []

    if info.resources["water"] >= info.MENU[coffee]["ingredients"]["water"]:
        water = True
    else:
        not_enough.append("water")
        water = False

    if info.resources["milk"] >= info.MENU[coffee]["ingredients"]["milk"]:
        milk = True
    else:
        not_enough.append("milk")
        milk = False

    if info.resources["coffee"] >= info.MENU[coffee]["ingredients"]["coffee"]:
        coffee_en = True
    else:
        not_enough.append("coffee powder")
        coffee_en = False

    if water and milk and coffee_en:
        not_enough.append(True)

    return not_enough    ##
def balance(q, d, n, p, coffee):
    received = (q * 0.25) + (d * 0.10) + (n * 0.05) + (p * 0.01)
    needed = info.MENU[coffee]["cost"]

    return received - needed


while True:
    # Init user input and validation
    u_input = (input("What would you like? (espresso / latte / cappuccino):").lower().strip())
    while u_input not in ["espresso", "latte", "cappuccino", "report", "off"]:
        print("Invalid. Input again")
        u_input = (input("What would you like? (espresso / latte / cappuccino):").lower().strip())

    if u_input == "report":
        print(report())
        continue
    elif u_input == "off":
        print("Turning Off...")
        break


    #check resources
    reso_report = check_resources(u_input)
    if True in reso_report:
        print("Proceeding to Payment ......... ")
    else:
        print(f"We are sorry that we are short of {' & '.join(reso_report)}")
        continue


    # Payment
    while True:
        print(f"Your Bill is {info.MENU[u_input]["cost"]}$ \nCheckout........ ")

        while True:
            quarters = int(input("How Many Quarters are your paying - "))
            dimes = int(input("How Many Dimes  are your paying - "))
            nickels = int(input("How Many Nickels are your paying - "))
            pennies = int(input("How Many Pennies are your paying - "))

            if (quarters >=0 and dimes >=0) and (nickels >=0 and pennies >=0) :
                break

        bal = balance(quarters, dimes, nickels, pennies, u_input)

        if bal > 0:
            print(f"Payment Validated, Dispensing change of {bal}$")
            payment_val = True
            break
        elif bal == 0:
            print(f"Payment Validated ")
            payment_val = True
            break
        elif bal < 0:
            print(f"Insufficient money - Payment failed\nRefunding {abs(bal)}$")

        while True:
            cp = (input("Do You want to retry payment (R) or Cancel(C)?").strip().upper())
            if cp in ["R","C"]:
                break
            else:
                continue

        if cp == "R":
            payment_val = None
            continue
        elif cp == "C":
            payment_val = False
            break


    #making Coffee
    if payment_val:
        print(f"Dispensing Your {u_input}.......")
        #updating resources
        info.money += info.MENU[u_input]["cost"]
        for i in ["water", "milk", "coffee"]:
            info.resources[i] -= (info.MENU[u_input]["ingredients"][i])
    else:
        print(f"Order cancelled.")
    print("Thank You, Have a nice day !\n\n\n")