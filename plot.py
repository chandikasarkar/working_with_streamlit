import numpy as np
import pandas as pd
import streamlit as st 

st.header('1. Charts with randon dataset')
chart_data = pd.DataFrame(np.random.randn(20,3),columns =["line 1","line 2","line 3"])

st.subheader('1.1 Line chart')
st.line_chart(chart_data)

st.subheader('1.2 Area chart')
st.area_chart(chart_data)

st.subheader('1.3 Bar chart')
st.bar_chart(chart_data)

st.header('2.Data Visualization with Matplotlib ans Seaborn')
import matplotlib.pyplot as plt
import seaborn as sns

st.subheader('2.1 Loading the DataFrame')
df=pd.read_csv('C:\\Users\chand\OneDrive\Desktop\stremlit\iris.csv')
st.dataframe(df)

st.subheader('2.2 Distribution the plot with Matplotlib')
fig=plt.figure(figsize=(15,8))
df['species'].value_counts().plot(kind='bar')
st.pyplot(fig)

st.subheader('2.2 Distribution the plot with Seaborn')
fig=plt.figure(figsize=(15,8))
sns.distplot(df['sepal_length'])
st.pyplot(fig)

st.header('3.Multiple graphs')
col1,col2=st.columns(2)
with col1:
    col1.header ='KDE = False'
    fig1=plt.figure(figsize=(5,5))
    sns.distplot(df['sepal_length'],kde=False)
    st.pyplot(fig1)

with col2:
    col2.header='Hist = False'
    fig2=plt.figure(figsize=(5,5))
    sns.distplot(df['sepal_length'] , hist = False)
    st.pyplot(fig2)


st.header('4.Changing the style')
col1,col2=st.columns(2)
with col1:
    col1.header ='hist = False'
    fig1=plt.figure(figsize=(5,5))
    sns.set_style('darkgrid')
    sns.set_context('notebook')
    sns.distplot(df['sepal_length'],hist =False)
    st.pyplot(fig1)

with col2:
    col2.header='Hist = False'
    fig2=plt.figure(figsize=(5,5))
    sns.set_theme(context='poster',style='dark')
    # sns.set_style('darkgrid')
    # sns.set_context('notebook'
    sns.distplot(df['sepal_length'] , hist = False)
    st.pyplot(fig2)

st.header('5.Exploring Different Graphs')

st.subheader('5.1 Scatter plot ')
fig,ax= plt.subplots(figsize=(15,8))
ax.scatter(*np.random.random(size=(2,100)))
st.pyplot(fig)

st.subheader('5.2 Count-Plot')
fig=plt.figure(figsize=(15,8))
sns.countplot(data=df,x='species')
st.pyplot(fig)

st.subheader('5.3 Box Plot')
fig=plt.figure(figsize=(15,8))
sns.boxplot(data=df,x='species',y='petal_length')
st.pyplot(fig)

st.subheader('5.4 Violin-Plot')
fig=plt.figure(figsize=(15,8))
sns.violinplot(data=df,x='species',y='petal_length')
st.pyplot(fig)


