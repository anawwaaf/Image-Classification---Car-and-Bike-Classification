import streamlit as st
import requests

# Give the Name of the Application
st.title('Churn Prediction')

# Create Submit Form
with st.form(key='form_parameters'):
    Gender = st.sidebar.selectbox(label='Gender', options=['Female', 'Male'])
    SeniorCitizen = st.sidebar.selectbox(label='SeniorCitizen', options=['No','Yes'])
    Partner = st.sidebar.selectbox(label='Partner', options=['No', 'Yes'])
    Dependents = st.sidebar.selectbox(label='Dependents', options=['No', 'Yes'])
    Tenure = st.number_input('Tenure', min_value=0, step=1, max_value=73)
    PhoneService = st.sidebar.selectbox(label='PhoneService', options=['No', 'Yes'])
    MultipleLines = st.sidebar.selectbox(label='MultipleLines', options=['No','Yes'])
    InternetService = st.sidebar.selectbox(label='InternetService', options=['No','DSL','Fiber optic'])
    OnlineSecurity = st.sidebar.selectbox(label='OnlineSecurity', options=['No','Yes'])
    OnlineBackup = st.sidebar.selectbox(label='OnlineBackup', options=['No','Yes'])
    DeviceProtection = st.sidebar.selectbox(label='DeviceProtection', options=['No','Yes'])
    TechSupport = st.sidebar.selectbox(label='TechSupport', options=['No','Yes'])
    StreamingTV = st.sidebar.selectbox(label='StreamingTV', options=['No','Yes'])
    StreamingMovies = st.sidebar.selectbox(label='StreamingMovies', options=['No','Yes'])
    Contract = st.sidebar.selectbox(label='Contract', options=['Month-to-month','One year','Two year'])
    PaperlessBilling = st.sidebar.selectbox(label='PaperlessBilling', options=['No', 'Yes'])
    PaymentMethod = st.sidebar.selectbox(label='PaymentMethod', options=['Electronic check','Mailed check','Bank transfer (automatic)','Credit card (automatic)'])
    MonthlyCharges = st.number_input('MonthlyCharges', min_value=18.25, step=0.05, max_value=118.75)
    TotalCharges = st.number_input('TotalCharges', min_value=0, step=0.02, max_value=8684.8)

    submitted = st.form_submit_button('Predict')

# inference
if submitted:
    URL = 'https://churn-anawwaaf.koyeb.app//predict'
    param = {'Gender': Gender,
    'SeniorCitizen': SeniorCitizen,
    'Partner': Partner,
    'Dependents': Dependents,
    'Tenure': Tenure,
    'PhoneService': PhoneService,
    'MultipleLines': MultipleLines,
    'InternetService': InternetService,
    'OnlineSecurity': OnlineSecurity,
    'OnlineBackup': OnlineBackup,
    'DeviceProtection': DeviceProtection,
    'TechSupport': TechSupport,
    'StreamingTV': StreamingTV,
    'StreamingMovies':StreamingMovies,
    'Contract': Contract,
    'PaperlessBilling': PaperlessBilling,
    'PaymentMethod': PaymentMethod,
    'MonthlyCharges': MonthlyCharges,
    'TotalCharges': TotalCharges}

    r = requests.post(URL, json=param)
    if r.status_code == 200:
        res = r.json()
        st.title('Telco Customer Churn is {}'.format(res['label_names']))
    else:
        st.title("Unexpected Error")
        st.write(r.status_code)
