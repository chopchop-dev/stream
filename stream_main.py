import streamlit as st
import streamlit.components.v1 as components
import pyvista
import shutil
import pickle
from pathlib import Path
import streamlit_authenticator as stauth


st.set_page_config(page_title="Sales Dashboard", page_icon=":bar_chart:", layout="wide")

# --- USER AUTHENTICATION ---
names = ["Peter Parker", "Rebecca Miller"]
usernames = ["pparker", "rmiller"]

# load hashed passwords
file_path = Path(__file__).parent / "hashed_pw.pkl"
with file_path.open("rb") as file:
    hashed_passwords = pickle.load(file)

authenticator = stauth.Authenticate(names, usernames, hashed_passwords)

name, authentication_status, username = authenticator.login("Login", "main")

if authentication_status == False:
    st.error("Username/password is incorrect")

if authentication_status == None:
    st.warning("Please enter your username and password")


if authentication_status:
    st.warning('pass')
