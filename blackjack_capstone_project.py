from blackjack_capstone_art import logo
import random
import os
cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

def calculate_score(cards):
    """"Take a list of cards and returns the score calculated from the cards"""
    if sum(cards) == 21 and len(cards) == 2:
        return 0
    if 11 in cards and sum(cards) > 21:
        cards.remove(11)
        cards.append(1)
    return sum(cards)

def compare(user_score, computer_score):
	if user_score == computer_score:
		return "Draw 🙃"
	elif computer_score == 0:
		return "Lose, opponent has Blackjack 😱"
	elif user_score == 0:
		return "Win with a Blackjack 😎"
	elif user_score > 21:
		return "You went over. You lose 😭 "
	elif computer_score > 21:
		return "Opponent went over. You win 😁"
	elif user_score > computer_score:
		return "You win 😃"
	else:
		return "You lose 😤"
	
def blackjack():
	print(logo)
	player_random_cards = random.choices(cards, k=2)
	computer_random_cards = random.choices(cards, k=2)
	is_game_over = False

	while not is_game_over:
		user_score = calculate_score(player_random_cards)   
		computer_score = calculate_score(computer_random_cards)    
		print(f"Your cards: {player_random_cards}, current score: {user_score}\nComputer's first card: {computer_random_cards[0]}")
		if(user_score == 0 or computer_score == 0 or user_score > 21):
				is_game_over = True
		else:
				user_should_deal = input("Type 'y' to get another card, type 'n' to pass: ")
				if user_should_deal == "y":
								player_random_cards.append(random.choice(cards))
				else:
						is_game_over = True        
	while computer_score != 0 and computer_score < 17:
		computer_random_cards.append(random.choice(cards))
		computer_score = calculate_score(computer_random_cards)
	print(f"Your final hand: {player_random_cards}, final score: {user_score}")
	print(f"Computer's final hand: {computer_random_cards}, final score: {computer_score}")
	print(compare(user_score, computer_score))

while input("Do you want to play a game of Blackjack? Type 'y' or 'no': ") == 'y':
  os.system('cls')
  blackjack()
