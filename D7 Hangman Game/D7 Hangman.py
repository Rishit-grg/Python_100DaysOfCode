import random
import Hangman_Art
import Hangman_wordlist

stages = Hangman_Art.stages
word_list = Hangman_wordlist.word_list
start_art = Hangman_Art.art

print(start_art[0])
word = random.choice(word_list)
life = 6

placeholder = []
for i in range(0, len(word)):
    placeholder.append("_")
print("".join(placeholder))

guessed = []

# Game loop
while life != 0 and "_" in placeholder:

    guess = input("Pick an Alphabet- ").lower()

    # input filtering and fixing
    if guess == "" or not guess.isalpha():
        print("Enter a valid alphabet.")
        continue
    guess = guess[0]

    if guess in guessed:  # check for repeated guess
        print(f"Already guessed {guess}. Try something new.")
        print(" ".join(placeholder))
        print(f"{life} lives left ")
        continue

    guessed.append(guess)

    if guess in word:
        print(f"{guess} is correct guess")
        # replace alpha in placeholder
        for i in range(0, len(word)):
            if word[i] == guess:
                placeholder[i] = guess
    else:
        print(f"{guess} is wrong guess")
        life -= 1

    print(" ".join(placeholder))
    print(f"{life} lives left ")
    print(stages[life])

if life == 0:
    print("LOST : Your hangman died ")
    print(f"The word was: {word}")
if "_" not in placeholder:
    print("VICTORY : Your hangman survives ")


# TODO - make difficulty levels to choose from (put harder words list of upper levels and decide amount of lives accordingly )
#        use more functions where possible
#        use some kind of random words finder instead of hardcoding word_list (maybe even add word_list categories )
