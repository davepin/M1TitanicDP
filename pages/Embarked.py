import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import plotly_express as px
import plotly.graph_objects as go

data = pd.read_csv( 'datos/TitanicPro.csv')
df = pd.DataFrame(data=data)

st.set_page_config(page_title="Titanic Embarked", layout="wide",page_icon="🚢")
st.set_option('deprecation.showPyplotGlobalUse', False)

st.image("img/Titanicembarked.png",width=900)

st.title("Titanic embarked")

st.subheader('The dataframe :blue[processed] with the _sidebar filter_ 👨‍💻')

# Sidebar con filtros

fil_title = st.sidebar.title("Filters")

filtro_puerto = st.sidebar.multiselect("Embarkation Port", df["Embarked"].unique())

filtro_class = st.sidebar.multiselect("Class", df['Pclass'].unique())

df1 = df

if filtro_puerto:
 df1 = df[(df["Embarked"].isin(filtro_puerto))]
if filtro_class:
 df1 = df[(df["Pclass"].isin(filtro_class))]
st.dataframe(df1[['Pclass','Name','Embarked']])

st.subheader(':blue[Graphics]👨‍🏫')

distEmb = df['Embarked'].value_counts().to_frame()

distage = px.pie(distEmb, values="Embarked", names=distEmb.index, title="Embarked Distribution")
plt.title('Embarked Distribution')
st.plotly_chart(distage)

st.write('\nThe number of people boarded at Southampton:\n{}'.format(df['Embarked'][df['Embarked']== 'Southampton'].count()))
st.write('\nThe number of people boarded at Cherburgo:\n{}'.format(df['Embarked'][df['Embarked']== 'Cherburgo'].count()))
st.write('\nThe number of people boarded at Queenstown:\n{}'.format(df['Embarked'][df['Embarked']== 'Queenstown'].count()))

col1, col2 = st.columns(2)
with col1:
  colores = {'#4945D6':'Third class','#587BED':'First class','#458DD6':'Second class'}
  distclass = df["Pclass"].value_counts().to_frame()
  grafica = px.bar(distclass, x=['Third class','First Class','Second Class'], y="Pclass",color=colores, template="plotly_dark", width=400, height=400, 
                 labels={'x':'Class',
                     "Pclass": "Number of people for Class"
                 })
  grafica.update_layout(title='Class Distribution')      #utilizar grafica.update_layout
  st.plotly_chart(grafica)
with col2:
 distclass = df["Pclass"].value_counts()
 st.dataframe(distclass)
