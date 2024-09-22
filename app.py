import streamlit as st
import pickle
import numpy as np

# Load the trained model
with open('data/titanic_model.pkl', 'rb') as file:
    model = pickle.load(file)

# Function to make predictions
def predict_survival(Pclass, Sex, Age, Fare, Embarked):
    features = np.array([[Pclass, Sex, Age, Fare, Embarked]])
    prediction = model.predict(features)
    return prediction

# User interface with Streamlit
st.title('🚢 Titanic Survival Prediction')
st.write('🔍 Predict whether a passenger would have survived the Titanic sinking.')

# Adding some space and a separator
st.markdown("---")

Pclass = st.selectbox('Passenger Class 🛏️', [1, 2, 3])
Sex = st.selectbox('Gender 🧍', ['Male', 'Female'])
Age = st.slider('Age 🎂', 0, 80, 25)
Fare = st.slider('Fare 💵', 0, 500, 15)
Embarked = st.selectbox('Port of Embarkation 🛳️', ['Southampton', 'Cherbourg', 'Queenstown'])

# Convert user inputs to the format expected by the model
Sex = 0 if Sex == 'Male' else 1
Embarked = 0 if Embarked == 'Southampton' else (1 if Embarked == 'Cherbourg' else 2)

# Adding some space and a separator
st.markdown("---")

if st.button('Predict 🧭'):
    result = predict_survival(Pclass, Sex, Age, Fare, Embarked)
    if result == 1:
        st.success('✅ The passenger would have survived.')
    else:
        st.error('❌ The passenger would not have survived.')

# Adding a footer note
st.markdown("---")
st.write("Developed with 💻 by Zakaria ATLASSI DOUCH")
