import random as rd

error = 'Please type a valid answer'
error2 = 'Type "y" for Yes and "n" for No'
rules = ("\n1- your goal is to reach 21, or the closest to 21 without surpassing it;\n2- You receive 2 initial cards from the deck and can buy more if you want;\n3- You start with 100 coins to bet, you can't bet more than you have;\n4- game is over once you reach 0 coins;\n5- The dealers will also play, if it gets closer to 21 than you without surpassing you lose;\n6- if both you and the dealer gets the same number, it's a draw and nothing happens.")

deck = 4*['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']
values = {'A':1, '2':2, '3':3, '4':4, '5':5, '6':6, '7':7, '8':8, '9':9, '10':10, 'J':10, 'Q':10, 'K':10}

#Dealer's Play function
def dealer_play(deck,values):

    # Define the cards received by the dealer and the value of it's hand
    dealer_hand = rd.sample(deck,2) #This rd function is used to choose two random cards from the deck
    dealer_sum = sum(values[card] for card in dealer_hand if card in values) #this sum function is structured to find the values of the received cards (dealer_hand) in the 'values' dictionary and add those values together

    # Decision making loop, condition for the dealer to buy a new card or not
    while dealer_sum < 17:
        ncard = rd.choice(deck) #rd function do choose a random card from the deck, the difference from the sample is the amount of cards chosen
        dealer_hand.append(ncard) #the .append was used to add the new card to the initial object (dealer_hand)
        dealer_sum += values.get(ncard,0) # the .get is used to retrieve the ncard value from the dictionary, and the += operation is responsible to add this value to the previous sum

    return dealer_hand, dealer_sum

#Introduction
while True:
    m1 = input('This is a blackjack game, would you like to learn the rules? [y/n]: ')
    if m1.lower().strip() == 'y' or m1.lower().strip() == 'n':
         m1 = m1.lower().strip()
         break
    else:
         print(error2)

if m1 == 'y':
    print(rules)

#Starting amount of coins
wallet = 100

#Main Game
while wallet > 0:
    #loop for starting betting amount        
    while True:
        try:
            bet = int(input(f'\nYou have {wallet} coins, how much do you want to bet?: '))
            if bet < 0:
                print(error)
            elif bet > wallet:
                print("\nYou don't have enough coins, please type a valid amount")
            else:
                break
        except ValueError:
            print(error)

    #Using rd to define the player starting cards
    hand = rd.sample(deck,2)
    hand_sum = sum(values[cards] for cards in hand if cards in values)
    p1 = print(f'\nYour cards are {hand[0]} and {hand[1]}')

    #Verifying user intention to draw another card
    while True:
        m3 = input(f'\nYour hand is in {hand_sum}, would you like to draw one more card? [y/n]: ')
        if m3.lower().strip() == 'y' or m3.lower().strip() == 'n':
            m3 = m3.lower().strip()
            break
        else:
            print(error2)

    #Loop for drawing new cards
    if m3 == 'y':
        while hand_sum < 22:
            ncard2 = rd.choice(deck)
            hand_sum += values.get(ncard2,0)
            if hand_sum > 21:
                wallet = wallet-bet
                print(f"\nYour new card was {ncard2}, you've got {hand_sum} \nOh no! You surpassed 21 and lost {bet} coins\nYou now have {wallet} coins")                
                break    
            while True:
                m7 = input(f'Your new card was {ncard2}, your hand is in {hand_sum}. Want to drawn another card? [y/n]: ')
                if m7.lower().strip() == 'y' or m7.lower().strip() == 'n':
                    m7 = m7.lower().strip()
                    break
                else:
                    print(error2)
            if m7 == 'n':
                break
            
    if hand_sum <= 21:


        dealer_hand, dealer_sum = dealer_play(deck, values)

        # print(f"You've got {hand_sum} and the dealer got {dealer_sum}")

        print(dealer_hand)
        if hand_sum == dealer_sum:
            print(f"You both got {hand_sum}! It's a draw")
        elif hand_sum > dealer_sum and hand_sum <= 21:
            print(f"You won! your hand was {hand_sum} and the dealer's hand was {dealer_sum} \nYou now have {wallet+bet} coins!")
            wallet = wallet+bet
        elif dealer_sum > 21 and hand_sum <= 21:
            print(f"You won! your hand was {hand_sum} and the dealer's hand was {dealer_sum} \nYou now have {wallet+bet} coins!")
            wallet = wallet+bet
        elif dealer_sum > hand_sum and dealer_sum <= 21:
            print(f"You lost... Your hand was {hand_sum} and the dealer's hand was {dealer_sum} \nYou now have {wallet-bet} coins.")
            wallet = wallet-bet

    #Condition to start another round
    if wallet > 0:
        while True:
            m4 = input('\nWould you like to play again? [y/n]: ')
            if m4.lower().strip() == 'y' or m4.lower().strip() == 'n':
                m4 = m4.lower().strip()
                break
            else:
                print(error2)
    else:
        print("Oh no... seems like you don't have enough coins for another round")
        break    

    if m4 == 'n':
        break


print('\nThanks for trying this code!\n')

