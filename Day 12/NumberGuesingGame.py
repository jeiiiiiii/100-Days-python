from random import randint

#Random Number
random_number = randint(1, 100)

def Guessing_game(number):
    #Attempts
    EASY = 10
    HARD = 5
    
    #Headline
    print("Welcome to the number guessing game!")
    print("Guess the number from 1 - 100")
    
    #Choose difficulty
    difficulty = input("Easy or hard: ").lower()
    
    while True:
        #Easy

        if difficulty == "easy":
            print(f"You have {EASY} attempts remaining to guess the number")
            guessed_number = int(input("Make a guess: "))
            if guessed_number != number:
                EASY -= 1

        #Hard
        if difficulty == "hard":
            print(f"You have {HARD} attempts remaining to guess the number")
            guessed_number = int(input("Make a guess: "))
            if guessed_number != number:
                HARD -= 1
                
        #Comments
        if guessed_number > number:
            print("High")
        elif guessed_number < number:
            print("low")
        
        #Loop break
        if guessed_number == number:
            print("You got it right!")
            break

Guessing_game(number= random_number)