import streamlit as st

def carregar_chain()
    return carregar_normal_chain()

def limpar_input_field():
    st.session_state.usuario_pergunta = st.session_state.usuario_input
    st.session_state.usuario_input = ''

def set_enviar_input():
    st.session_state.enviar_input =True
    limpar_input_field()

def main():
    st.title('Multimodal Local IA')
    chat_container = st.container()

    if 'enviar_input' not in st.session_state:
        st.session_state.enviar_input = False
        st.session_state.usario_pergunta = ''

    usuario_input = st.text_input('Digite sua mensagem aqui', key='usuario_input', on_change=set_enviar_input)
    enviar_button =  st.button('Enviar', key='enviar_button')

    if enviar_button or st.session_state.enviar_input:
        if st.session_state.usuario_pergunta != '':       
            llm_resposta='Esse é um modelo LLM'

            with chat_container:
                st.chat_message('user').write(st.session_state.usuario_pergunta)
                st.chat_message('ai').write('Aqui esta a resposta')

if __name__ == '__main__':
    main()
