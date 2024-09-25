import streamlit as st
import pandas as pd
import plotly.express as px

st.header('Wholesale')

df = pd.read_csv('Wholesale_customers_data.csv')
with st.expander('show data'):
    st.dataframe(df)


#with st.sidebar.selectbox:
   # op = st.multiselect('select y axis,'[1,2,3])

op = st.sidebar.selectbox('select options',[1,2,3])

df2 = df[df['Region']==op] 
st.write(df2)

op2 = st.sidebar.selectbox('select another',[1,2])

df3 = df2[df2['Channel']==op2]
st.write(df3)


col1,col2,col3, = st.columns(3)

col1.metric('Total Fresh',df3['Fresh'].sum())
col2.metric('Total Milk',df3['Milk'].sum())
col3.metric('Total Grocery',df3['Grocery'].sum())

col1.metric('Total Frozen',df3['Frozen'].sum())
col2.metric('Total Detergents_Paper',df3['Detergents_Paper'].sum())
col3.metric('Total Delicassen',df3['Delicassen'].sum())

fig = px.bar(x=['Fresh','Milk','Grocery','Frozen','Detergents_Paper','Delicassen'], y=[df3['Fresh'].sum(),df3['Milk'].sum(),df3['Grocery'].sum(),df3['Frozen'].sum(),df3['Detergents_Paper'].sum(),df3['Delicassen'].sum()])
st.plotly_chart(fig)

regions = ['Ahmedabad','Banglore','Chennai']

op3 = st.sidebar.selectbox('select region',[1,2,3],format_func=lambda x: regions[x-1])
