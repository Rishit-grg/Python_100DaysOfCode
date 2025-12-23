principle = int(input("What is the bill amount ?"))
tip_percentage = int(input("what percentage do you want to tip your server ?"))
tip = (tip_percentage / 100) * principle
total = round(tip + principle, 2)
print(f"Your total payable amount is - {total} Rs.")
people = int(input("How many people do you want to split the bill between? "))
print(f"each person must pay {round(total/people,2)} Rs.")
