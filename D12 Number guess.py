import random
is_won = False
logo = r"""
  / _ \_   _  ___  ___ ___  /__   \ |__   ___    /\ \ \_   _ _ __ ___ | |__   ___ _ __ 
 / /_\/ | | |/ _ \/ __/ __|   / /\/ '_ \ / _ \  /  \/ / | | | '_ ` _ \| '_ \ / _ \ '__|
/ /_\\| |_| |  __/\__ \__ \  / /  | | | |  __/ / /\  /| |_| | | | | | | |_) |  __/ |   
\____/ \__,_|\___||___/___/  \/   |_| |_|\___| \_\ \/  \__,_|_| |_| |_|_.__/ \___|_| 
"""

print(logo)
print("""
RULES:
1. Guess a number between 1 and 100.
2. You get limited guesses based on difficulty.
3. After each guess, you'll be told higher or lower.
4. Guess correctly before guesses run out to win.
""")


# -----------------------------
# Difficulty selection 
# -----------------------------

def get_init_guesses(difficulty):
    if difficulty == "e":
        return 10
    elif difficulty == "m":
        return 7
    elif difficulty == "h":
        return 5
    else:
        return 0

# Keep prompting until a valid difficulty is entered
while True:
    difficulty = input("Choose a difficulty level -\nEasy (E)\nMedium (M)\nHard (H)\n").strip().lower()
    if difficulty in ("e", "m", "h"):
        break
    print("Invalid input. Please enter E, M, or H.")

guesses_left = get_init_guesses(difficulty) 

# -----------------------------
# Functions for result and comparison 
# -----------------------------

def check_guess(guess, num):
    global guesses_left
    
    if guess == num:
        return True
    elif guess > num:
        print("Wrong - Try a lower number ")
        guesses_left -=1
        return False
    else:
        print("Wrong - Guess Higher ")
        guesses_left -=1
        return False
def show_result (is_won):
    if is_won:
        print("Correct Guess - YOU WIN")
    else:
        print("Out of guesses -YOU LOSE")

# -----------------------------
# Main Game 
# -----------------------------

num = random.randint(1, 100)

while guesses_left > 0 and not is_won:
    print(f"You have {guesses_left} guesses")
    while True:
        guess = input("Take a Guess: ").strip()

        if guess.isdigit() and (1<= int(guess) <= 100):
            guess = int(guess)
            break
        else:
            print("Invalid input. Please enter an integer between 1 and 100.")

    is_won = check_guess(guess, num)

show_result(is_won)