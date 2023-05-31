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

def buttons():
  st.header("Gestión financiera y contable")
  col1, col2, col3 = st.columns(3)
        
  with col1:
    col1.metric("Ventas membresía básica Mayo 2023", "5", "20%")
        
  with col2:
    col2.metric("Ventas membresía black Mayo 2023", "4", "-3%")

  with col3:
    col3.metric("Ventas membresía platino Mayo 2023", "2", "5%")
  
def chart():
    col1, col2, col3 = st.columns(3)
            
    with col1:
            source = pd.DataFrame({
                "Membresias":[ 15, 14, 9, 24, 11, 15, 15, 18, 14, 15, 13, 17],
                "Mes":["ENE", "FEB", "MAR", "ABR", "MAY", "JUN", "JUL", "AGO", "SEPT", "OCT", "NOV", "DIC"]
            })
                
            bar_chart = alt.Chart(source).mark_bar().encode(
                y = "Membresias",
                x = "Mes",
            )
            st.altair_chart(bar_chart, use_container_width=True)
    with col2:
            source = pd.DataFrame({
                "Membresias":[ 180, 153, 197, 76],
                "Año":["2020", "2021", "2022", "2023"]
            })
                
            bar_chart = alt.Chart(source).mark_bar().encode(
                y = "Membresias",
                x = "Año",
            )
            st.altair_chart(bar_chart, use_container_width=True)
    with col3:
             source = pd.DataFrame({
                "Cierres":[ 5, 10, 15, 20, 25, 30, 35, 40, 45, 50],
                "Leads":["10", "20", "30", "40", "50", "60", "70", "80", "90", "100"]
            })
                
            line_chart = alt.Chart(source).mark_line().encode(
                y = "Cierres",
                x = "Leads",
            )
            st.altair_chart(line_chart, use_container_width=True)
          
sidebar()
buttons()
chart()
