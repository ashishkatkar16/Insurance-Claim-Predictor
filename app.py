#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Mar 12 18:25:01 2024

@author: ashishkatkar
"""

import pickle
import streamlit as st

st.set_page_config(page_title="Insurance Claim Predictor", page_icon=":bar_chart:")

hide_st_style = """
            <style>
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            header {visibility: hidden;}
            </style>
            """
st.markdown(hide_st_style, unsafe_allow_html=True)


st.title('Insurance Claim Predictor :bar_chart:')

load = open('model.pkl','rb')
model = pickle.load(load)


def predict(age,gender,bmi,smoker):
    prediction = model.predict([[age,gender,bmi,smoker]])
    return prediction

def main():
    
    st.markdown('This is a very simple webapp for prediction of claim amount :chart:')
    age = st.number_input('Age', min_value= 0 , max_value=100)
    gender = st.selectbox('Gender', ('Male','Female'))
    bmi = st.number_input('BMI')
    smoker = st.selectbox('Smoker',('Yes','No'))
    if st.button('Predict'):
        result = predict(age,gender,bmi,smoker)
        st.success('The claim is : ${} '.format(result))                          
                          
        
if __name__ == '__main__':
    main()
