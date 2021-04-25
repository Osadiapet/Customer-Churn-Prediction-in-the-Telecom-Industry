import pandas as pd
import matplotlib.pyplot as plt 
import pickle 
import streamlit as st

st.title('Predicting Bank Customer Churn With Machine Learning techniques')
st.header('Input the required parameter')
def predict():
    try:
        geography = st.radio("Country",('France', 'Spain', 'Germany'))
        gender = st.radio("Gender",('Male', 'Female'))
        age = st.slider('Age', 18, 100, 50)
        creditscore = st.slider('Credit Score', 300, 900, 700)
        tenure = st.slider('Tenure Payment Plan', 0, 10, 4)

        balance = st.slider('Balance', 0, 260000, 50000)    
        numofproducts = st.slider('Number of products', 1, 4, 2)
    
        card = st.radio("Has a card ?",('Yes', 'No'))
        
        if HasCrCard == 'Yes':
            HasCrCard = 1

        
        else:
            HasCrCard = 0


        active = st.radio("Is Active Member ?",('Yes', 'No'))
        if IsActiveMember == 'Yes':
            IsActiveMember = 1
        else:
            IsActiveMember = 0
        Salary = st.slider('Estimated Salary', 200, 200000, 20000)


        html_temp = """
        <div style="background-color:#ff9966;padding:5px;margin-bottom:20px"> </div>
        """
        st.markdown(html_temp,unsafe_allow_html=True)
        result = ""
        value=[geography, gender, age, creditscore, tenure, balance, numofproducts, card, active, Salary]
        model=pickle.load(open('Customer_Churn.pkl','rb'))
        if st.button("Predict"):
            result=model.predict([value])
            
            if result[0] == 0:
                st.success('This customer is less likely to cancel the subscription !')
                st.balloons()
            else:
                st.success('Warning ! This customer is more likely to cancel the subscription !')
    except:
        st.exception('There is some exception')
predict()
st.header('By Simon Peter Osadiapet')
