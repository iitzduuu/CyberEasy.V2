import streamlit as st
import time

st.title('CYBEREASY')  # nome pode ser alterado
st.write('Welcome to cybereasy')

uploader_file = st.file_uploader('Drag a probably malicious file here')  # caixa para selecionar arquivo

if uploader_file is not None:
    if st.button('Analyze file'):
        # Barra de progresso
        progress_bar = st.progress(0)
        for percent_complete in range(101):
            time.sleep(0.05)
            progress_bar.progress(percent_complete)

        # Spinner
        with st.spinner('Loading file...'):
            time.sleep(2)

        st.success('Is not a virus')
#python -m streamlit run frontcyber.py
#  #python -m pip install streamlit