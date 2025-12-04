# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import numpy as np
import pickle
import pandas as pd

#loading the trained model
loaded_model=pickle.load(open(r'C:/Users/badri/OneDrive/Desktop/project-dp/trained_model.sav','rb'))    


input_data=(1,85,66,29,0,26.6,0.351,31)
feature_names=['Pregnancies','Glucose','BloodPressure','SkinThickness','Insulin','BMI','DiabetesPedigreeFunction','Age']
input_df=pd.DataFrame([input_data],columns=feature_names)
prediction=loaded_model.predict(input_df)
print(prediction)
if prediction[0]==1:
  print("patient is diabetic")
else:
  print("patient is not diabetic")