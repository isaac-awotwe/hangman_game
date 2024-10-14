
# import packages
import streamlit as st
import random
from hangman_words import word_list
from hangman_art import stages, logo

if "chosen_word" not in st.session_state:
    st.session_state.chosen_word = random.choice(word_list)

if "lives" not in st.session_state:
    st.session_state["lives"] = 6

if "end_of_game" not in st.session_state:
    st.session_state.end_of_game = False

if "display" not in st.session_state:
    st.session_state["display"] = ["_" for letter in st.session_state.chosen_word]











