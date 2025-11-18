import streamlit as st

st.set_page_config(page_title='Pokedex', layout='wide')

if "pagina" not in st.session_state:
    st.session_state.pagina = "perfil"

pagina = st.sidebar.selectbox(
    'Escolha uma página:',
    ['perfil', 'cadastrar','deletar', 'pokedex'],
    index=['perfil', 'cadastrar','deletar', 'pokedex'].index(st.session_state.pagina)
)

st.session_state.pagina = pagina
if st.session_state.pagina == "perfil":
    import page.perfil as perfil
    perfil.app()

elif st.session_state.pagina == "cadastrar":
    import page.cadastrar as cadastrar
    cadastrar.app()
    
elif st.session_state.pagina == "deletar":
    import page.deletar as deletar
    deletar.app()

elif st.session_state.pagina == "pokedex":
    import page.pokedex as pokedex
    pokedex.app()
