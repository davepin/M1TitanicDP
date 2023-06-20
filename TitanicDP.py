#Librerias

import os 
import requests
import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import plotly_express as px
import plotly.graph_objects as go


st.set_page_config(page_title="Titanic Main", layout="wide",page_icon="🚢")
st.set_option('deprecation.showPyplotGlobalUse', False)

custom_background = """ <style> body { background-color: #9BBBB5 } </style> """

st.markdown(custom_background , unsafe_allow_html=True)

#Creación de columnas y logotipo

col1,col2,col3 = st.columns(3)
with col1:
 st.title("Titanic")
with col2:
 st.image("img/Titanic.png",width=600)
with col3:
 st.write('')

df0 = pd.read_csv( 'datos/titanic.csv')

st.subheader('I load the :blue[dataframe] in our _streamlit_ ')

st.write(df0)

st.subheader('To do the :blue[preprocessing] of the _dataframe_ we need to know the number of nulls ❌⭕')

code1 = '''# Know number of nulls with
nulos0 = df0.isnull()

grafica = px.imshow(nulos0)
st.plotly_chart(grafica)'''

st.code(code1 , language='python')

col1,col2,col3 = st.columns(3)
with col1:
  nulos0 = df0.isnull()
  grafica = px.imshow(nulos0)
  st.plotly_chart(grafica)
with col2:
 st.write('')
with col3:
 st.write(df0.isnull().sum())


# nuls = df0.isnull().sum()
# # create figure
# fig = plt.figure()
# ax = fig.add_axes([0,0,1,1])
# # set Y axis label
# ax.set_ylabel('count')
# # set orientation for X axis labels
# plt.xticks(rotation='vertical')
# # draw bar chart
# ax.bar(df0.columns, nuls)
# ax.set_xlabel('Columns')
# plt.title('Nulls')
# st.plotly_chart(fig)

#grafica = px.scatter(data_frame=nulos0, x="sepal length (cm)", y="sepal width (cm)", title="Sample Data")
#grafica = px.pie(nulos0, values=nulos0, names=nulos0.index, title="Nulls Distribution")

# del df['Columnas']

code2 = '''# Preprocessed
df = df.drop(['Cabin'], axis=1)
df['Age'].fillna(value=df['Age'].mean(),inplace=True)
df['Age'] = df['Age'].astype(int)
df['Embarked'] = df['Embarked'].fillna(df['Embarked'].mode()[0])
df.replace({'Embarked': {'S':'Southampton','C':'Cherburgo','Q':'Queenstown'}},  inplace=True)

rangos= [-1,10,20,30,40,50,60,70,80]
labels = ['0-10','10-20','20-30','30-40','40-50','50-60','60-70','70-80']
df['AgeRange'] = pd.cut(df['Age'], bins=rangos, labels=labels)

rangos1 = [-1,1,60,120,180,240,300,540]
labels1 = ['0-0','1-60','60-120','120-180','180-240','240-300','300-540']
df['FareRange'] = pd.cut(df['Fare'], bins=rangos1, labels=labels1)'''

st.code(code2 , language='python')

df = pd.read_csv( 'datos/TitanicPro.csv')

#Visual change of the 'survived' data

df.replace({'Survived': {1:'Survived',0:'Not Survived'}},  inplace=True)

st.subheader('The dataframe :blue[processed]👨‍💻')

st.write(df[['PassengerId','Survived','Pclass','Name','Sex','Age','SibSp','Parch','Ticket','Fare','Embarked']])

# if 'Unnamed:0' in df:
#  df = df.drop(colums=['Unnamed:0'])

# fil_title = st.sidebar.title("Filters")

# filtro_puerto = st.sidebar.multiselect("Embarkation Port", df["Embarked"].unique())

# filtro_sex = st.sidebar.multiselect("Sex", df["Sex"].unique())

# filtro_surv = st.sidebar.multiselect("Survived", df["Survived"].unique())

# df1 = df

# if filtro_puerto:
#  df1 = df[(df["Embarked"].isin(filtro_puerto))]
# if filtro_sex:
#  df1 = df[(df["Sex"].isin(filtro_sex))]
# if filtro_surv:
#  df1 = df[(df["Survived"].isin(filtro_surv))]
# st.dataframe(df1[['PassengerId','Survived','Pclass','Name','Sex','Age','SibSp','Parch','Ticket','Fare','Embarked']])


# code3 = '''df = pd.read_csv( 'datos/TitanicPro.csv')

# #Visual change of the 'survived' data

# df.replace({'Survived': {1:'Survived',0:'Not Survived'}},  inplace=True)

# # Sidebar con filtros

# fil_title = st.sidebar.title("Filters")

# filtro_puerto = st.sidebar.multiselect("Embarkation Port", df["Embarked"].unique())

# filtro_sex = st.sidebar.multiselect("Sex", df["Sex"].unique())

# filtro_surv = st.sidebar.multiselect("Survived", df["Survived"].unique())

# df1 = df

# if filtro_puerto:
#  df1 = df[(df["Embarked"].isin(filtro_puerto))]
# if filtro_sex:
#  df1 = df[(df["Sex"].isin(filtro_sex))]
# if filtro_surv:
#  df1 = df[(df["Survived"].isin(filtro_surv))]
# st.dataframe(df1)'''

# st.code(code3 , language='python')

html_code = """<iframe src="https://www.google.com/maps/d/embed?mid=1ghFCpQTutHultL8p3aIZzUKqgyA&ehbc=2E312F" width="640" height="480"></iframe>"""
st.components.v1.html(html_code, height=480)

listings = pd.read_csv( 'datos/listings.csv')
import folium
from folium.plugins import FastMarkerCluster
from streamlit_folium import folium_static

lats2018 = listings['latitude'].tolist()
lons2018 = listings['longitude'].tolist()
locations = list(zip(lats2018, lons2018))

map2 = folium.Map(location=[-34.582760, -58.418240], zoom_start=150)
FastMarkerCluster(data=locations).add_to(map2)
folium_static(map2)
st.write('check this [link del mapa](https://www.google.com/maps/d/embed?mid=1w6eXY1HRbaGV-WGUHgLyvjpP0Uk&hl=es&ehbc=2E312F)')

