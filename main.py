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

# code needs refactoring, too many redundancies.

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
player_hand = []
dealer_hand = []

def main():
    while len(player_hand) != 2 and len(dealer_hand) != 2:
        player_hand.append(random.choice(cards))
        dealer_hand.append(random.choice(cards))

    print(f"Your cards: {player_hand}, current total: {sum(player_hand)}")
    print(f"Computer's first card: {dealer_hand[0]}\n")


    while True:
        hit_or_pass = input("Type 'y' to get another card.\nType 'n' to pass: ")
        
        if hit_or_pass == "y":
            player_hand.append(random.choice(cards))
            print(f"\nYour cards: {player_hand}, current total: {sum(player_hand)}")
            
            if check_hand(player_hand):
                return
        else:
            break

    if sum(dealer_hand) < 17:
        dealer_hand.append(random.choice(cards))
        if check_hand(dealer_hand):
            return
        
        if sum(player_hand) <= 21:
            if sum(dealer_hand) > sum(player_hand):
                print(f"\nDealer hand: {dealer_hand} ,total: {sum(dealer_hand)}")
                print(f"Player hand: {player_hand} ,total: {sum(player_hand)}")
                print("\nYou lost!")
            elif sum(dealer_hand) == sum(player_hand):
                print(f"\nDealer hand: {dealer_hand} ,total: {sum(dealer_hand)}")
                print(f"Player hand: {player_hand} ,total: {sum(player_hand)}")
                print("\nDraw!")
            else:
                print(f"\nDealer hand: {dealer_hand} ,total: {sum(dealer_hand)}")
                print(f"Player hand: {player_hand} ,total: {sum(player_hand)}")
                print("\nYou win!")

# needs to be fixed, I think it's doing too much currently
def check_hand(lst):
    if sum(lst) > 21 and 11 in lst:
        index = lst.index(11)
        lst[index] = 1
        print("Card total went over 21 and you have an Ace(11), swapped it to Ace(1)") # need to fix this, this says "you" have an ace. it should be used by both dealer and player
        print(f"\nYour cards: {player_hand}, current total: {sum(player_hand)}\n")
    
    if sum(lst) > 21:
        if player_hand is lst:
            print("\nYou went over, you lose!\n")
            print(f"\nDealer hand: {dealer_hand} ,total: {sum(dealer_hand)}")
            print(f"Player hand: {player_hand} ,total: {sum(player_hand)}")
            return True
        elif dealer_hand is lst:
            print("\nDealer went over, you win!")
            print(f"\nDealer hand: {dealer_hand} ,total: {sum(dealer_hand)}")
            print(f"Player hand: {player_hand} ,total: {sum(player_hand)}")
            return True
    else:
        return False

if __name__ == "__main__":
    main()
