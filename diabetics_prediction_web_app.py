# -*- coding: utf-8 -*-
"""
Created on Tue Dec  2 17:50:33 2025

@author: badri
"""

import numpy as np
import pickle
import streamlit as st
import pandas as pd


loaded_model=pickle.load(open('C:/Users/badri/OneDrive/Desktop/project-dp/trained_model.sav','rb'))
    


def diabetes_predction(input_data):
    
    input_data=(1,85,66,29,0,26.6,0.351,31)
    feature_names=['Pregnancies','Glucose','BloodPressure','SkinThickness','Insulin','BMI','DiabetesPedigreeFunction','Age']
    input_df=pd.DataFrame([input_data],columns=feature_names)
    prediction=loaded_model.predict(input_df)
    print(prediction)
    if prediction[0]==1:
        return "patient is diabetic"
    else:
        return "patient is not diabetic"
      
      
      
def main():
    #giving a title
    st.title("diabetes prediction web app")
    
    #getting the input data from the user
    Pregnancies = st.text_input("enter the number of pregnancies")
    Glucose = st.text_input("enter the glucose level")
    BloodPressure = st.text_input("enter the bloodpressure value")
    SkinThickness = st.text_input("enter the skinthckness value")
    Insulin = st.text_input("enter the insulin value")
    BMI = st.text_input("enter the bmi value")
    DiabetesPedigreeFunction = st.text_input("enter the number of diabetespedigreefunction")
    Age = st.text_input("enter the age of a person")
    
    #code for prediction
    diagnosis=" "
    
    #creating a button for prediction
    if st.button("diabetes test result"):
        diagnosis=diabetes_predction([Pregnancies,Glucose,BloodPressure,SkinThickness,Insulin,BMI,DiabetesPedigreeFunction,Age])
    
    st.success(diagnosis)
    
if __name__=='__main__':
    main()
    
    
    