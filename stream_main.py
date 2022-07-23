import streamlit as st

file = st.file_uploader("Choose a file")    
if file is not None:
    # save the uploaded file to disk
    with open("new_mesh.vtk", "wb") as buffer:
        shutil.copyfileobj(file, buffer)
    tlog2 = log_analyzer.TrajectoryLog("new_mesh.vtk")
    
