import random
import blackjack_art

print(blackjack_art.logo)

# Blackjack/21 Rules
# Add your cards without going over 21 (or you lose)
# J, Q, K each count as 10
# Ace is either 1 or 11
# Dealer deals the first cards, you can see his first card.
# You can "hit" to get another card 
# If the dealers card is <17 (16 and under) the dealer must take another card

# To simplify this, we would right J, Q, K as 10s. So there are 4 10s
# Ace will start as 11 and will stay as 11 unless the user goes over 21
# And if a card is drawn from a deck we will not remove it from the deck

def deal_card():
    # returns a random number from the list```
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    draw_card = random.choice(cards)
    return draw_card

def show_cards(player_lst, dealer_lst):
    print(f"Your cards: {player_lst}, current total: {sum(player_lst)}")
    print(f"Computer's first card: {dealer_lst[0]}\n")

def calculate_score(cards_lst):
    # blackjack
    if sum(cards_lst) == 21 and len(cards_lst) == 2:
        return 0 
    
    # dealer draws card if card total is less than 17
    while True:
        if cards_lst == dealer_hand and sum(cards_lst) < 17:
            dealer_hand.append(deal_card())
        else:
            break

    # swaps Ace(11) with Ace(1) if card total exceeds 21
    if sum(cards_lst) > 21 and 11 in cards_lst:
        index = cards_lst.index(11)
        cards_lst[index] = 1

    return sum(cards_lst)

player_hand = []
dealer_hand = []
is_game_over = False

for _ in range(2):
    # draws two numbers/cards to each list
    player_hand.append(deal_card())
    dealer_hand.append(deal_card())

show_cards(player_hand, dealer_hand)

# there are game-breaking issues here
def check_game_status():
    if calculate_score(dealer_hand) == calculate_score(player_hand):
        is_game_over = True
        print(f"Your cards: {player_hand}")
        print(f"Computer's cards: {dealer_hand}")
        print("Draw!")
    elif calculate_score(player_hand) == 0:
        is_game_over = True
        print("You win!")
    elif calculate_score(dealer_hand) == 0:
        is_game_over = True
        print(f"Computer's cards: {dealer_hand}")
        print("You lost!")
    elif calculate_score(player_hand) > 21:
        is_game_over = True
        show_cards(player_hand, dealer_hand)
        print("You went over 21, you lost!")
    elif calculate_score(dealer_hand) > 21:
        is_game_over = True
        print(f"Computer's cards: {dealer_hand}")
        print("Computer went over 21, you win!")
    else:
        hit_or_pass = input("Type 'y' to get another card.\nType 'n' to pass: ")
        if hit_or_pass == "y":
            player_hand.append(deal_card())
            show_cards(player_hand, dealer_hand)
        else:
            is_game_over = True

while is_game_over == False:
    check_game_status()

if calculate_score(player_hand) > calculate_score(dealer_hand):
    print(f"Your cards: {player_hand}")
    print(f"Computer's cards: {dealer_hand}")
    print("You win!")
else:
    print(f"Your cards: {player_hand}")
    print(f"Computer's cards: {dealer_hand}")
    print("You lost!")
