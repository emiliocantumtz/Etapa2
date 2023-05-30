import streamlit as st
from streamlit_option_menu import option_menu
import pandas as pd
import numpy as np
import altair as alt

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
  
def chart():
    col1, col2 = st.columns(2)
    
    with col1:
            source = pd.DataFrame({
                "Dinero":[ 15, 14, 9, 24, 11, 15, 15, 18, 14, 15, 13, 17] "Operacion":[ 25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25],
                "Mes":["ENE", "FEB", "MAR", "ABR", "MAY", "JUN", "JUL", "AGO", "SEPT", "OCT", "NOV", "DIC"]
            })
                
            line_chart = alt.Chart(source).mark_line().encode(
                y = "Dinero" "Operacion",
                x = "Mes",
            )
            st.altair_chart(line_chart, use_container_width=True)
            
    with col2:
            source = pd.DataFrame({
                "Membresias":[ 15, 14, 9, 24, 11, 15, 15, 18, 14, 15, 13, 17],
                "Mes":["ENE", "FEB", "MAR", "ABR", "MAY", "JUN", "JUL", "AGO", "SEPT", "OCT", "NOV", "DIC"]
            })
                
            bar_chart = alt.Chart(source).mark_bar().encode(
                y = "Membresias",
                x = "Mes",
            )
            st.altair_chart(bar_chart, use_container_width=True)
          
sidebar()
header()
chart()
