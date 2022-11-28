#Initalization 
import streamlit as st
import pandas as pd
import numpy as np
from prediction import predict
st.title('Classifying NFL Teams')
st.markdown('Predicting if a NFL Team will Qualify for the Playoffs based on Team DVOA Metrics')

st.header('DVOA Metrics')
col1, col2= st.columns(2)
with col1:
    st. text("Offense")
    o_pass = st.slider('Pass DVOA', -1.000, 1.000, .001, key = 'o_pass')
    o_run = st.slider('Rush DVOA', -1.000, 1.000, .001, key = 'o_rush')
    o_variance = st.slider("Variance", -1.000, 1.000, .001, key = 'o_variance')
    o_schedule = st.slider("Schedule", -1.000, 1.000, .001, key = 'o_schedule' )
    
with col2:
    st.text("Defense")
    d_pass = st.slider('Pass DVOA', -1.000, 1.000, .001, key = 'd_pass')
    d_run = st.slider('Rush DVOA', -1.000, 1.000, .001, key = 'd_rush')
    d_variance = st.slider("Variance", -1.000, 1.000, .001, key = 'd_variance')
    d_schedule = st.slider("Schedule", -1.000, 1.000, .001, key = 'd_schedule')
    

if st.button('Predict Playoff'):
    result = predict(np.array([[o_pass, o_run, o_variance, o_schedule, d_pass, d_run, d_variance, d_schedule,]]))
    st.text(result[0])