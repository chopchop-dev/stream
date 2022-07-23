import streamlit as st
import streamlit.components.v1 as components
import pyvista
import shutil

file = st.file_uploader("Choose a file")    
if file is not None:
    # save the uploaded file to disk
    with open("new_mesh.vtk", "wb") as buffer:
        shutil.copyfileobj(file, buffer)
    mesh = pyvista.read('new_mesh.vtk')
    
