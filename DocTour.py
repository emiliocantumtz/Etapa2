import streamlit as st
import pandas as pd
import numpy as np

def sidebar():
    # st.title("O")
    st.markdown("<h1 style='text-align: center; color: #7D3C98 ;'> DocTour</h1>", unsafe_allow_html=True)
    with st.sidebar:
        st.header("Encabezado")
        st.subheader("Subencabezado")
        text = st.text_area("Filtrar ")

        button0 = st.button("Golf")
        if button0:
            st.write(text)
 
def header():
  st.header("Variables Críticas")
  col1, col2 = st.columns(2)
  
  with col1:
    button1 = st.button("Costos de Operación")
    if button1:
        st.write("Gráfica")
    elif not button1:
        st.write("Golf")
        
  with col2:
    button2 = st.button("Márgenes/Punto de equilibrio")
    if button2:
        st.write("No")
    elif not button1:
        st.write("Golf'nt")
          
sidebar()
header()
