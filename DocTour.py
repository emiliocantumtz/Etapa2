import streamlit as st
import pandas as pd
import numpy as np

def sidebar():
    # st.title("O")
    st.markdown("<h1 style='text-align: center; color: #7D3C98 ;'> DocTour</h1>", unsafe_allow_html=True)
 
def header():
  st.header("Gestión financiera y contable")
  col1, col2 = st.columns(2)
  
  with col1:
    button1 = st.button("Costo de Operación por Ingresos")
    if button1:
        st.write("Costo de Operación por Ingresos")
    elif not button1:
        st.write("")
        
  with col2:
    button2 = st.button("Punto de equilibrio")
    if button2:
        st.write("Punto de equilibrio")
    elif not button1:
        st.write("")
  
def barra():
    chart_data = pd.DataFrame(
        np.random.randn(20, 3),
        columns=['Costo de operacion', 'Ingresos por membresias activas', 'Ingresos por pruebas de covid'])
     
    st.line_chart(chart_data)
          
sidebar()
header()
barra()
