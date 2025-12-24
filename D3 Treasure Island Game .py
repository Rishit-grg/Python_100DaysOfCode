print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")

c1 = input("You come across a crossroad\nDo you want to go left(l) or right(r)? ").lower()
if c1=="r":
    print("GAME OVER : You fell off a cliff (T-T)\n Poor luck")
elif c1=="l":
    c2 = input("You are on a riverbank. Do u want to wait for a boat (w) or swim across(s)?").lower()
    if c2 == "w":
        c3 = input("you found a castle across the river with 3 coloured doors, choose one - Red(r), Blue(b) or Green (g)").lower()
        if c3 =="r":
            print("GAME OVER : Have a good swim in red redlava\nShould've know Red means danger")
        elif c3 =="b":
            print("CONGRATULATIONS You Win !! You Found the treasure")
            print(r'''
                888                                                          
                888                                                          
                888                                                          
                88888 8888d888 .d88b.   8888b.  .d8888b  888  888 888d888 .d88b.  
                888    888P"  d8P  Y8b     "88b 88K      888  888 888P"  d8P  Y8b 
                888    888    88888888. d888888 "Y8888b. 888  888 888    88888888 
                Y88b.  888    Y8b.     888  888      X88 Y88b 888 888    Y8b.     
                "Y888 888     "Y8888  "Y888888  88888P'  "Y88888  888     "Y8888  
                ''')
        elif c3 =="g":
            print("GAME OVER : Green was the colour of the monster behind the door whose dinnerplate u are on")
        else :
            print ("Invalid input")
    elif c2 == "s":
        print("GAME OVER : You are now tasty crocodile dinner")
    else:
        print("Invalid input")
else :
    print("Invalid input")