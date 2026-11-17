import streamlit as st
if "a" not in st.session_state:
    st.session_state.a = 0
if "b" not in st.session_state:
        st.session_state.b = 0
if st.button("Get money!"):
    if st.session_state.b == 0:
        st.session_state.a += 1
    else:
        st.session_state.a += 2
st.write("You have ",st.session_state.a,"dollars")

if st.button("Upgrade your clicker  \n50 dollars"):
    if st.session_state.a > 50:
        if st.session_state.b == 0:
            st.session_state.b = 1
            st.session_state.a -= 50
            st.balloons()
