import pandas as pd 

import matplotlib.pyplot as plt 
import pickle 
import streamlit as st

st.title('Customer Churn Prediction Assistant')

st.markdown('This application is meant to assist banks in dealing with customer curn to know which customer will churn based on certain features')
st.markdown('Please Enter the below details to know the results')

 
# loading the trained model
pickle_in = open('BankChurnGB.pkl', 'rb') 
classifier = pickle.load(pickle_in)
 
@st.cache()

def prediction(CreditScore, Geography, Gender, Age, Tenure, Balance, NumOfProducts, HasCrCard,IsActiveMember, EstimatedSalary):

    if Geography == 'Spain':
        Geography = 0
    elif Geography== 'Germany':
        Geography = 1
    else:
        Geography=2
        
    if Gender == 'Male':
        Gender = 0
    else:
        Gender = 1

    if HasCrCard == '1':
        HasCrCard=1
    else:
        HasCrCard = 0

    if IsActiveMember == '1':
        IsActiveMember = 1
    else:
        IsActiveMember =0

    # Making predictions 
    prediction = classifier.predict([[CreditScore, Geography, Gender, Age, Tenure, Balance, NumOfProducts, HasCrCard,IsActiveMember, EstimatedSalary]])
     
    if prediction == 0:
        pred = 'is *__NOT__* likely to churn'
    else:
        pred = 'is likely to churn '
    return pred
      
  
# this is the main function in which we define our webpage  
def main():       
    # front end elements of the web page 
    html_temp = """ 
    <div style ="background-color:yellow;padding:13px"> 
    <h1 style ="color:black;text-align:center;"> Customer Churn Prediction ML App</h1> 
    </div> 
    """

    # display the front end aspect
    st.markdown(html_temp, unsafe_allow_html = True) 
      
    # following lines create boxes in which user can enter data required to make prediction 
    CreditScore = st.number_input('Credit Score of customer')
    Geography=st.selectbox("Geographical Location / Country of customer",('Spain', 'Germany', 'France'))
    Gender=st.selectbox('Gender of customer', ('Male', 'Female'))
    Age=st.slider('Age of customer',0,120,10)
    Tenure=st.slider('Number of years customer has been associated with the bank',0,100,3)
    Balance = st.number_input("Amount of balance in customer's account")
    NumOfProducts=st.slider('Number of Products', 0,10,2)
    HasCrCard=st.selectbox('Do customer owns a credit card', ('Yes', 'No'))
    IsActiveMember=st.selectbox('Is customer an active member with the bank',('Yes', 'No'))
    EstimatedSalary=st.number_input('Estimated salary of customer')

    result =""

     # when 'Predict' is clicked, make the prediction and store it 
    if st.button("Predict"): 
        result = prediction(CreditScore, Geography, Gender, Age, Tenure, Balance, NumOfProducts, HasCrCard,IsActiveMember, EstimatedSalary)
        st.success('This customer {}'.format(result))
       
if __name__=='__main__': 
    main()
      


  