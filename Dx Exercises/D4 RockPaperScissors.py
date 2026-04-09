import random

rock = """
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
"""
paper = """
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
"""
scissors = """
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
"""

lose_lines = [
    "Skill issue. Possibly hardware-related.",
    "I didn’t win. You lost. There’s a difference.",
    "Good choice. Regrettable outcome.",
    "Simulation complete. Result unchanged.",
]

win_lines = [
    "Huh. That was… unexpected.",
    "You win this round. I’ll remember that.",
    "Just got lucky, don't get too hyped upp.",
    "Enjoy it. Statistically, it won’t last.",
]

game_images = [0,rock, paper, scissors] 
names = [0, "rock", "paper", "scissors"]

player_choice = int(input("choose 1 for rock, choose 2 for paper, choose 3 for scissors - "))

if player_choice in [1,2,3]:
    print(game_images[player_choice])
    print(f"You chose {names[player_choice]}")
else:
    print("invalid input")
    exit(1)

comp_choice = random.randint(1, 3)

print(f"Computer chose {names[comp_choice]}")
print(game_images[comp_choice])

# logic

diff = (player_choice - comp_choice) % 3  # ............................

if diff == 0:
    print("DRAW")
elif diff == 1:
    print("YOU WIN", random.choice(win_lines))
else:
    print("YOU LOSE", random.choice(lose_lines))
