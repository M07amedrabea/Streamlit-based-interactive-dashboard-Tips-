
# import Libraries

import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px

st.set_page_config(page_title='Tips Dashboard' , page_icon=None , layout='wide', initial_sidebar_state='auto', menu_items=None)


# Loading data

df = pd.read_csv(r'C:\Users\HP\Desktop\Projects\Streamlit\tip.csv')

# Sidebar

st.sidebar.header('Tips Dashboard')

st.sidebar.image('tip.jpg')

st.sidebar.write('This Dashboard is using Tips dataset from seaborn for educational purposes')



st.write("")
st.sidebar.write('Filter Your Data : ')
cat_filter = st.sidebar.selectbox("Categorical Filtering : ",[None,'sex','smoker','day','time'])
Num_filter = st.sidebar.selectbox("Numerical Filtering : ",[None,'total_bill','tip'])

row_filter = st.sidebar.selectbox("Row Filtering : ",[None,'sex','smoker','day','time'])
col_filter = st.sidebar.selectbox("Column Filtering : ",[None,'sex','smoker','day','time'])





st.sidebar.write("")
st.sidebar.markdown("Made with Love :heart_eyes: \n by Prog. [Mo7amed R@be3](https://github.com/M07amedrabea)")


# Body

st.subheader('Main Measures')
# Row a

a1 , a2 , a3 , a4 = st.columns(4)

a1.metric('Max Total Bill',df['total_bill'].max())
a2.metric('Max Total Bill',df['tip'].max())
a3.metric('Min Total Bill',df['total_bill'].min())
a4.metric('Min Total Bill',df['tip'].min())

# Row B 

st.subheader('total_bill VS tip ')

fig = px.scatter(data_frame = df , x='total_bill' , y = 'tip', color = cat_filter , size=Num_filter, facet_col=col_filter , facet_row=row_filter)

st.plotly_chart(fig,use_container_width = True)


# Row C

st.subheader('More Figures')

c1, c2, c3 = st.columns((4,3,3))

with c1 : 
    st.text('(Sex VS total_bill)')
    fig = px.bar(data_frame = df , x = df['sex'], y = df['total_bill'], color = cat_filter)
    st.plotly_chart(fig, use_container_width= True)


with c2 : 
    st.text('(Smoker Or None_Smoker)  VS. Tips')
    fig = px.pie(data_frame = df , names= df['smoker'], values = df['tip'], color = cat_filter)
    st.plotly_chart(fig, use_container_width= True)

with c3 : 
    st.text('(Days VS. Tips)')
    fig = px.pie(data_frame = df , names= df['day'], values = df['tip'], color = cat_filter,hole=0.4)
    st.plotly_chart(fig, use_container_width= True)