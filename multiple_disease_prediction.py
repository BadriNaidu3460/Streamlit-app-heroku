# -*- coding: utf-8 -*-
"""
Created on Wed Dec  3 17:37:23 2025

@author: badri
"""

import pickle
import streamlit as st
from streamlit_option_menu import option_menu

diabetes_model=pickle.load(open('C:/Users/badri/OneDrive/Desktop/project-dp/diabetes_model.sav','rb'))


#side bar for navigate

with st.sidebar:
    selected=option_menu('multiple disease prediction system',['diabetes prediction'],default_index=0)


# diabetes prediction page
if (selected=='diabetes prediction'):
    #page title
    st.title('diabetes prediction using ML')
    
    col1,col2,col3 = st.columns(3)
    with col1:
        Pregnancies = st.text_input("enter the number of pregnancies")
    with col2:
        Glucose = st.text_input("enter the glucose level")
    with col3:
        BloodPressure = st.text_input("enter the bloodpressure value")
    with col1:
        SkinThickness = st.text_input("enter the skinthckness value")
    with col2:
        Insulin = st.text_input("enter the insulin value")
    with col3:
        BMI = st.text_input("enter the bmi value")
    with col1:
        DiabetesPedigreeFunction = st.text_input("enter the number of diabetespedigreefunction")
    with col2:
        Age = st.text_input("enter the age of a person")
        
        
        
    
    #code for prediction
    diagnosis=" "
    
    #creating a button for prediction
    if st.button("diabetes test result"):
        diagnosis=diabetes_model.predict([[Pregnancies,Glucose,BloodPressure,SkinThickness,Insulin,BMI,DiabetesPedigreeFunction,Age]])
        if (diagnosis[0]==1):
            diagnosis= "person is diabetic"
        else: 
            diagnosis= "person is not diabetic"
    st.success(diagnosis)
    
    
    
    