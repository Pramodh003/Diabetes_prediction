# -*- coding: utf-8 -*-
"""
Created on Sat Dec 11 11:20:47 2021

@author: pramo
"""

import numpy as np
import pickle
import streamlit as st

loaded_model = pickle.load(open('C:/Users/pramo/trained_model.sav', 'rb'))

#creating function

def diabetes_prediction(input_data):
    

# changing the input_data to numpy array
    input_data_as_numpy_array = np.asarray(input_data)

# reshape the array as we are predicting for one instance
    input_data_reshaped = input_data_as_numpy_array.reshape(1,-1)

    prediction = loaded_model.predict(input_data_reshaped)
    print(prediction)

    if (prediction[0] == 0):
        return 'The person is not diabetic'
    else:
        return 'The person is diabetic'
    
    
    
    
def main():
    
    #giving title for webpage
    
    st.title("Diabetes prediction")
    
    #getting the input data
    
    
    Pregnancies = st.text_input('Number of pregnancies')
    Glucose = st.text_input('Gluose level')
    BloodPressure = st.text_input('BloodPressure value')
    SkinThickness = st.text_input('skin thikness')
    Insulin = st.text_input('Insulin level')
    BMI = st.text_input('BMI value')
    DiabetesPedigreeFunction = st.text_input('Diabetes Pedigree Function value')
    Age = st.text_input('age of person')
                        
    #code for prediction
    diagnosis = ''
    
    #creating button for prediction
    if st.button('diabetes test result'):
        diagnosis = diabetes_prediction([Pregnancies,Glucose,BloodPressure,SkinThickness,Insulin,BMI,DiabetesPedigreeFunction,Age])
    
    st.success(diagnosis)
    
    
if __name__ == '__main__':
    main()
        