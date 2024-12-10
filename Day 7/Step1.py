import random

word_list = ["aardvark", "baboon", "camel"]

chosen_word = random.choice(word_list)
print(chosen_word)

guess = str(input("Guess the word: ")).lower()

for letter in chosen_word:
    if letter == guess:
        print("Correct")
    else:
        print("Wrong")
        
