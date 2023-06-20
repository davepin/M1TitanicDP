import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import plotly_express as px
import plotly.graph_objects as go

data = pd.read_csv( 'datos/TitanicPro.csv')
df = pd.DataFrame(data=data)

st.set_page_config(page_title="Titanic Economy", layout="wide",page_icon="🚢")
st.set_option('deprecation.showPyplotGlobalUse', False)

st.image("img/Titaniceconomy.png",width=900)

st.title("Titanic economy")

st.subheader('The dataframe :blue[processed] with the _sidebar filter_ 👨‍💻')

# Sidebar con filtros

fil_title = st.sidebar.title("Filters")

filtro_FareRange = st.sidebar.multiselect("Fare", df["FareRange"].unique())

filtro_class = st.sidebar.multiselect("Class", df['Pclass'].unique())

df1 = df

if filtro_FareRange:
 df1 = df[(df["FareRange"].isin(filtro_FareRange))]
if filtro_class:
 df1 = df[(df["Pclass"].isin(filtro_class))]
st.dataframe(df1[['Name','Pclass','Ticket','Fare','FareRange']])

code = '''df = pd.read_csv( 'datos/TitanicPro.csv')

# Sidebar con filtros

fil_title = st.sidebar.title("Filters")

filtro_FareRange = st.sidebar.multiselect("Fare", df["FareRange"].unique())

filtro_class = st.sidebar.multiselect("Class", df['Pclass'].unique())

df1 = df

if filtro_FareRange:
 df1 = df[(df["FareRange"].isin(filtro_FareRange))]
if filtro_class:
 df1 = df[(df["Pclass"].isin(filtro_class))]
st.dataframe(df1[['Name','Pclass','Ticket','Fare','FareRange']])'''

st.code(code , language='python')

st.subheader(':blue[Graphics]👨‍🏫')

col1, col2 = st.columns(2)
with col1:
  distclass = df["FareRange"].value_counts()
  grafica = px.bar(distclass, x=['1-60','60-120','120-180','0-0','180-240','240-300','300-540'], y="FareRange", template="plotly_dark", width=400, height=400, 
                 labels={'x':'Fare',
                     "FareRange": "Number of people for Fare"
                 })
  grafica.update_layout(title='Fare Range Distribution')      #utilizar grafica.update_layout
  st.plotly_chart(grafica)
with col2:
 distclass = df["FareRange"].value_counts()
 st.write(distclass)

col1,col2, col3 = st.columns(3)
with col1:
    scatter = px.scatter(df, "Fare", "Pclass", title="Fare by class")
    plt.title('Age for sex')
    st.plotly_chart(scatter)
with col2:
    st.write('')
with col3:
    distclass = df["FareRange"].value_counts()
    st.write(distclass)
