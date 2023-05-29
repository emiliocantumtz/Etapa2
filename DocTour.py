from __future__ import annnotations
import streamlit as st
from streamlit_option_menu import option_menu
import pandas as pd
import numpy as np

def sidebar():
    # st.title("O")
    st.markdown("<h1 style='text-align: center; color: #7D3C98 ;'> DocTour</h1>", unsafe_allow_html=True)
    
    select = option_menu(
        menu_title = None, #required
        options = ["Operaciones", "Ventas", "Membresías"], #required
        icons = ["gear", "bar-chart", "person-badge"], #optional --- https://icons.getbootstrap.com/
        orientation = "horizontal",
    )
    
    if select == "Home":
        st.title(f"You have selected {select}")
    elif select == "Projects":
        st.title(f"You have selected {select}")
    elif select == "Contact":
        st.title(f"You have selected {select}")
 
def header():
  st.header("Gestión financiera y contable")
  col1, col2 = st.columns(2)
  
  with col1:
    button1 = st.button("Costo de Operación contra Ingresos")
    if button1:
        st.write("Costo de Operación contra Ingresos")
    elif not button1:
        st.write("")
        
  with col2:
    button2 = st.button("Ventas por vendedor contra periodo")
    if button2:
        st.write("Ventas por vendedor contra periodo")
    elif not button1:
        st.write("")
  
def csv():
    csv_url = "https://raw.githubusercontent.com/IngDanielRG/Streamlit_DRG/main/try.csv"
    # Load the .csv file
    df = pd.read_csv(csv_url, encoding='utf-8')
    # Display the table using Streamlit
    st.line_chart(df)
          
sidebar()
header()
csv()
