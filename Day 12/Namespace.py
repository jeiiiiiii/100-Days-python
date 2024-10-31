enemies = 1

def increase_enemies():
    enemies = 2
    print(f"Hi inside {enemies}")
    
increase_enemies()
print(f"outside {enemies}")

#Local Scope

def drink_potion():
    strenght = 2
    print(strenght)
    
drink_potion()
#print(strengt) error!

#Global

health = 10


def agility():
    agility = 2
    print(health)
    
agility()