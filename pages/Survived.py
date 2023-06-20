import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import plotly_express as px
import plotly.graph_objects as go

data = pd.read_csv( 'datos/TitanicPro.csv')
df = pd.DataFrame(data=data)

df.replace({'Survived': {1:'Survived',0:'Not Survived'}},  inplace=True)

st.set_page_config(page_title="Titanic Survived", layout="wide",page_icon="🚢")
st.set_option('deprecation.showPyplotGlobalUse', False)

st.image("img/Titanicembarked.png",width=900)

st.title("Titanic survivors")

st.subheader('The dataframe :blue[processed] with the _sidebar filter_ 👨‍💻')

# Sidebar con filtros

fil_title = st.sidebar.title("Filters")


filtro_puerto = st.sidebar.multiselect("Embarkation Port", df["Embarked"].unique())

filtro_FareRange = st.sidebar.multiselect("Fare", df["FareRange"].unique())

filtro_class = st.sidebar.multiselect("Class", df['Pclass'].unique())

filtro_Age = st.sidebar.multiselect("Age Range", df["AgeRange"].unique())

filtro_sex = st.sidebar.multiselect("Sex", df["Sex"].unique())

filtro_surv = st.sidebar.multiselect("Survived", df["Survived"].unique())

df1 = df

if filtro_puerto:
 df1 = df[(df["Embarked"].isin(filtro_puerto))]
if filtro_FareRange:
 df1 = df[(df["FareRange"].isin(filtro_FareRange))]
if filtro_class:
 df1 = df[(df["Pclass"].isin(filtro_class))]
if filtro_Age:
 df1 = df[(df["AgeRange"].isin(filtro_Age))]
if filtro_sex:
 df1 = df[(df["Sex"].isin(filtro_sex))]
if filtro_surv:
 df1 = df[(df["Survived"].isin(filtro_surv))]

min_value= float(df["Fare"].min())
max_value= float(df["Fare"].max())
initial_value= (float(df["Fare"].min()), float(df["Fare"].max()))
inicio, fin = st.sidebar.slider("Select Fare Range", min_value=min_value, max_value=max_value , value=initial_value, step=0.1)
filtro_fare = (df['Fare'] >= inicio) & (df['Fare'] <= fin)
df1 = df.loc[filtro_fare]

min_value= float(df["Pclass"].min())
max_value= float(df["Pclass"].max())
initial_value= (float(df["Pclass"].min()), float(df["Pclass"].max()))
inicio, fin = st.sidebar.slider("Select Pclass Range", min_value=min_value, max_value=max_value , value=initial_value, step=0.1)
filtro_Pclass = (df['Pclass'] >= inicio) & (df['Pclass'] <= fin)
df1 = df.loc[filtro_Pclass]

st.dataframe(df1[['Name','Survived','Pclass','Sex','Age','Embarked','AgeRange','FareRange','Fare']])

data = pd.read_csv( 'datos/TitanicPro.csv')
df = pd.DataFrame(data=data)

st.subheader(':blue[Graphics]👨‍🏫')

col1,col2 = st.columns(2)
with col1:
 distSurvs = df[(df['Survived'] == 1)][['AgeRange']].value_counts()
 grafica = px.bar(distSurvs, x=distSurvs, y=['0-10','10-20','20-30','30-40','40-50','50-60','60-70','70-80'], template="plotly_dark", width=400, height=400, 
                 labels={"x": "Number of people Survived by age range", 'y':'Age Range'})
 grafica.update_layout(title='Survivors by age')      #utilizar grafica.update_layout
 st.plotly_chart(grafica)
 
 st.write('\nThe youngest person to die:\n{} years old'.format(df['Age'][df['Survived']== 0].min()))
 st.write('\nThe oldest person to die:\n{} years old'.format(df['Age'][df['Survived']== 0].max()))
 st.write('\nthe median age of death on the ship was:\n{} years old'.format(df['Age'][df['Survived']== 0].median()))

