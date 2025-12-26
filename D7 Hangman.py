import random as rndm
stages = [r'''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''', r'''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', r'''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''', r'''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', r'''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''', r'''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', r'''
  +---+
  |   |
      |
      |
      |
      |
=========
''']
word_list = ["apple", "banana", "orange", "grapes", "mango","chair", "table", "window", "mirror", "pillow","river", "mountain", "forest", "desert", "ocean","cloud", "thunder", "rainbow", "sunshine", "breeze","school", "garden", "market", "station", "library","friend", "family", "teacher", "student", "neighbor","happy", "angry", "nervous", "excited", "curious","music", "movie", "picture", "story", "poetry","travel", "journey", "adventure", "holiday", "memory","coffee", "butter", "cheese", "sugar", "biscuit","morning", "evening", "midnight", "weekend","freedom", "silence", "promise", "courage", "wisdom"
]
print(r"""
 _                                             
| |                                            
| |__   __ _ _ __   __ _ _ __ ___   __ _ _ __  
| '_ \ / _` | '_ \ / _` | '_ ` _ \ / _` | '_ \ 
| | | | (_| | | | | (_| | | | | | | (_| | | | |
|_| |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|
                    __/ |                      
                   |___/                        
""")

life = 6
word = rndm.choice(word_list)

placeholder = []
for i in range(0,len(word)):
    placeholder.append("_")
print ("".join(placeholder))

guessed = []

# Game loop 
while life!=0 and "_" in placeholder:
    
    guess = (input("Pick an Alphabet- ")[0]).lower()

    if guess in guessed: # check for repeated guess
        print("repeated guess")
        print (" ".join(placeholder))
        print (f"{life} lives left ")
        print (stages[life])
        continue
    
    guessed.append(guess)

    if guess in word:
        print("Good Guess")
        # replace alpha in placeholder 
        for i in range(0,len(word)):
            if word[i] == guess:
                placeholder[i] = guess
    else:
        print("Wrong Guess")
        life-=1    

    print (" ".join(placeholder))
    print (f"{life} lives left ")
    print (stages[life])

if life ==0:
    print ("LOST : Your hangman died ")
if "_" not in placeholder:
    print ("VICTORY : Your hangman survives ")



# TODO - make difficulty levels to choose from (put harder words list of upper levels and decide amount of lives accordingly )