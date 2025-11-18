import streamlit as st
import functions

def app():
    st.title("Cadastro de Pokémon")
    with st.form('button'):
        pokemon = st.text_input("Digite o nome do Pokémon que vai ser cadastrado").lower()
        id = st.text_input("Digite o id do treinador que o cadastrou")
        imagem = st.file_uploader("Envie uma imagem do Pokémon", type=["png", "jpg", "jpeg"])
        button = st.form_submit_button('Cadastrar')

    if button:
        tem = functions.verif_trein(id)
        if tem == False:
            st.warning("O treinador não está cadastrado!")
        else:
            functions.adic_pokemon(pokemon, id, imagem)
            st.success("Pokémon cadastrado")
            st.balloons()
            
    
    st.header('Pokémons cadastrados:')
    functions.show_pokemons()