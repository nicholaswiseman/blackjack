import random
import os
import time

def clear():
    os.system( 'cls' )
	
class Card():
    
    def __init__(self,suit,value):
        self.suit = suit
        self.value = value
    def __str__(self):
        return f"-----\n|{self.value}  |\n| {self.suit[0]} |\n|  {self.value}|\n-----"
	
class Player():
    
    hand = []
    
    def __init__(self, credit):
        self.credit = credit
    
    def draw_card(self,deck):
        while 1:
            card_num = random.randint(0,51)
            if deck[card_num]=='CARD DRAWN':
                continue
            else:
                self.hand.append(deck[card_num])
                deck[card_num] = 'CARD DRAWN'
                break
    
    def get_card(self,card):
            self.hand.append(card)
    
    def discard(self):
        self.hand = []
    
    def __str__(self):
        string = ''
        for card in self.hand:
            string=string+'-----  '
        string = string+"\n"
        for card in self.hand:
            string=string+f'|{card.value}  |  '
        string=string+'\n'
        for card in self.hand:
            string=string+f'| {card.suit[0]} |  '
        string=string+'\n'
        for card in self.hand:
            string=string+f'|  {card.value}|  '
        string=string+'\n'
        for card in self.hand:
            string=string+'-----  '
        string=string+f'\n{self.credit} credits'
        return string
	
class Dealer():
    
    hand = []
    
    def __init__(self):
        pass
    
    def draw_card(self,deck):
        while 1:
            card_num = random.randint(0,51)
            if deck[card_num]=='CARD DRAWN':
                continue
            else:
                self.hand.append(deck[card_num])
                deck[card_num] = 'CARD DRAWN'
                break
    def discard(self):
        self.hand = []
    
    def __str__(self):
        string = ''
        if self.hand == []:
            string = string + '-----  -----\n'
            string = string + '|\ /|  |\ /|\n'
            string = string + '| X |  | X |\n'
            string = string + '|/ \|  |/ \|\n'
            string = string + '-----  -----\n'
        elif len(self.hand) == 1:
            string = string + '-----  -----\n'
            string = string + f'|{self.hand[0].value}  |  |\ /|\n'
            string = string + f'| {self.hand[0].suit[0]} |  | X |\n'
            string = string + f'|  {self.hand[0].value}|  |/ \|\n'
            string = string + '-----  -----\n'
        else:
            for card in self.hand:
                string=string+'-----  '
            string = string+"\n"
            for card in self.hand:
                string=string+f'|{card.value}  |  '
            string=string+'\n'
            for card in self.hand:
                string=string+f'| {card.suit[0]} |  '
            string=string+'\n'
            for card in self.hand:
                string=string+f'|  {card.value}|  '
            string=string+'\n'
            for card in self.hand:
                string=string+'-----  '
            string=string+'\n'
        return string
	
def get_deck():
    deck = []
    for suit in ['Spades', 'Clubs','Hearts','Diamonds']:
        for value in ['A',2,3,4,5,6,7,8,9,10,'J','Q','K']:
            deck.append(Card(suit,value))
    random.shuffle(deck)
    for card in deck:
	    print("SHUFFLING")
	    print(card)
	    time.sleep(0.04)
	    clear()
    return deck

def show_table():
	clear()
	print(dealer)
	print(check_hand(dealer))
	print(player)
	print(check_hand(player))
	print('\n')
	time.sleep(1)

def check_hand(player):
	cards = []
	ace_count = 0
	for card in player.hand:
		if (card.value == 'J' or card.value == 'Q' or card.value == 'K'):
			cards.append(10)
		elif (card.value == 'A'):
			cards.append(11)
			ace_count = ace_count+1
		else:
			cards.append(card.value)
	if sum(cards) <= 21:
		return sum(cards)
	elif (sum(cards) > 21 and ace_count>0):
		total = sum(cards)
		while sum(cards)>21 and ace_count>0:
			total = total - 10
			ace_count = ace_count - 1
		if total<=21:
			return total
		else:
			return 'BUST'
	else:
		return 'BUST'

def get_wager():
	while 1:
		try:
			bet = int(input("Place Your Bet: "))
		except:
			print("Please enter an integer!")
		else:
			if bet <= player.credit:
				return bet
			else:
				print("Can't bet more than you have!")
	
		
if 1:#__name__ == "_main__":
	#set up the table:
	#instantiate the player and the dealer and deal to the player
	player = Player(100)
	dealer = Dealer()
	play_again = True
	
	while play_again == True:
		mydeck = get_deck()
		dealer.draw_card(mydeck)
		show_table()
		wager = get_wager()
		player.draw_card(mydeck)
		show_table()
		player.draw_card(mydeck)
		show_table()
		
		#if they get less than 21 ask them to hit 
		if check_hand(player)<21:
			choice = input("Hit or Pass?")
			hit = choice.lower() == 'hit'
		else:
			hit = False
		
		#keep asking to hit until they pass or bust or get 21
		while hit == True: 
			player.draw_card(mydeck)
			show_table()
			if check_hand(player) == 'BUST' or check_hand(player) == 21 or check_hand(player) == '21':
				break
			choice = input("Hit or Pass? ")
			hit = choice.lower() == 'hit'
		
		#if the player has 21 or busted the hands over
		if check_hand(player) == 'BUST':
			print("YOU BUSTED!")
			print(f'YOU LOSE {wager} CREDITS!')
			time.sleep(1)
			player.credit = player.credit - wager
		elif check_hand(player) == 21 and len(player.hand)==2:
			print("BLACKJACK!")
			print(f'YOU GET {wager} CREDITS!')
			time.sleep(1)
			player.credit = player.credit + wager
		else: #if the player doesnt bust or get BJ the dealer will draw next card
			#dealer.draw_card(mydeck)
			dealer.draw_card(mydeck)
			show_table()
			
			while 1:
				if check_hand(dealer)<check_hand(player):
					dealer.draw_card(mydeck)
					show_table()
				if check_hand(dealer) == check_hand(player) and check_hand(dealer)<=11:
					dealer.draw_card(mydeck)
					show_table()
				if check_hand(dealer) == 'BUST' or check_hand(dealer)>check_hand(player) or check_hand(dealer)==check_hand(player):
					break
			
			if check_hand(dealer) == 'BUST':
				print("DEALER BUSTS! PLAYER WINS!")
				print(f'YOU GET {wager} CREDITS!')
				time.sleep(1)
				player.credit = player.credit + wager
			elif (check_hand(player)>check_hand(dealer)):
				print("PLAYER WINS")
				print(f'YOU GET {wager} CREDITS!')
				time.sleep(1)
				player.credit = player.credit + wager
			elif (check_hand(player)<check_hand(dealer)):
				print("DEALER WINS")
				print(f'YOU LOST {wager} CREDITS!')
				time.sleep(1)
				player.credit = player.credit - wager
			elif (check_hand(player) == check_hand(dealer)):
				print("PUSH")
				time.sleep(1)

		#show_table()
		player.discard()
		dealer.discard()
		if player.credit == 0:
			print("Sorry! You're out of credit!")
			break
		elif (input("Play Again? (Yes/No)").lower() != 'yes'):
			break