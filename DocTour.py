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
        options = ["Resumen mensual", "Detalle de ingresos mensuales", "Detalle de gastos mensuales"], #required
        icons = ["gear", "bar-chart", "person-badge"], #optional --- https://icons.getbootstrap.com/
        orientation = "horizontal",
    )
    
    if select == "Home":
        st.title(f"You have selected {select}")
    elif select == "Projects":
        st.title(f"You have selected {select}")
    elif select == "Contact":
        st.title(f"You have selected {select}") 

def buttons():
  st.header("DocTour")
  col1, col2, col3 = st.columns(3)
        
  with col1:
    col1.metric("Ingresos por membresía Mayo 2023", "120K", "20%")
        
  with col2:
    col2.metric("Costos de operación Mayo 2023", "100K", "-4.2%")

  with col3:
    col3.metric("Utilidad/Pérdida Mayo 2023", "20K", "20%")
  
def chart():
    col1, col2, col3 = st.columns(3)
    
    with col1:
            source = pd.DataFrame({
                "Ingresos":[ 15, 14, 9, 24, 11, 15, 15, 18, 14, 15, 13, 17],
                "Mes":["ENE", "FEB", "MAR", "ABR", "MAY", "JUN", "JUL", "AGO", "SEPT", "OCT", "NOV", "DIC"]
            })
                
            line_chart = alt.Chart(source).mark_line().encode(
                y = "Ingresos",
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
    with col3:
            source = pd.DataFrame({
                "Membresias":[ 180, 153, 197, 76],
                "Año":["2020", "2021", "2022", "2023"]
            })
                
            bar_chart = alt.Chart(source).mark_bar().encode(
                y = "Membresias",
                x = "Año",
            )
            st.altair_chart(bar_chart, use_container_width=True)
          
sidebar()
buttons()
chart()