with col2:
 colores = ['Female','Male']
 distSurv = df[(df['Survived'] == 1)][['Sex']].value_counts()
 grafica = px.bar(distSurv, x=['female','male'], y=distSurv,color=colores, template="plotly_dark", width=400, height=400, 
                 labels={"x":"Sex","y": "Number of people Survived by sex"})
 grafica.update_layout(title='Survivors by sex')      #utilizar grafica.update_layout
 st.plotly_chart(grafica)
 st.write('\nThe number of men survived was:\n{}'.format(df[(df['Sex']== 'male')&(df['Survived'] == 1)]['Survived'].sum()))
 st.write('\nThe number of women survived was:\n{}'.format(df[(df['Sex']== 'female')&(df['Survived'] == 1)]['Survived'].sum()))


col1,col2 = st.columns(2)
with col1:
 distSurvs = df[(df['Survived'] == 1)][['Pclass']].value_counts()
 grafica = px.bar(distSurvs, x=['First class','Second Class','Third Class'], y=distSurvs, template="plotly_dark", width=400, height=400,labels={"x": "Class", 'y':'Number of people Survived by Class'})
 grafica.update_layout(title='Survivors by class')      #utilizar grafica.update_layout
 st.plotly_chart(grafica)

 st.write('\nThe number of surviving people of First Class:\n{}'.format(df[(df['Pclass']== 1)&(df['Survived'] == 1)]['Survived'].sum()))
 st.write('\nThe number of surviving people of Second Class:\n{}'.format(df[(df['Pclass']== 2)&(df['Survived'] == 1)]['Survived'].sum()))
 st.write('\nThe number of surviving people of Third Class:\n{}'.format(df[(df['Pclass']== 3)&(df['Survived'] == 1)]['Survived'].sum()))

with col2:
 distSurv = df[(df['Survived'] == 1)][['FareRange']].value_counts()
 grafica = px.bar(distSurv, x=['1-60','60-120','240-300','120-180','0-0','300-540','180-240'], y=distSurv, template="plotly_dark", width=400, height=400, 
                 labels={"x":"Fare","y": "Number of people Survived by fare"})
 grafica.update_layout(title='Survivors by fare')      #utilizar grafica.update_layout
 st.plotly_chart(grafica)
 st.write('\nThe maximum fare for survived was:\n{}'.format(df['Fare'][df['Survived'] == 1].max()))
 st.write('\nThe minimum fare for survived was:\n{}'.format(df['Fare'][df['Survived'] == 1].min()))

col1,col2 = st.columns(2)
with col1:
 distSurv = df[(df['Survived'] == 1)][['Embarked']].value_counts()
 grafica = px.bar(distSurv, x=['Southampton','Cherburgo','Queenstown'], y=distSurv, template="plotly_dark", width=400, height=400, 
                 labels={'x':'City of embarked',
                     "y": "Number of people Survived by boarded city"
                 })
 grafica.update_layout(title='Survivors by city of embarked')      #utilizar grafica.update_layout
 st.plotly_chart(grafica)
 st.write('\nThe number of surviving people:\n{}'.format(df[df['Survived'] == 1]['Survived'].sum()))
 st.write('\nThe number of surviving people boarded at Southampton:\n{}'.format(df[(df['Embarked']== 'Southampton')&(df['Survived'] == 1)]['Survived'].sum()))
 st.write('\nThe number of surviving people boarded at Cherburgo:\n{}'.format(df[(df['Embarked']== 'Cherburgo')&(df['Survived'] == 1)]['Survived'].sum()))
 st.write('\nThe number of surviving people boarded at Queenstown:\n{}'.format(df[(df['Embarked']== 'Queenstown')&(df['Survived'] == 1)]['Survived'].sum()))
with col2:
 st.video("https://www.youtube.com/watch?v=1EMkCJWQIDY")
 st.text('''You can find more information watching the titanic movie
 and find the movie on disney plus''')
 st.markdown('https://www.disneyplus.com/es-es/movies/titanic/1vXLGiOUqEP9')

 code = '''st.video("https://www.youtube.com/watch?v=1EMkCJWQIDY")
 st.markdown('https://www.disneyplus.com/es-es/movies/titanic/1vXLGiOUqEP9')'''
 st.code(code, language='python')
