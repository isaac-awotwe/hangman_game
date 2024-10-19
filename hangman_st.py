
# import packages
import streamlit as st
import random
from hangman_words import word_list
from hangman_art import stages, logo

# Randomly choose a word from the word_list and assign it to the variable called chosen_world
if "chosen_word" not in st.session_state:
    st.session_state.chosen_word = random.choice(word_list)

#Create a variable called 'lives' to keep track of the number of lives left. 
if "lives" not in st.session_state:
    st.session_state["lives"] = 6

# Create a variable that signifies end of game
if "end_of_game" not in st.session_state:
    st.session_state.end_of_game = False

#Create an empty List called display.
#For each letter in the chosen_word, add a "_" to 'display'.
if "display" not in st.session_state:
    st.session_state["display"] = ["_" for letter in st.session_state.chosen_word]

# create a variable that represent the key to the text input
if "key" not in st.session_state:
    st.session_state.key = 0

if "guess" not in st.session_state:
    st.session_state.guess = ""

# define a function to increment the key for text input
# def key_auto_incr():
#     st.session_state.key +=1

# print hangman logo
st.text(logo)


# Use a while loop to let the user guess again.
#The loop should only stop once the user has guessed all the letters in the chosen_word and 'display has not more blanks ("_")
while not st.session_state.end_of_game:
    st.session_state.key+=1
    guess = st.text_input("Guess a letter: ", key = st.session_state.key).lower()

    #If the user has entered a letter they've already guessed, print the letter and let them know.
    if st.session_state.guess in st.session_state.display:
        st.markdown(f"You've already correctly guessed '{st.session_state.guess}'. Guess a different letter.")
    
    #Loop through each position in the chosen_word;
    #If the letter at that position matches 'guess' then reveal that letter in the display at that position.
    for i in range(len(st.session_state.chosen_word)):
        if st.session_state.chosen_word[i] == st.session_state.guess:
            st.session_state.display[i] = st.session_state.guess
    

    #If guess is not a letter in the chosen_word,
    #Then reduce 'lives' by 1. 
    #If lives goes down to 0 then the game should stop and it should print "You lose."
    if st.session_state.guess not in st.session_state.chosen_word:
        #If the letter is not in the chosen_word, print out the letter and let them know it's not in the word.
        st.markdown(f"You guessed '{st.session_state.guess}', that's not in the word. You lose a life.")
        st.session_state.lives-=1


    if st.session_state.lives == 0:
        st.session_state.end_of_game = True
        st.write("Game over! You lost!")
    
    #Join all the elements in the list and turn it into a String.
    st.write(f"{' '.join(st.session_state.display)}")


    #Print 'display' and you should see the guessed letter in the correct position and every other letter replace with "_".
    st.write(st.session_state.display)

    if "_" not in st.session_state.display:
        st.session_state.end_of_game = True
        st.write("You win!")
    
    #print the ASCII art from 'stages' that corresponds to the current number of 'lives' the user has remaining.
    st.text(stages[st.session_state.lives])












