import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import plotly_express as px
import plotly.graph_objects as go

data = pd.read_csv( 'datos/TitanicPro.csv')
df = pd.DataFrame(data=data)

st.set_page_config(page_title="Titanic People", layout="wide",page_icon="🚢")
st.set_option('deprecation.showPyplotGlobalUse', False)

st.image("img/Titanicpeople.png",width=900)

st.title("Titanic people")

st.subheader('The dataframe :blue[processed] with the _sidebar filter_ 👨‍💻')

# Sidebar con filtros

fil_title = st.sidebar.title("Filters")

filtro_Age = st.sidebar.multiselect("Age Range", df["AgeRange"].unique())

filtro_sex = st.sidebar.multiselect("Sex", df["Sex"].unique())

df1 = df

if filtro_Age:
 df1 = df[(df["AgeRange"].isin(filtro_Age))]
if filtro_sex:
 df1 = df[(df["Sex"].isin(filtro_sex))]
st.dataframe(df1[['Name','Sex','Age','Parch']])


# code3 = '''df = pd.read_csv( 'datos/TitanicPro.csv')

# # Sidebar con filtros

# fil_title = st.sidebar.title("Filters")

# filtro_Age = st.sidebar.multiselect("Age Range", df["AgeRange"].unique())

# filtro_sex = st.sidebar.multiselect("Sex", df["Sex"].unique())

# df1 = df

# if filtro_Age:
#  df1 = df[(df["AgeRange"].isin(filtro_Age))]
# if filtro_sex:
#  df1 = df[(df["Sex"].isin(filtro_sex))]'''

# st.code(code3 , language='python')

st.subheader(':blue[Graphics]👨‍🏫')

col1,col2 = st.columns(2)
with col1:
 age_count = df["AgeRange"].value_counts()
 distage = px.pie(age_count, values="AgeRange", names=age_count.index, title="Age Distribution",)
 plt.title('Age Distribution')
 st.plotly_chart(distage)
 st.write('\nThe youngest person on the boat had:\n{} years old'.format(df['Age'].min()))
 st.write('\nThe oldest person on the boat had:\n{} years old'.format(df['Age'].max()))
 st.write('\nThe median age on the ship was:\n{} years old'.format(df['Age'].median()))
with col2:
 distsex = df["Sex"].value_counts().to_frame()
 distage = px.pie(distsex, values="Sex", names=distsex.index,title="Embarked Distribution")
 plt.title('Sex Distribution')
 st.plotly_chart(distage)
 st.write('\nThe number of women on the ship were:\n{}'.format(df['Sex'][df['Sex']== 'female'].count()))
 st.write('\nThe number of men on the ship were:\n{}'.format(df['Sex'][df['Sex']== 'male'].count()))


scatter = px.scatter(df, "Age", "Sex", title="Age by sex")
plt.title('Age for sex')
st.plotly_chart(scatter)
