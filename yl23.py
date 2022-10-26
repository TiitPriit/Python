import os
import random

decks = input("Sisestage kasutatavate tekkide arv: ")

deck = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]*(int(decks)*4)

VÕIDUD = 0
KAOTUSED = 0

def deal(deck):
    hand = []
    for i in range(2):
        random.shuffle(deck)
        card = deck.pop()
        if card == 11:card = "J"
        if card == 12:card = "Q"
        if card == 13:card = "K"
        if card == 14:card = "A"
        hand.append(card)
    return hand

def play_again():
    again = input("Tahad uuesti mängida? (Y/N) : ").lower()
    if again == "y":
        dealer_hand = []
        player_hand = []
        deck = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]*4
        game()
    else:
        print("Headaega!")
        exit()

def total(hand):
    total = 0
    for card in hand:
        if card == "J" or card == "Q" or card == "K":
            total+= 10
        elif card == "A":
            if total >= 11: total+= 1
            else: total+= 11
        else: total += card
    return total

def hit(hand):
    card = deck.pop()
    if card == 11:card = "J"
    if card == 12:card = "Q"
    if card == 13:card = "K"
    if card == 14:card = "A"
    hand.append(card)
    return hand

def clear():
    if os.name == 'nt':
        os.system('CLS')
    if os.name == 'posix':
        os.system('clear')

def print_results(dealer_hand, player_hand):
    clear()

    print("\n    TERE TULEMAST BLACKJACKI!\n")
    print("-"*30+"\n")
    print("    \033[1;32;40mVÕIDUD:  \033[1;37;40m%s   \033[1;31;40mKAOTUSED:  \033[1;37;40m%s\n" % (VÕIDUD, KAOTUSED))
    print("-"*30+"\n")
    print ("Diileril on " + str(dealer_hand) + " Summaks " + str(total(dealer_hand)))
    print ("Sul on " + str(player_hand) + " Summaks " + str(total(player_hand)))

def blackjack(dealer_hand, player_hand):
    global VÕIDUD
    global KAOTUSED
    if total(player_hand) == 21:
        print_results(dealer_hand, player_hand)
        print ("Palju õnne! Sul on Blackjack!\n")
        VÕIDUD += 1
        play_again()
    elif total(dealer_hand) == 21:
        print_results(dealer_hand, player_hand)
        print ("Anlaki, Sa kaotasid. Diiler sai blackjacki.\n")
        KAOTUSED += 1
        play_again()

def score(dealer_hand, player_hand):
        # score function now updates to global win/loss variables
        global VÕIDUD
        global KAOTUSED
        if total(player_hand) == 21:
            print_results(dealer_hand, player_hand)
            print ("Palju õnne! Sul on Blackjack!\n")
            VÕIDUD += 1
        elif total(dealer_hand) == 21:
            print_results(dealer_hand, player_hand)
            print ("Anlaki, Sa kaotasid. Diiler sai blackjacki.\n")
            KAOTUSED += 1
        elif total(player_hand) > 21:
            print_results(dealer_hand, player_hand)
            print ("Anlaki. Sa läksid üle. Sa kaotasid.\n")
            KAOTUSED += 1
        elif total(dealer_hand) > 21:
            print_results(dealer_hand, player_hand)
            print ("Diiler läks üle. You win!\n")
            VÕIDUD += 1
        elif total(player_hand) < total(dealer_hand):
            print_results(dealer_hand, player_hand)
            print ("Anlaki. Teie skoor pole diilerist kõrgem. Sa kaotasid.\n")
            KAOTUSED += 1
        elif total(player_hand) > total(dealer_hand):
            print_results(dealer_hand, player_hand)
            print ("Palju õnne. Teie skoor on kõrgem kui Diileril. Sa võidad\n")
            VÕIDUD += 1

def game():
    global VÕIDUD
    global KAOTUSED
    choice = 0
    clear()
    print("\n    TERE TULEMAST BLACKJACKI!\n")
    print("-"*30+"\n")
    print("    \033[1;32;40mVÕIDUD:  \033[1;37;40m%s   \033[1;31;40mKAOTUSED:  \033[1;37;40m%s\n" % (VÕIDUD, KAOTUSED))
    print("-"*30+"\n")
    dealer_hand = deal(deck)
    player_hand = deal(deck)
    print ("Diiler näitab " + str(dealer_hand[0]))
    print ("Sul on " + str(player_hand) + " Summaks " + str(total(player_hand)))
    blackjack(dealer_hand, player_hand)
    quit=False
    while not quit:
        choice = input("Kas sa tahad [H]it, [S]tand, või [Q]uit: ").lower()
        if choice == 'h':
            hit(player_hand)
            print(player_hand)
            print("Summa: " + str(total(player_hand)))
            if total(player_hand)>21:
                print('Läksid üle')
                KAOTUSED += 1
                play_again()
        elif choice=='s':
            while total(dealer_hand)<17:
                hit(dealer_hand)
                print(dealer_hand)
                if total(dealer_hand)>21:
                    print('Diiler läks üle, Sa võidad!')
                    VÕIDUD += 1
                    play_again()
            score(dealer_hand,player_hand)
            play_again()
        elif choice == "q":
            print("Headaega!")
            quit=True
            exit()


if __name__ == "__main__":
   game()
