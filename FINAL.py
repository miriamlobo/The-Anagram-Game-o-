import json
import random
import streamlit as st
from colored import fg, attr

def word_prompt(data, length):
    all_words = list(data.keys())
    while True:
        word = random.choice(all_words)
        if len(word) < length and len(word) > 2:
            return word

def shuffle_word(word):
    array = list(word)
    shuffled = word
    while True:
        random.shuffle(array)
        shuffled = ''.join(array)
        if shuffled != word:
            return shuffled

if __name__ == "__main__":
    filename = 'dictionary.json'
    file = open(filename)
    data = json.load(file)
    
    st.markdown("<h1 style='font-size: 32px;'>Welcome to the Anagram Game! ✧⁠\⁠(⁠>⁠o⁠<⁠)⁠ﾉ⁠✧</h1>", unsafe_allow_html=True)
    score = 0
    
    while True:
        word = word_prompt(data, 5)
        question = shuffle_word(word)
        meaning = data[word]
        
        question = question.lower()
        word = word.lower()
        
        st.markdown(f"<p style='font-size: 24px;'>{question}</p>", unsafe_allow_html=True)
        st.write(meaning)

        st.markdown("<p style='color: orange; font-size: 18px;'>Try to guess the word right〜⁠(⁠꒪⁠꒳⁠꒪⁠)⁠〜</p>", unsafe_allow_html=True)
        st.markdown("<p style='color: red; font-size: 16px;'>Please write in the system shell!!</p>", unsafe_allow_html=True)
        
        attempts = 5
        
        while attempts > 0:
            st.write("\nAttempts Left:", attempts)
            #guess = input('Make a guess (⁠ﾉﾟ⁠0ﾟ⁠)⁠ﾉ⁠→ ').lower()
            guess = st.text_input('Make a guess (⁠ﾉﾟ⁠0ﾟ⁠)⁠ﾉ⁠→ ').lower()
            if guess == word:
                score += 1
                st.markdown("<p style='color: green; font-size: 22px;'>Congrats! You guessed it! ┌⁠(⁠★⁠ｏ⁠☆⁠)⁠┘</p>", unsafe_allow_html=True)
                break
            attempts -= 1
            if attempts == 0:
                st.write("\nAnd the correct answer wassss (⁠☞՞⁠ਊ⁠ ⁠՞⁠)⁠☞", "<span style='color: green;'>", word, "</span>", unsafe_allow_html=True)

        
        st.write("Score:", score)
        
        choice = input("\nContinue? (Y/N): ")
        st.write('-' * 50)
        if choice.lower() == 'n':
            st.write("\nOh okay...Thank you for playing anyway!✧⁠◝⁠(⁠⁰⁠▿⁠⁰⁠)⁠◜⁠✧")
            break


