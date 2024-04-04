import streamlit as st
import numpy as np
import pickle

pickle_RandomForest_model = open("G:\\My Drive\\MPSTME\\SEM IV\\Machine Learning\\Avnish\\RandomForest.pkl", "rb")
RandomForest_model = pickle.load(pickle_RandomForest_model)



#test fuction
def predict_price(Area ,No_of_Bedrooms ,AC ,Gas_connection ,Power_Backup ,SwimmingPool ,Children_Play_Area):
    
    test_values = [Area ,No_of_Bedrooms ,AC ,Gas_connection ,Power_Backup ,SwimmingPool ,Children_Play_Area]
    Price_Predicted = RandomForest_model.predict(test_values)

    return (Price_Predicted)

st.title("House Price Prediction Model")

hide_st_style = """
            <style>
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            header {visibility: hidden;}
            </style>
            """
st.markdown(hide_st_style, unsafe_allow_html=True)

# Input columns
st.sidebar.header("Input Parameters")
Area = st.sidebar.text_input(" Enter Area ")
No_of_Bedrooms = st.sidebar.text_input("Enter No. of Bedrooms")
AC = st.sidebar.text_input("Enter  AC (Yes/No)")
Gas_connection = st.sidebar.text_input("Enter  Gas Connection (Yes/No)")
Power_Backup = st.sidebar.text_input("Enter  Power Backup (Yes/No)")
SwimmingPool = st.sidebar.text_input("Enter Swimming  Pool (Yes/No)")
Children_Play_Area = st.sidebar.text_input("Enter  Children Play Area (Yes/No)")

# enter your output hre
if st.sidebar.button("Check predicted price:"):
    Price = predict_price(int(Area) ,int(No_of_Bedrooms) ,int(AC) ,int(Gas_connection) ,int(Power_Backup) ,int(SwimmingPool) ,int(Children_Play_Area))
    st.success(f"The estimated price of the property is : {Price}")

