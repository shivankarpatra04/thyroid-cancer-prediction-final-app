# app.py

import streamlit as st
from database import create_table, add_user, login_user
from main import main_page

# Create the users table if it doesn't exist
create_table()

def main():
    st.title("Thyroid Cancer Prediction Web App")

    # Initialize session state for login status and username
    if 'logged_in' not in st.session_state:
        st.session_state['logged_in'] = False
        st.session_state['username'] = ''

    def logout():
        st.session_state['logged_in'] = False
        st.session_state['username'] = ''
        st.experimental_rerun()

    def login(username, password):
        user = login_user(username, password)
        if user:
            st.success(f"Welcome {username}")
            st.session_state['logged_in'] = True
            st.session_state['username'] = username
            st.experimental_rerun()
        else:
            st.error("Invalid Username or Password")

    if st.session_state['logged_in']:
        st.sidebar.write(f"Logged in as {st.session_state['username']}")
        if st.sidebar.button("Logout"):
            logout()
        main_page()
    else:
        menu = ["Login", "Sign Up"]
        choice = st.sidebar.selectbox("Menu", menu)

        if choice == "Login":
            st.subheader("Login Section")

            username = st.text_input("Username")
            password = st.text_input("Password", type='password')

            if st.button("Login"):
                login(username, password)

        elif choice == "Sign Up":
            st.subheader("Create New Account")

            new_user = st.text_input("Username")
            new_password = st.text_input("Password", type='password')

            if st.button("Sign Up"):
                add_user(new_user, new_password)
                st.success("You have successfully created an account")
                st.info("Go to Login Menu to login")

if __name__ == '__main__':
    main()
