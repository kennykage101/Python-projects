# Creating a Hangman Game
import random
from hangman_art import *
from hangman_words import word_list
from IPython.display import clear_output

chosen_word = random.choice(word_list)
word_length = len(chosen_word)
lives = 6
end_of_game = False
display = []

for char in chosen_word:
    display += "_"

print(logo)
while not end_of_game:
    guess = input("Guess a letter: ").lower()
    clear_output()
    if(guess in display):
        print(f"You've already guessed {guess}")
    for index in range(word_length):
        chosen_letter = chosen_word[index]
        if(guess == chosen_letter):
            display[index] = chosen_letter
            
    if(guess not in chosen_word ):
        print(f"letter {guess} is not in the chosen word. You lose a life.")
        lives -= 1
        if lives == 0:
            end_of_game = True
            print("You lose")
        
            
    if "_" not in display:
        end_of_game = True
        print("You win")
        
    print(f"{''.join(display)}") 
    print(stages[lives])
   