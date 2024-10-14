import streamlit as st
import random
from hangman_words import word_list
from hangman_art import stages, logo

chosen_word = random.choice(word_list)
lives = 6
display = ["_" for letter in chosen_word]
end_of_game = False

if 'stage' not in st.session_state:
    st.session_state.stage = 0

def set_state(i):
    st.session_state.stage = i

if st.session_state.stage == 0:
    st.write("Click the button below to begin")
    st.button('Begin', on_click=set_state, args=[1])
    
if st.session_state.stage >= 1:
    st.write("## Welcome to the Hangman Game.")
    st.text(logo)
    st.markdown(f"The chosen word is '{chosen_word}'")

# sess_state_arg = 0
# key = 0

# while not end_of_game:
#     sess_state_arg+=1
#     key+=1
#     if st.session_state.stage >= sess_state_arg:
#         guess = st.text_input("Guess a letter: ", on_change = set_state, args = [sess_state_arg+1], key=key).lower()

#         if guess in display:
#             st.markdown(f"You've already correctly guessed '{guess}'. Guess a different letter.")
        
#         for i in range(len(chosen_word)):
#             if chosen_word[i] == guess:
#                 display[i] = guess
        
#         if guess not in chosen_word:
#             #If the letter is not in the chosen_word, print out the letter and let them know it's not in the word.
#             st.markdown(f"You guessed '{guess}', that's not in the word. You lose a life.")
#             lives-=1
        
#         if lives == 0:
#             end_of_game = True
#             st.write("Game over! You lost!")
        
#         #Join all the elements in the list and turn it into a String.
#         st.markdown(f"{' '.join(display)}")

#         if "_" not in display:
#             end_of_game = True
#             st.write("You win!")
        
#         st.text(stages[lives])