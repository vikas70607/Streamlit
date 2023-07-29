import streamlit as st
import pandas as pd
import numpy as np
import pickle

st.write("""
# Loan eligibility Prediction app
""")

st.write(""" 
         ## Enter your features
         """)


def user_input_features():
    gender = st.selectbox('Gender',('Male','Female'))
    Credit = st.selectbox('Credit History',('Positive','Negative'))
    area = st.selectbox('Property Area',('Urban','Rural','Semiurban'))
    income = st.slider('Applicant Income', 0,100000,0)
    CoIncome = st.slider('Co-Applicant Income', 0,10000,0)
    Term = st.slider('Co-Applicant Income', 12,480,12,step=3)
    
    features = [gender, income, CoIncome, Term,Credit,area]
    
    return features
input = user_input_features()


if(input[0] == 'Male'):
    input[0] = 1
else:
    input[0] = 0
    
if(input[4] == 'Positive'):
    input[4] = 1
else:
    input[4] = 0
    
if(input[5] == 'Urban'):
    input[5] = 0
elif(input[5] == 'Rural'):
    input[5] = 2
else:
    input[5] = 1

# Reads in saved classification model
with open('loan_pkl' , 'rb') as f:
    lr = pickle.load(f)

print(input)
# Apply model to make predictions
prediction = lr.predict([input])

st.subheader('Prediction')
if prediction[0] == 1:
    st.write(''' ### Loan Approved ''')
else:
    st.write(''' ### Oops , not this time ''')
