
# import packages
import streamlit as st
import random
from hangman_words import word_list
from hangman_art import stages, logo

word_lens = [len(word) for word in word_list]
max_word_len =  max(word_lens)
keys = [*range(max_word_len*3)]

chosen_word = random.choice(word_list)
display = []
for letter in chosen_word:
    display.append("_")
word_length = len(chosen_word)
end_of_game = False

if 'stage' not in st.session_state:
    st.session_state.stage = 0

def set_state(i):
    st.session_state.stage = i

if st.session_state.stage == 0:
    st.write("Click the button below to begin")
    st.button('Begin', on_click=set_state, args=[1])

if st.session_state.stage >= 1:
    #st.write("## Welcome to the Hangman Game.")
    st.text(logo)
    st.markdown(f"The chosen word is '{chosen_word}'")

    while not end_of_game:
        guess = st.text_input("Guess a letter: ", on_change = set_state, args = [2], key = random.sample(keys, 1))

        for i in range(word_length):
            if chosen_word[i] == guess:
                display[i] = guess
        
        st.text(''.join(display))

        if "_" not in display:
            end_of_game = True
            st.write("You win!")










