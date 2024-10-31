logo = '''
                         ___________
                         \         /
                          )_______(
                          |"""""""|_.-._,.---------.,_.-._
                          |       | | |               | | ''-.
                          |       |_| |_             _| |_..-'
                          |_______| '-' `'---------'` '-'
                          )"""""""(
                         /_________\\
                       .-------------.
                      /_______________\\
'''

print(logo)
done = False
bids ={}

while not done:
    name = input("What is your name?: ")
    price = int(input("What is your bid?: "))
    
    bids[name] = price
    
    not_done = input("Is there any bidder? Type 'yes' or 'no': ").lower()
    
    if not_done == "no":
        winner = max(bids, key=bids.get)
        print(f"The winner is {name} with the price of {price}")
        break
    elif not_done == "yes":
        print("\n" * 20)