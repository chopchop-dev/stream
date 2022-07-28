import streamlit as st
import streamlit.components.v1 as components
import pyvista
import shutil
import pickle
from pathlib import Path
import yaml
import streamlit_authenticator as stauth

with open('config.yaml') as file:
    config = yaml.safe_load(file)

authenticator = Authenticate(
    config['credentials'],
    config['cookie']['name'],
    config['cookie']['key'],
    config['cookie']['expiry_days'],
    config['preauthorized']
)

name, authentication_status, username = authenticator.login('Login', 'main')
