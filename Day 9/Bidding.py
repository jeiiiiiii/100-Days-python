
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
bids = {}
done = False

def find_the_bidder(record):
    highest = 0
    winner = ""
    
    for bidder in record:
        bid_amount = record[bidder]
        if bid_amount > highest:
            highest = bid_amount
            winner = bidder
    print(f"The winner is {winner} with the price of {highest}")
    

print(logo)

while not done:
    name = input("What is your name?: ")
    price = int(input("What is your bid?: "))
    bids[name] = price
    not_done = input("Is there any bidder? Type 'yes' or 'no': ").lower()
    
    if not_done == "no":
        done = True
        find_the_bidder(bids)
    elif not_done == "yes":
        print("\n" * 100)
        
