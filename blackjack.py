#=====================
# Program: Blackjack
#=====================
import random

def main():
    print('Single Deck Blackjack: Dealer hits on soft 17 and Blackjack pays 2:3.')
    total_money_left = int(input('Enter starting balance: '))

    keep_playing = True
    while keep_playing:
        round_bet = int(input('Enter bet amount: '))
        if round_bet > total_money_left:
            print('Insufficient funds. Please restart game or enter lower bet amount.')
            round_bet = int(input('Enter bet amount: '))
        total_money_left = total_money_left - round_bet
        initial_random_deal()

        dealer_hand_value = hand_value_calc(dealer_hand)
        user_hand_value = hand_value_calc(user_hand)
        if user_hand_value == 21:
            total_money_left += 2*round_bet + (round_bet * 0.5)
            print('\n')
            print('Dealer hand: ', dealer_hand, '(Value: ',dealer_hand_value,')')
            print('Your hand: ', user_hand, '(Value: ',user_hand_value, ')')
            print('BLACKJACK')
            print('\n')
            print('-------------------------------')
            print('USER WINS')
        else:
            print('\n')
            print('Dealer hand: ', dealer_hand, '(Value: ',dealer_hand_value,')')
            print('Your hand: ', user_hand, '(Value: ',user_hand_value, ')')
            print('\n')
            done = False
            while not done:
                user_decision = input('hit, stand, or double? ')
                if user_decision in ('hit', 'Hit', 'HIT'):
                    user_hit()
                    user_hand_value = hand_value_calc(user_hand)
                    print('Your hand: ', user_hand, '(Value: ',user_hand_value, ')')
                    if user_hand_value > 21:
                        print('USER BUST')
                        done = True
                elif user_decision in ('stand', 'Stand', 'STAND', 's', 'S'):
                    done = True
                elif user_decision in ('double', 'Double', 'DOUBLE', 'd', 'D'):
                    if total_money_left < round_bet:
                        print('Insufficient funds for doubling. Choose different option.')
                        done = False
                    else:
                        total_money_left = total_money_left - round_bet
                        round_bet *= 2
                        user_hit()
                        user_hand_value = hand_value_calc(user_hand)
                        print('Your hand: ', user_hand, '(Value: ',user_hand_value, ')')
                        if user_hand_value > 21:
                            print('USER BUST')
                        done = True
            dealer_play()
            dealer_hand_value = hand_value_calc(dealer_hand)
            print('\n')
            print('Dealer hand: ', dealer_hand, '(Value: ',dealer_hand_value,')')
            print('Your hand: ', user_hand, '(Value: ',user_hand_value, ')')
            print('\n')
            print('-------------------------------')


            if user_hand_value > 21:
                print('DEALER WINS')
            elif (dealer_hand_value < user_hand_value) and (user_hand_value <= 21):
                print('USER WINS')
                total_money_left += 2*round_bet
            elif (dealer_hand_value > user_hand_value) and (dealer_hand_value <= 21):
                print('DEALER WINS')
            elif dealer_hand_value == user_hand_value:
                print('PUSH')
                total_money_left += round_bet
            else:
                print('USER WINS')
                total_money_left += 2*round_bet
        print('TOTAL MONEY LEFT: $', total_money_left)
        print('-------------------------------')



def dealer_play():
    global dealer_hand_value
    global dealer_hand
    done = False
    while not done:
        dealer_hand_value = hand_value_calc(dealer_hand)
        if dealer_hand_value >= 17:
            done = True
        else:
            dealer_hit()
            dealer_hand_value = hand_value_calc(dealer_hand)
            if dealer_hand_value > 21:
                done = True
                print('DEALER BUST')

def dealer_hit():
    global dealer_hand
    global cards
    rand_int = random.randint(0,(len(cards))-1)
    rand_card_dealer = cards[rand_int]
    cards.pop(rand_int)
    dealer_hand += rand_card_dealer


def user_hit():
    global user_hand
    global cards
    rand_int = random.randint(0,(len(cards))-1)
    rand_card_4 = cards[rand_int]
    cards.pop(rand_int)
    user_hand += rand_card_4

def initial_random_deal():
    global dealer_hand
    global user_hand
    global cards
    cards = ['2', '3', '4', '5', '6', '7' ,'8', '9', 'T', 'J', 'Q', 'K', 'A',
             '2', '3', '4', '5', '6', '7' ,'8', '9', 'T', 'J', 'Q', 'K', 'A',
             '2', '3', '4', '5', '6', '7' ,'8', '9', 'T', 'J', 'Q', 'K', 'A',
             '2', '3', '4', '5', '6', '7' ,'8', '9', 'T', 'J', 'Q', 'K', 'A']
    rand_int = random.randint(0,51)
    rand_card_1 = cards[rand_int]
    cards.pop(rand_int)

    rand_int = random.randint(0,50)
    rand_card_2 = cards[rand_int]
    cards.pop(rand_int)

    rand_int = random.randint(0,49)
    rand_card_3 = cards[rand_int]
    cards.pop(rand_int)

    dealer_hand = rand_card_1
    user_hand = rand_card_2 + rand_card_3

def hand_value_calc(hand):
    hand_value = 0
    for i in str(hand):
        if i in ('T','J', 'Q', 'K'):
            hand_value += 10
        elif i in ('2', '3', '4', '5', '6', '7' ,'8', '9'):
            hand_value += int(i)
        elif i == 'A':
            if hand_value <= 10:
                hand_value += 11
            else:
                hand_value += 1
    return hand_value

main()
