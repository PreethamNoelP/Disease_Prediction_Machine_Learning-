# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import pickle
import streamlit as st
from streamlit_option_menu import option_menu


#Loading the saved Models 

diabetes_model = pickle.load(open('C:/Users/preet/OneDrive/Desktop/Multiple Disease Prediction\Disease Prediction/diabetes_model.sav','rb'))

heart_disease_model=pickle.load(open('C:/Users/preet/OneDrive/Desktop/Multiple Disease Prediction/Disease Prediction/heart_disease_model.sav','rb'))

parkinsons_model=pickle.load(open('C:/Users/preet/OneDrive/Desktop/Multiple Disease Prediction/Disease Prediction/parkinsons_model.sav','rb'))


#Sidebar for Navigation 

with st.sidebar:
    selected = option_menu('Disease Predicition',
                           ['Diabetes Prediction',
                            'Heart Disease Prediction',
                            'Parkinsons Prediction'],
                           
                           icons = ['activity','heart-pulse-fill','person'],
                           
                           default_index = 0)
    
# Diabetes Prediciton Page 
if(selected=='Diabetes Prediction'):
    st.title('Diabetes Prediction Model Using ML')
    
    
    Glucose = st.text_input('Glucose Level')
    BloodPressure = st.text_input('Blood Pressure value')
    SkinThickness = st.text_input('Skin Thickness Value ')
    Insulin = st.text_input('Insulin Level')
    BMI = st.text_input('BMI value')
    DiabetesPedigreeFunction = st.text_input(' Diabetes Pedigree Function value')
    Age = st.text_input('Age of the Individual')
        
    diabetes_diagnosis = ''
    if st.button('Diabetes Result'):
        diabetes_prediction = diabetes_model.predict([[Glucose,BloodPressure,SkinThickness,Insulin,BMI,DiabetesPedigreeFunction,Age]])
        
        if(diabetes_prediction[0]==1):
            diabetes_diagnosis = 'The Person is Diabetic'
        else:
            diabetes_diagnosis = 'The Person is Not Diabetic'
            
        st.success(diabetes_diagnosis)

if(selected=='Heart Disease Prediction'):
    st.title('Heart Disease Prediction Model Using ML')
    
    age = st.text_input('Age')
    sex = st.text_input('Sex')
    cp = st.text_input('Chest Pain types')
    trestbps = st.text_input('Resting Blood Pressure')
    chol = st.text_input('Serum Cholestoral in mg/dl')
    fbs = st.text_input('Fasting Blood Sugar > 120 mg/dl')
    restecg = st.text_input('Resting Electrocardiographic results')
    thalach = st.text_input('Maximum Heart Rate achieved')
    exang = st.text_input('Exercise Induced Angina')
    oldpeak = st.text_input('ST depression induced by exercise')
    slope = st.text_input('Slope of the peak exercise ST segment')
    ca = st.text_input('Major vessels colored by flourosopy')
    thal = st.text_input('thal: 0 = normal; 1 = fixed defect; 2 = reversable defect')
    
    heart_diagnosis = ''
    heart_prediction = None
    
    if st.button('Heart Disease Test Result'):
        user_input = [age, sex, cp, trestbps, chol, fbs, restecg, thalach, exang, oldpeak, slope, ca, thal]
        user_input = [float(x) for x in user_input]
        
        # Assuming heart_disease_model is already defined
        heart_prediction = heart_disease_model.predict([user_input])

    if heart_prediction is not None:
        if heart_prediction[0] == 1:
            heart_diagnosis = 'The person is having heart disease'
        else:
            heart_diagnosis = 'The person does not have any heart disease'
        
        st.success(heart_diagnosis)

    
    
if selected == 'Parkinsons Prediction':
    st.title('Parkinsons Prediction Model Using ML')
    
    # Assuming these are Streamlit text input calls
    fo = st.text_input('fo')
    fhi = st.text_input('fhi')
    flo = st.text_input('flo')
    Jitter_percent = st.text_input('Jitter_percent')
    Jitter_Abs = st.text_input('Jitter_Abs')
    RAP = st.text_input('RAP')
    PPQ = st.text_input('PPQ')
    DDP = st.text_input('DDP')
    Shimmer = st.text_input('Shimmer')
    Shimmer_dB = st.text_input('Shimmer_dB')
    APQ3 = st.text_input('APQ3')
    APQ5 = st.text_input('APQ5')
    APQ = st.text_input('APQ')
    DDA = st.text_input('DDA')
    NHR = st.text_input('NHR')
    HNR = st.text_input('HNR')
    RPDE = st.text_input('RPDE')
    DFA = st.text_input('DFA')
    spread1 = st.text_input('spread1')
    spread2 = st.text_input('spread2')
    D2 = st.text_input('D2')
    PPE = st.text_input('PPE')

    user_input = [fo, fhi, flo, Jitter_percent, Jitter_Abs,
                  RAP, PPQ, DDP, Shimmer, Shimmer_dB, APQ3, APQ5,
                  APQ, DDA, NHR, HNR, RPDE, DFA, spread1, spread2, D2, PPE]

    try:
        user_input = [float(x) for x in user_input]
        
        parkinsons_prediction = parkinsons_model.predict([user_input])

        if parkinsons_prediction[0] == 1:
            parkinsons_diagnosis = "The person has Parkinson's disease"
        else:
            parkinsons_diagnosis = "The person does not have Parkinson's disease"

        st.success(parkinsons_diagnosis)
    except ValueError:
        st.error("Please enter valid numerical values.")
