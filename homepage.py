import streamlit as st

html_string = "<body><h1>Write, edit and run HTML, CSS and JavaScript code online.</h1><p>Our HTML editor updates the webview automatically in real-time as you write code.</p></body>"

st.markdown(html_string, unsafe_allow_html = True);