import streamlit as st
from module.send_email import send_email

st.header("Contact Me")

with st.form(key='email_form'):
    visitor_email = st.text_input('Your email address')
    raw_message = st.text_area('Your message')
    message_body = f"""\
Subject: Streamlit Portfolio: New email from {visitor_email}
    
{raw_message}
From: {visitor_email}
"""
    button = st.form_submit_button('Submit')
    if button:
        try:
            send_email(message_body)


            @st.dialog('✅Email successfully sent!')
            def instruction_modal():
                st.write('Thank you for contacting me! I will get back to you soon.')


            instruction_modal()

        except:
            print('There was an error sending the email.')
