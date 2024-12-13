import random
stages = ['''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', '''
  +---+
  |   |
      |
      |
      |
      |
=========
''']


word_list = ["aardvark", "baboon", "camel"]

lives = 6

chosen_word = random.choice(word_list)
print(chosen_word)

placeholder = "_" * len(chosen_word)
print(placeholder)

done = False
correct = []

while not done:
    guess = str(input("Guess the word: ")).lower()

    display = ""
    print(lives)

    for letter in chosen_word:
        if letter == guess:
            display += letter
            correct.append(letter)
        elif letter in correct:
            display += letter
        else:
            display += "_"
            
    print(display)
    
    if guess not in chosen_word:
        lives -= 1
        if lives == 0:
            done = True
            print("Game Over!")
    
    if "_" not in display:
        done == True
        print("Nicely done")
        break

    print(stages[lives])



