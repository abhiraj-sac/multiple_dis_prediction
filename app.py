import pickle
import streamlit as st
# from streamlit_option_menu import option_menu

# import numpy as np

# # diabetic_model = pickle.load(open('C:/Users/Abhi/OneDrive/Desktop/multiple_dis_prediction/diabetic_model.sav'))
# # heart_model = pickle.load(open('C:/Users/Abhi/OneDrive/Desktop/multiple_dis_prediction/heart_model.sav'))
# # diabetes_model = pickle.load(open('diabetic_model.sav', 'rb'))
heart_disease_model = pickle.load(open('model.pkl', 'rb'))

# # with st.sidebar:
# #     selected = option_menu('Multiple_disease', ['Diabetic', 'Heart'], icons=['activity', 'heart'],
# #                            default_index=0)

# # if selected == 'Heart':

#     # page title
# st.title('Diabetes Prediction using ML')

#     # getting the input data from the user
# col1, col2, col3 = st.columns(3)

# with col1:
#     male = st.number_input('male')

# with col2:
#     age = st.number_input('age')

# with col3:
#     education = st.number_input('education')

# with col1:
#     currentSmoker = st.number_input('currentSmoker')

# with col2:
#     cigsPerDay = st.number_input('cigsPerDay')

# with col3:
#     BPMeds = st.number_input('BPMeds')

# with col1:
#     prevalentStroke = st.number_input('prevalentStroke')

# with col2:
#     prevalentHyp = st.number_input('prevalentHyp')
# with col3:
#     diabetes = st.number_input('diabetes')
# with col1:
#     totChol = st.number_input('totChol')

# with col2:
#     sysBP = st.number_input('sysBP')
# with col3:
#     diaBP = st.number_input('diaBP')
# with col1:
#     BMI = st.number_input('BMI')

# with col2:
#     heartRate = st.number_input('heartRate')
# with col3:
#     glucose = st.number_input('glucose')

#     # code for Prediction
#     # diab_diagnosis = ''

#     # creating a button for Prediction

# if st.button('Diabetes Test Result'):
#     pred = heart_disease_model.predict([[male, age, education, currentSmoker, cigsPerDay, BPMeds, prevalentStroke,prevalentHyp,diabetes,totChol,sysBP,diaBP,BMI,heartRate,glucose]])
#     st.header(pred[0])
# # if selected == 'Heart':
# #     st.title('Heart')




import streamlit as st

# Load your heart attack prediction model (replace with your actual code)
def predict_heart_attack(features):
    # Your model code here
    return "Heart Attack Prediction Result"

# Load your diabetes prediction model (replace with your actual code)
# def predict_diabetes(features):
#     # Your model code here
#     return "Diabetes Prediction Result"

# Sidebar to select between models
model_option = st.sidebar.radio("Select Model", ["Heart Attack Prediction", "Diabetes Prediction"])
diabetes_model = pickle.load(open('rf_model.pkl', 'rb'))

# Main content based on selected model
st.title("Health Prediction App")

if model_option == "Heart Attack Prediction":
    st.header("Heart Attack Prediction")
    # Input features for heart attack prediction
    # Replace with your actual input fields
    col1, col2, col3 = st.columns(3)

    with col1:
        male = st.number_input('male')

    with col2:
        age = st.number_input('age')

    with col3:
        education = st.number_input('education')

    with col1:
        currentSmoker = st.number_input('currentSmoker')

    with col2:
        cigsPerDay = st.number_input('cigsPerDay')

    with col3:
        BPMeds = st.number_input('BPMeds')

    with col1:
        prevalentStroke = st.number_input('prevalentStroke')

    with col2:
        prevalentHyp = st.number_input('prevalentHyp')
    with col3:
        diabetes = st.number_input('diabetes')
    with col1:
        totChol = st.number_input('totChol')

    with col2:
        sysBP = st.number_input('sysBP')
    with col3:
        diaBP = st.number_input('diaBP')
    with col1:
        BMI = st.number_input('BMI')

    with col2:
        heartRate = st.number_input('heartRate')
    with col3:
        glucose = st.number_input('glucose')

        # code for Prediction
        # diab_diagnosis = ''

        # creating a button for Prediction

    if st.button('Heart Test Result'):
        pred = heart_disease_model.predict([[male, age, education, currentSmoker, cigsPerDay, BPMeds, prevalentStroke,prevalentHyp,diabetes,totChol,sysBP,diaBP,BMI,heartRate,glucose]])
        if pred[0] ==1:
            st.header("We are sorry to say, but you will suffer!")
        else:
            st.header("Congrats you are safe!")

# Pregnancies	Glucose	BloodPressure	SkinThickness	Insulin	BMI	DiabetesPedigreeFunction	Age


elif model_option == "Diabetes Prediction":
    st.header("Diabetes Prediction")
    # Input features for diabetes prediction
    # Replace with your actual input fields
    col1, col2, col3 = st.columns(3)

    with col1:
        Pregnancies = st.number_input('Pregnancies')

    with col2:
        Glucose = st.number_input('Glucose')

    with col3:
        BloodPressure = st.number_input('BloodPressure')

    with col1:
        SkinThickness = st.number_input('SkinThickness')

    with col2:
        Insulin = st.number_input('Insulin')

    with col3:
        BMI = st.number_input('BMI')

    with col1:
        DiabetesPedigreeFunction = st.number_input('DiabetesPedigreeFunction')

    with col2:
        Age = st.number_input('Age')

    # glucose_level = st.slider("Glucose Level", 70, 200, 120)
    # bmi = st.slider("BMI", 15.0, 45.0, 25.0)

    if st.button('Heart Test Result'):
        pred = diabetes_model.predict([[Pregnancies,Glucose,BloodPressure,SkinThickness,Insulin,BMI,DiabetesPedigreeFunction,Age]])
        if pred[0] ==1:
            st.header("We are sorry to say, but you will suffer!")
        else:
            st.header("Congrats you are safe!")