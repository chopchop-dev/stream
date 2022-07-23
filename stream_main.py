import streamlit as st
import streamlit.components.v1 as components
import pyvista
import shutil

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
  
