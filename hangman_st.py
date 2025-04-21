import streamlit as st
import random
from hangman_art import stages, logo
from hangman_words import word_list

# Initialize game state on first load
if 'chosen_word' not in st.session_state:
    st.session_state.chosen_word = random.choice(word_list)
    st.session_state.display = ['_' for _ in st.session_state.chosen_word]
    st.session_state.lives = 6
    st.session_state.end_of_game = False
    st.session_state.guessed_letters = []

st.image("https://raw.githubusercontent.com/streamlit/streamlit/develop/examples/data/hangman-logo.png", width=200)
st.title("🎯 Hangman Game")

# Show logo (you can also display it as text if needed)
st.markdown(f"<pre>{logo}</pre>", unsafe_allow_html=True)

# Display the word with blanks
st.subheader("Word to Guess:")
st.write(" ".join(st.session_state.display))

# Display ASCII art of the hangman
st.text(stages[st.session_state.lives])

# Input guess
if not st.session_state.end_of_game:
    guess = st.text_input("Guess a letter", max_chars=1).lower()

    if guess:
        if guess in st.session_state.display or guess in st.session_state.guessed_letters:
            st.warning(f"You already guessed '{guess}'. Try another letter.")
        else:
            st.session_state.guessed_letters.append(guess)

            if guess in st.session_state.chosen_word:
                for i, letter in enumerate(st.session_state.chosen_word):
                    if letter == guess:
                        st.session_state.display[i] = guess
                st.success(f"Good guess: '{guess}' is in the word!")
            else:
                st.session_state.lives -= 1
                st.error(f"Wrong guess: '{guess}' is not in the word.")

        if "_" not in st.session_state.display:
            st.session_state.end_of_game = True
            st.balloons()
            st.success("🎉 Congratulations! You won!")

        if st.session_state.lives == 0:
            st.session_state.end_of_game = True
            st.error(f"💀 Game Over! The word was: {st.session_state.chosen_word}")

# Show lives
st.markdown(f"**Lives Remaining:** {st.session_state.lives}/6")

# Reset button
if st.button("🔄 Play Again"):
    st.session_state.chosen_word = random.choice(word_list)
    st.session_state.display = ['_' for _ in st.session_state.chosen_word]
    st.session_state.lives = 6
    st.session_state.end_of_game = False
    st.session_state.guessed_letters = []
