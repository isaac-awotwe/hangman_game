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