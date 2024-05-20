import random
playerIn = True
dealerIn = True

# deck of cards / player of cards

deck = [2,3,4,5,6,7,8,9,10,2,3,4,5,6,7,8,9,10,2,3,4,5,6,7,8,9,10,2,3,4,5,6,7,8,9,10,
        'A','J','Q','K','A','J','Q','K','A','J','Q','K','A','J','Q','K']

playerhand = []
dealerHand = []

#deal the cards

def dealcard(turn):
    card = random.choice(deck)
    turn.append(card)
    deck.remove(card)

#calculate the total of each hand

def total(turn):
    total = 0
    face = ['J', 'K', 'Q']
    for card in turn:
        if card in range(1,11):
            total+= card
        elif card in face:
            total +=1
        else:
            if total > 11:
                total += 1
            else:
                total +=11
    return total
#check for winner
def revealDealerhand():
    if len(dealerHand) == 2:
        return dealerHand[0]
    elif len(dealerHand) > 2:
        return dealerHand[0], dealerHand[1]

#game loop

for _ in range(2):
    dealcard(dealerHand)
    dealcard(playerhand)

while playerIn or dealerIn:
    print(f"Dealer had {revealDealerhand()} and X")
    print(f"You have{playerhand} for a total of {total(playerhand)}")
    if playerIn:
        stayOrhit = input("1: Stay\n2: Hit\n")
    if total(dealerHand) > 16:
        dealerIn = False
    else:
        dealcard(dealerHand)

    if stayOrhit == '1':
        playerIn = False
    else:
        dealcard(playerhand)
    if total(playerhand) >= 21:
        break
    elif total(dealerHand) >=21:
        break

if total(playerhand) == 21:
    print(f"\n You have{playerhand} for a total of {total(playerhand)} and the dealer has {dealerHand} for a total of {total(dealerHand)}")
    print("Blackjack! You win!!!")
elif total(dealerHand) == 21:
    print(f"\n You have{playerhand} for a total of {total(playerhand)} and the dealer has {dealerHand} for a total of {total(dealerHand)}")
    print("Dealer Wins")
elif total(playerhand) > 21:
    print(f"\n You have{playerhand} for a total of {total(playerhand)} and the dealer has {dealerHand} for a total of {total(dealerHand)}")
    print("You bust! Dealer wins!")
elif total(dealerHand) > 21:
    print(f"\n You have{playerhand} for a total of {total(playerhand)} and the dealer has {dealerHand} for a total of {total(dealerHand)}")
    print("dealer busts! You win!")
elif 21 - total(dealerHand) < 21 - total(playerhand):
    print(f"\n You have{playerhand} for a total of {total(playerhand)} and the dealer has {dealerHand} for a total of {total(dealerHand)}")
    print("Dealer Wins")
elif 21 - total(dealerHand) > 21 - total(playerhand):
    print(f"\n You have{playerhand} for a total of {total(playerhand)} and the dealer has {dealerHand} for a total of {total(dealerHand)}")
    print("You win!")