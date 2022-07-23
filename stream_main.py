import streamlit as st
import streamlit.components.v1 as components
import pyvista
import pandas as pd
import numpy as np
st.title('Uber pickups in NYC')

def save_uploadedfile(uploadedfile):
     with open(os.path.join("Data”, uploadedfile.name), “wb”) as f:
     f.write(uploadedfile.getbuffer())
     return st.success(“Saved File:{} to Data”.format(uploadedfile.name))

st.title(” PDF File upload”)
st.text(” A simple way to upload files directly into a directory”)
uploadedfiles = st.file_uploader(“Upload PDF”, type=[‘pdf’], accept_multiple_files=True)
for file in uploadedfiles:
     if uploadedfiles is not None:
         save_uploadedfile(file)

uploaded_file = st.file_uploader("Upload Mesh, vtk only",type=["vtk"])
if uploaded_file is not None:
     # To read file as bytes:
     bytes_data = uploaded_file.getvalue()
     #st.write(bytes_data)
     mesh = pyvista.read('new_mesh.vtk')
     clipped = mesh.clip('y', invert=False)
     pl = pyvista.Plotter(shape=(1,2))
     _ = pl.add_mesh(clipped, label='Clipped',show_edges=True)
     pl.subplot(0,1)
     _ = pl.add_mesh(mesh, show_edges=True)
     pl.export_html('pyvista.html')  # doctest:+SKIP
     option=st.sidebar.radio('Pyvista',('On','Off'))
     if option=='On':
       HtmlFile = open("pyvista.html", 'r', encoding='utf-8')
       source_code = HtmlFile.read() 
       components.html(source_code, height = 500,width=500)


