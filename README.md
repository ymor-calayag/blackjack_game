# Blackjack Game

This command-line Blackjack game lets you play against a computer dealer. Cards are drawn randomly from a simulated deck with face cards counted as 10 and Aces counted as 11 or 1, depending on the hand’s total. The dealer follows standard rules, drawing cards until reaching 17 or more.

**Technologies Used**

+ ```Python```
+ ```random``` module for card selection
+ Functions for game logic and hand evaluation

**Features**

+ Random card dealing with appropriate values for face cards and Aces
+ Player can choose to “hit” (draw a card) or “pass”
+ Dealer automatically draws cards until total reaches 17 or higher
+ Ace value adjusted dynamically between 11 and 1 to prevent busting
+ Win, lose, and draw conditions clearly displayed

**What Users Can Do**

+ See their initial two cards and the dealer’s visible card
+ Choose to hit or pass during their turn
+ Receive feedback when Aces are adjusted from 11 to 1
+ View final results comparing their hand with the dealer’s

**The Process / How It’s Built**

+ The deck is represented by a list of card values, with face cards treated as 10 and Aces as 11 initially.
+ Cards are randomly dealt to player and dealer to start.
+ The player can hit to add cards or pass to end their turn.
+ The dealer draws cards automatically if their total is below 17.
+ The game checks for busts (hand totals over 21), adjusting Aces from 11 to 1 if necessary.
+ Results are printed based on who wins or loses.

