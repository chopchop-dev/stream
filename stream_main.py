import streamlit as st
import streamlit.components.v1 as components
import pyvista
import pandas as pd
import numpy as np
st.title('Uber pickups in NYC')
uploaded_file = st.file_uploader("Choose a Mesh file")
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


