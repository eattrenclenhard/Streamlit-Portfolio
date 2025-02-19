import streamlit as st

st.set_page_config(layout='wide')

col1, col2 = st.columns(2)

with col1:
    st.image("images/stig.png")

with col2:
    st.title("The Stig")
    content = """
        Some say he’s wanted by the CIA
        and that he sleeps upside down like a Bat.
        All we know is he’s called the Stig.
        """
    st.info(content)
