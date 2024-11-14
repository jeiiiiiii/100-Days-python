from random import randint
from GameData import data



def information():
    #Random number to be set into the data
    random_numberA = randint(1, 49 )
    random_numberB = randint(1, 49 )
    compareA = data[random_numberA]
    compareB = data[random_numberB]
    
    #Data description of Compare A
    name = compareA["name"]
    description = compareA["description"]
    country = compareA["country"]
    follower_count = compareA["follower_count"]
    compare_A = print(f"Compare A: {name}, a { description}, from { country}")
    
    #Data description of Compare B
    name = compareB["name"]
    description = compareB["description"]
    country = compareB["country"]
    follower_count = compareB["follower_count"]
    compare_B = print(f"Against B: {name}, a { description}, from { country}")
    
information()


def comparison(answer):
    profile_A, follower_A = information()
    profile_B, follower_B = information()
    if follower_A == follower_B:
        profile_b, followers_b = information()
    score = 0
    correct = True
    
    while correct:
        if correct:
            print(f"You're right! Current score: {score} ")
            score += 1
        print(f"Compare A:{profile_A}")


answer = input("Who has more followers? A or B").lower()
comparison(answer)
