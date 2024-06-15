import streamlit as st
from main import main_page
import pymysql
from pymysql.err import OperationalError, MySQLError

# MySQL database connection
def get_connection():
    try:
        connection = pymysql.connect(
            host=st.secrets["db_host"],
            user=st.secrets["db_username"],
            password=st.secrets["db_password"],
            database=st.secrets["db_name"],
            cursorclass=pymysql.cursors.DictCursor
        )
        return connection
    except OperationalError as e:
        st.error(f"Operational error: {e}")
    except MySQLError as e:
        st.error(f"MySQL error: {e}")
    except Exception as e:
        st.error(f"Unexpected error: {e}")

# Initialize session state for login
if 'logged_in' not in st.session_state:
    st.session_state["logged_in"] = False

if 'username' not in st.session_state:
    st.session_state["username"] = None

# Sign up form
def sign_up():
    st.title("Sign Up")

    username = st.text_input("Username")
    password = st.text_input("Password", type="password")

    if st.button("Sign Up"):
        if username and password:
            connection = get_connection()
            if connection:
                try:
                    with connection.cursor() as cursor:
                        # Check if username already exists
                        cursor.execute("SELECT * FROM users WHERE username=%s", (username,))
                        user = cursor.fetchone()
                        if user:
                            st.error("Username already exists.")
                        else:
                            # Insert new user
                            cursor.execute("INSERT INTO users (username, password) VALUES (%s, %s)", (username, password))
                            connection.commit()
                            st.success("User registered successfully!")
                except MySQLError as e:
                    st.error(f"MySQL error: {e}")
                finally:
                    connection.close()
        else:
            st.error("Please provide a username and password.")

# Login form
def login():
    st.title("Login")

    username = st.text_input("Username")
    password = st.text_input("Password", type="password")

    if st.button("Login"):
        if username and password:
            connection = get_connection()
            if connection:
                try:
                    with connection.cursor() as cursor:
                        # Authenticate user
                        cursor.execute("SELECT * FROM users WHERE username=%s AND password=%s", (username, password))
                        user = cursor.fetchone()
                        if user:
                            st.session_state["logged_in"] = True
                            st.session_state["username"] = username
                            st.success("Login successful!")
                            st.experimental_rerun()  # Refresh the page after successful login
                        else:
                            st.error("Incorrect username or password.")
                except MySQLError as e:
                    st.error(f"MySQL error: {e}")
                finally:
                    connection.close()
        else:
            st.error("Please provide a username and password.")

# Logout function
def logout():
    st.session_state["logged_in"] = False
    st.session_state["username"] = None
    st.success("Logged out successfully!")
    st.experimental_rerun()

# Main application
def main():
    if st.session_state['logged_in']:
        st.sidebar.title(f"Welcome, {st.session_state['username']}!")
        if st.sidebar.button("Logout"):
            logout()
        main_page()
    else:
        st.sidebar.title("Navigation")
        option = st.sidebar.selectbox("Choose a page", ["Sign Up", "Login"])

        if option == "Sign Up":
            sign_up()
        elif option == "Login":
            login()

if __name__ == "__main__":
    main()
