import json
import random
import streamlit as st

# Carrega o arquivo dictionary.json
with open("dictionary.json") as file:
    d = json.load(file)

# Função para obter uma nova palavra aleatória
def get_random_word():
    pals = list(d.keys())
    return random.choice(pals)

# Variáveis para contar as tentativas
attempts = 0
max_attempts = 5
correct_attempts = 0

def verificar_():
    global word, attempts, correct_attempts  # Utilizado para modificar as variáveis word, attempts e correct_attempts
    hint = entry_hint.lower().strip()
    
    if hint == word:
        st.markdown("<p style='color: green; font-size: 18px;'>Congrats! You win! ┌⁠(⁠★⁠ｏ⁠☆⁠)⁠┘</p>", unsafe_allow_html=True)
        correct_attempts += 1
        # Reiniciar o contador de tentativas ao acertar a palavra
        attempts = 0
    else:
        if attempts >= max_attempts:
            st.markdown(f"<p style='color: red; font-size: 18px;'>You ran out of attempts! The word was: {word}</p>", unsafe_allow_html=True)
            # Reiniciar o contador de tentativas ao acabar as tentativas
            attempts = 0
        else:
            st.markdown("<p style='color: red; font-size: 18px;'>Oh... Try again! (⁠〒⁠﹏⁠〒⁠)</p>", unsafe_allow_html=True)
            st.markdown(f"<p style='font-size: 16px;'>Attempts remaining: {max_attempts - attempts}</p>", unsafe_allow_html=True)
            # Incrementar o contador de tentativas apenas quando não acertar a palavra
            attempts += 1
            
    # Obtém uma nova palavra aleatória
    word = get_random_word()
    st_baralhada = ''.join(random.sample(word, len(word)))
    st.markdown(f"<p style='font-size: 24px;'>{st_baralhada}</p>", unsafe_allow_html=True)

# Interface do Streamlit
word = get_random_word()
st.markdown("<h1 style='font-size: 32px;'>Welcome to the Anagram Game! ✧⁠\⁠(⁠>⁠o⁠<⁠)⁠ﾉ⁠✧</h1>", unsafe_allow_html=True)
st_baralhada = ''.join(random.sample(word, len(word)))
st.markdown(f"<p style='font-size: 24px;'>{st_baralhada}</p>", unsafe_allow_html=True)
st.write(d[word], font_size=20)
st.markdown("<p style='color: orange; font-size: 18px;'>Try to guess the word right〜⁠(⁠꒪⁠꒳⁠꒪⁠)⁠〜</p>", unsafe_allow_html=True)

entry_hint = st.text_input("Enter your guess", value="")

button_show_word = st.button("SHOW CORRECT WORD", on_click=lambda: st.markdown(f"<p style='font-size: 16px;'>Correct word: {word}</p>", unsafe_allow_html=True))
button_verify = st.button("VERIFY", on_click=verificar_)

# Score
st.markdown(f"<p style='font-size: 16px;'>Total attempts: {correct_attempts}</p>", unsafe_allow_html=True)

