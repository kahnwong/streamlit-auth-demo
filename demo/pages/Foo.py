import streamlit as st

if not st.session_state["authentication_status"]:
    st.warning("Please login on the welcome page")
    st.stop()
else:
    st.title("Foo")
