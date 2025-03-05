#!/usr/bin/python3

# Import packages
import random
from hangman_art import stages, logo
from hangman_words import word_list

# Randomly choose a word from the word_list and assign it to the variable called chosen_world
chosen_word = random.choice(word_list)

#Create a variable called 'lives' to keep track of the number of lives left. 
lives = 6

# Create a variable that signifies end of game
end_of_game = False

#Create an empty List called display.
#For each letter in the chosen_word, add a "_" to 'display'.
display = []
for letter in chosen_word:
    display.append("_")
    
# print hangman logo
print(logo)

# Use a while loop to let the user guess again.
# The loop should only stop once the user has guessed all the letters in the chosen_word and 'display has not more blanks ("_")
while not end_of_game:
    print(f"Word to guess: {''.join(display)}")
    guess = input("Guess a letter: ").lower()

    #If the user has entered a letter they've already guessed, print the letter and let them know.
    if guess in display:
        print(f"You've already correctly guessed '{guess}'. Guess a different letter.")

    #Loop through each position in the chosen_word;
    #If the letter at that position matches 'guess' then reveal that letter in the display at that position.
    for i in range(len(chosen_word)):
        if chosen_word[i] == guess:
            display[i] = guess

    #If guess is not a letter in the chosen_word,
    #Then reduce 'lives' by 1. 
    #If lives goes down to 0 then the game should stop and it should print "You lose."
    if guess not in chosen_word:
        #If the letter is not in the chosen_word, print out the letter and let them know it's not in the word.
        print(f"You guessed '{guess}', that's not in the word. You lose a life.")
        lives-=1
    
    if lives == 0:
        end_of_game = True
        print("Game over! You lost!")
    
    #Join all the elements in the list and turn it into a String.
    print(f"{' '.join(display)}")

    #Print 'display' and you should see the guessed letter in the correct position and every other letter replace with "_".
    #print(display)

    if "_" not in display:
        end_of_game = True
        print("You win!")
    
    #print the ASCII art from 'stages' that corresponds to the current number of 'lives' the user has remaining.
    print(stages[lives])

    # print the number of lives left
    print(f"****************************{lives}/6 LIVES LEFT****************************")

     