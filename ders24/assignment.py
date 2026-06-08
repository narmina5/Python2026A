"""
Sadə Blackjack oyunu - Komputerə qarşı

1) Kartları listdə və ya dictdə tut
2) İstifadəçiyə və kompyuterə əvvəlcə hər birinə 2 kart verilir
3) İstifadəçi "hit" (yeni kart) və ya "stand" (dayan) seçir
4) 21-i keçsə -> uduzur
5) Kompüterdə 17-dən kiçikdirsə, kart çəkməyə davam edir
6) 21-ə ən yaxın olan qalibdir

Tələb: Bu qaydalara uyğun proqram yazın
"""
import random

card_category = ['Spades', 'Hearts', 'Diamonds', 'Clubs']
card_list = ['Ace', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King']
deck = []
for category in card_category:
    for card in card_list:
        deck += [(card, category)]

def value(card):
    if card[0] == 'Ace':
        return 11
    elif card[0] in ['Jack', 'Queen', 'King']:
        return 10
    else:
        return int(card[0])

random.shuffle(deck)
player_hand = [deck.pop(), deck.pop()]
computer_hand = [deck.pop(), deck.pop()]

while True:
    player_score = sum(value(card) for card in player_hand)
    computer_score = sum(value(card) for card in computer_hand)

    move = input('Make your move: ').lower()
    if move == 'hit':
        new_card = deck.pop()
        player_hand.append(new_card)
    elif move == 'stand':
        break
    else:
        print('Invalid move')
        continue

    if player_score > 21:
        print("Computer won!")
        break

while computer_score < 17:
    new_card = deck.pop()
    computer_hand.append(new_card)
    computer_score += value(new_card)

if computer_score > 21:
    print("Player won!")
else:
    print("Draw!")

print(f"Player's hand': {player_hand}, Player's score: {player_score}")
print(f"Computer's hand: {computer_hand}, Computer's score: {computer_score}")
