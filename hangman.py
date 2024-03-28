
import random

stages = ['''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', '''
  +---+
  |   |
      |
      |
      |
      |
=========
''']


#Step 1
word_list = ["ardvark", "baboon", "camel"]

# Randomly choose a word from the word_list and assign it to the variable called chosen_world
chosen_word = random.choice(word_list)

## Testing Code
print(f"Pssst, the solution is {chosen_word}")


#Create a variable called 'lives' to keep track of the number of lives left. 
#Set 'lives' to equal 6.
lives = 6

#Create an empty List called display.
#For each letter in the chosen_word, add a "_" to 'display'.
display = []
for letter in chosen_word:
    display.append("_")
#print(display)
# Ask the  user to guess a latter and assign their answer to the variable called guess. Make guess lowercase.
    
# Use a while loop to let the user guess again.
#The loop should only stop once the user has guessed all the letters in the chosen_word and 'display has not more blanks ("_")

end_of_game = False

while not end_of_game:
    guess = input("Guess a letter: ").lower()

    #Loop through each position in the chosen_word;
    #If the letter at that position matches 'guess' then reveal that letter in the display at that position.
    for i in range(len(chosen_word)):
        if chosen_word[i] == guess:
            display[i] = guess


    #If guess is not a letter in the chosen_word,
    #Then reduce 'lives' by 1. 
    #If lives goes down to 0 then the game should stop and it should print "You lose."
    if guess not in chosen_word:
        lives-=1
    
    if lives == 0:
        end_of_game = True
        print("You lose")
    
    #Join all the elements in the list and turn it into a String.
    print(f"{' '.join(display)}")

    #Print 'display' and you should see the guessed letter in the correct position and every other letter replace with "_".
    #print(display)

    if "_" not in display:
        end_of_game = True
        print("You win!")
    
    #print the ASCII art from 'stages' that corresponds to the current number of 'lives' the user has remaining.
    print(stages[lives])
     