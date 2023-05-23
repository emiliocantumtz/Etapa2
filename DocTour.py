import streamlit as st
import pandas as pd
import numpy as np

def sidebar():
    # st.title("O")
    st.markdown("<h1 style='text-align: center; color: #7D3C98 ;'> DocTour</h1>", unsafe_allow_html=True)
 
def header():
  st.header("Variables Críticas")
  col1, col2, col3, col4 = st.columns(4)
  
  with col1:
    button1 = st.button("Costos de Operación")
    if button1:
        st.write("Gráfica")
    elif not button1:
        st.write("")
        
  with col2:
    button2 = st.button("Márgenes/Punto de equilibrio")
    if button2:
        st.write("Gráfica")
    elif not button1:
        st.write("")
   
  with col3:
    button3 = st.button("Ventas/Ingresos")
    if button3:
        st.write("Gráfica")
    elif not button1:
        st.write("")
        
  with col4:
    button4 = st.button("Márgenes/Punto de equilibrio")
    if button3:
        st.write("Gráfica")
    elif not button1:
        st.write("")
  
def barra():
    chart_data = pd.DataFrame(
        np.random.randn(20, 3),
        columns=['a', 'b', 'c'])

    st.bar_chart(chart_data)
          
sidebar()
header()
barra()
