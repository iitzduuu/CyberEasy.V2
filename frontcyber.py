import streamlit as st
import time
st.title('CYBEREASY')#nome pode ser alterado
st.write('Welcome to cybereasy  ')

file = st.file_uploader("Drag a problaly malicious file here") #caixa para selecionar arquivo

progress_bar = st.progress(0) #barra de progresso
for percent_complete in range(101):
    time.sleep(0.05)  
    progress_bar.progress(percent_complete)
with st.spinner('Loading files... '):
    time.sleep(2)
st.success('Completed')

