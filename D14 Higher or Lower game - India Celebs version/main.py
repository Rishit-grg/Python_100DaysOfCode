from game_data import data
from random import randint

def give_data_of(num):
    return f"{data[num]['name']} - {data[num]['description']} born in {data[num]['birthplace']}"



def give_name_of(num):
    return data[num]['name']


chosen = set()
points = 0
reps = 0

A_index = randint(0, len(data) - 1)
chosen.add(A_index)

B_index = randint(0, len(data) - 1)
while B_index in chosen:
    B_index = randint(0, len(data) - 1)
chosen.add(B_index)


while True :
    A_followers = data[A_index]["follower_count"]
    B_followers = data[B_index]["follower_count"]

    print(f"\nCompare A : {give_data_of(A_index)}")
    print("  V/s")
    print(f"Against B : {give_data_of(B_index)}\n")

    if A_followers > B_followers:
        answer = "A"
    else:
        answer = "B"

    u_input = (input("Who has More followers - A or B ?")).upper().strip()
    while not (u_input == "A" or u_input =="B"):
        u_input = (input("Enter a valid value - A or B ?")).upper().strip()

    if u_input == answer:
        print("YOU ARE RIGHT !!")
        print(f"{give_name_of(A_index)} has {A_followers} million followers.\n{give_name_of(B_index)} has {B_followers} million followers.")

        points+=1

        if len(chosen) >= 91:
            print(f"You Completed the entire Game correctly !!!\nYou are an absolute GENIUS. \nYour score is {points}")
            break

        if answer=="B":
            reps +=1

            A_index = B_index
            B_index = randint(1, len(data) - 1)
            while B_index in chosen:
                B_index = randint(1, len(data) - 1)
            chosen.add(B_index)



        else:
            reps += 1
            if reps > 6:
                print("\nLETS MIX THINGS UP ..... TO KEEP IT INTERESTING")
                A_index = randint(0, len(data) - 1)
                while A_index in chosen:
                    A_index = randint(0, len(data) - 1)
                chosen.add(A_index)
                reps = 0

            B_index = randint(1, len(data) - 1)
            while B_index in chosen:
                B_index = randint(1, len(data) - 1)
            chosen.add(B_index)

    else:
        if abs(A_followers-B_followers)<=5:
            print("OOOh... That was a close one")
        print(f"{give_name_of(A_index)} has {A_followers} million followers.\n{give_name_of(B_index)} has {B_followers} million followers.")
        print(f"YOU GOT THIS ONE WRONG ...... \nYour score is {points}")
        break