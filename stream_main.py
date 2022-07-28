import streamlit as st
import streamlit.components.v1 as components
import pyvista
import shutil
import pickle
from pathlib import Path
import yaml
import streamlit_authenticator as stauth


# --- USER AUTHENTICATION ---
names = ["Peter Parker", "Rebecca Miller"]
usernames = ["pparker", "rmiller"]

# load hashed passwords
file_path = Path(__file__).parent / "hashed_pw.pkl"
with file_path.open("rb") as file:
    hashed_passwords = pickle.load(file)

authenticator = stauth.Authenticate(names, usernames, hashed_passwords, "what", "wfwaefw", cookie_expiry_days=30)

name, authentication_status, username = authenticator.login("Login", "main")
