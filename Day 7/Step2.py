import random

word_list = ["aardvark", "baboon", "camel"]

chosen_word = random.choice(word_list)
print(chosen_word)


placeholder = "_" * len(chosen_word)
print(placeholder)

guess = str(input("Guess the word: ")).lower()

display = ""


for letter in chosen_word:
    if letter == guess:
        display += letter
    else:
        display += "_"
        
print(display)