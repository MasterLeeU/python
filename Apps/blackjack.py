# Blackjack game
print('''          _____
         |A .  | _____
         | /.\ ||K ^  | _____
         |(_._)|| / \ ||Q _  | _____
         |  |  || \ / || ( ) ||J_ _ |
         |_____||  .  ||(_'_)||( v )|
                |_____||  |  || \ / |
                       |_____||  .  |
                              |_____|''')

#
import random
#Cards 
def deal_cards():
    """Returns a random card from the deck"""
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    card = random.choice(cards)
    return card

def calc_score(cards):
     """Calculates Cards"""
     if sum(cards) == 21 and len(cards) == 2:
          return 0
     if 11 in cards and sum(cards) > 21:
          cards.remove(11)
          cards.append(1)
     return sum(cards)
     
user_card = []
dealer_card = []

for _ in range(2):
     user_card.append(deal_cards())
     dealer_card.append(deal_cards())

user_score = calc_score(user_card)
dealer_score = calc_score(dealer_card)

if user_score == 0 or dealer_score == 0 or user_score > 21:
     is_game_over = True
else:
     hit = input("Type 'h' to hit or 's' to stand").lower()
     if hit == "h":
          user_card.append(deal_cards())
     else:
          is_game_over = True