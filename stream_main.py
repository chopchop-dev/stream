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

authenticator = stauth.Authenticate(names, usernames, hashed_passwords,
    "sales_dashboard", "abcdef", cookie_expiry_days=30)

name, authentication_status, username = authenticator.login("Login", "main")

if authentication_status == False:
    st.error("Username/password is incorrect")

if authentication_status == None:
    st.warning("Please enter your username and password")


if authentication_status:
    # ---- READ EXCEL ----
   @st.cache 
   file = st.file_uploader("Choose a file, VTK only")    
   if file is not None:
       # save the uploaded mesh file to disk
       with open("mesh.vtk", "wb") as buffer:
           shutil.copyfileobj(file, buffer)
        
       mesh = pyvista.read('mesh.vtk')
       clipped = mesh.clip('y', invert=False)
       pl = pyvista.Plotter(shape=(1,2))
       _ = pl.add_mesh(mesh, style='wireframe', color='blue', label='Input')
       _ = pl.add_mesh(clipped, label='Clipped',show_edges=True)
       pl.subplot(0,1)
       _ = pl.add_mesh(mesh, show_edges=True)
       pl.export_html('pyvista.html')  # doctest:+SKIP
       option=st.sidebar.radio('Show Meshes',('On','Off'))
       if option=='On':
           HtmlFile = open("pyvista.html", 'r', encoding='utf-8')
           source_code = HtmlFile.read() 
           components.html(source_code, height = 500,width=500)
  
