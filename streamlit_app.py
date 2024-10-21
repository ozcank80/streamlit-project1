import streamlit as st

st.title('Merhaba Streamlit!')

st.write('Bu benim ilk Streamlit uygulamam.')

name = st.text_input('<center>Adınızı girin:</center>')
st.write('Merhaba,', name)
