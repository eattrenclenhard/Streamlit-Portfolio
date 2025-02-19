import streamlit as st
import pandas

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

st.write("We're no strangers to love. You know the rules and so do I.")
col3, col4 = st.columns(2)
df = pandas.read_csv("data.csv", sep=";")

with col3:
    for index, row in df.iterrows():
        if index % 2 == 0:
            st.header(row["title"])
            st.write(row["description"])
            st.image(f"images/{row['image']}")
            st.write(f"[Source Code]({row['url']})")

with col4:
    for index, row in df.iterrows():
        if index % 2 != 0:
            st.header(row["title"])
            st.write(row["description"])
            st.image(f"images/{row['image']}")
            st.write(f"[Source Code]({row['url']})")
