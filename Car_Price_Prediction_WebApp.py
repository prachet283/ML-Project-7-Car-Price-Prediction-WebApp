# -*- coding: utf-8 -*-
"""
Created on Thu May 23 15:20:21 2024

@author: prachet
"""

import numpy as np
import pickle
import streamlit as st

#loading. the saved model
loaded_model = pickle.load(open('C:/Users/prachet/OneDrive - Vidyalankar Institute of Technology/Desktop/Coding/Machine Learning/ML-Project-7-Car Price Prediction/car_price_prediction_model.sav','rb'))

#creating a function for prediction

def car_price_prediction(input_data):

    #changing the input data to numpy
    input_data_as_numpy_array = np.asarray(input_data)

    #reshape the array as we are predicting on 1 instance
    input_data_reshaped = input_data_as_numpy_array.reshape(1,-1)

    prediction = loaded_model.predict(input_data_reshaped)
    #print(prediction)

    return prediction[0]
  
    
  
def main():
    
    #giving a title
    st.title('Car Price Prediction Web App')
    
    col1 , col2 = st.columns(2)
    #getting input data from user
    with col1:
        year = st.number_input("Year")
    with col2:
        km_driven = st.number_input("km_driven")
    with col1:
        option1 = st.selectbox('fuel',('Diesel', 'Petrol','CNG','LPG','Electric')) 
        if option1 == 'Diesel':
            fuel = 0
        elif option1 == 'Petrol':
            fuel = 1 
        elif option1 == 'CNG':
            fuel = 2 
        elif option1 == 'LPG':
            fuel = 3
        elif option1 == 'Electric':
            fuel = 4
    with col2:	
        option2 = st.selectbox('seller_type',('Individual', 'Dealer','Trustmark Dealer')) 
        if option2 == 'Individual':
            seller_type = 0
        elif option2 == 'Dealer':
            seller_type = 1 
        elif option2 == 'Trustmark Dealer':
            seller_type = 2 
    with col1:
        option3 = st.selectbox('transmission',('Manual', 'Automatic')) 
        if option3 == 'Manual':
            transmission = 0
        elif option3 == 'Automatic':
            transmission = 1 
    with col2:
        option4 = st.selectbox('owner',('First Owner', 'Second Owner','Third Owner','Fourth & Above Owner','Test Drive Car')) 
        if option4 == 'First Owner':
            owner = 0
        elif option4 == 'Second Owner':
            owner = 1 
        elif option4 == 'Third Owner':
            owner = 2 
        elif option4 == 'Fourth & Above Owner':
            owner = 3
        elif option4 == 'Test Drive Car':
            owner = 4
    
    
    # code for prediction
    price = ''
    
    #creating a button for Prediction
    if st.button('Predict Car Price'):
        price = car_price_prediction((year,km_driven,fuel,seller_type,transmission,owner))
        
    st.success('The Predicted Price: '+ str(price)+'$')
    
    
    
if __name__ == '__main__':
    main()
    
    