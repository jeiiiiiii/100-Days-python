import random

def card_dealt():
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    card = random.choice(cards)
    return card

def calculate_score(sum_user_cards, sum_comp_cards):
    print(f"Your cards: {user_cards}, Current score: {sum_user_cards}")
    print(f"Computer's first card is: {comp_cards[0]}")

    # Check for blackjack
    if sum_user_cards == 21:
        print("User has blackjack\nYou Win!")
        return
    elif sum_comp_cards == 21:
        print("Computer has blackjack\nComputer Wins!")
        return

    # Player's turn
    while sum_user_cards < 21:
        new_card = input("Get another card? Y or N: ").lower()
        if new_card == "y":
            new_dealt_card = card_dealt()
            user_cards.append(new_dealt_card)
            sum_user_cards += new_dealt_card
            if sum_user_cards > 21 and 11 in user_cards:
                user_cards.remove(11)
                user_cards.append(1)
                sum_user_cards = sum(user_cards)
            print(f"Your cards: {user_cards}, Current score: {sum_user_cards}")
        else:
            break

    # Computer's turn
    while sum_comp_cards < 17:
        new_dealt_card = card_dealt()
        comp_cards.append(new_dealt_card)
        sum_comp_cards += new_dealt_card

    print(f"Computer's final cards: {comp_cards}, Final score: {sum_comp_cards}")

    # Determine the winner
    if sum_user_cards > 21:
        print("You went over 21. Computer Wins!")
    elif sum_comp_cards > 21 or sum_user_cards > sum_comp_cards:
        print("You Win!")
    elif sum_user_cards == sum_comp_cards:
        print("It's a draw!")
    else:
        print("Computer Wins!")

user_cards = []
comp_cards = []

for _ in range(2):
    user_cards.append(card_dealt())
    comp_cards.append(card_dealt())

user_sum = sum(user_cards)
comp_sum = sum(comp_cards)


calculate_score(sum_user_cards=user_sum, sum_comp_cards=comp_sum)
