import streamlit as st
import pandas as pd
import pickle

# Load model, scaler, and feature names
with open('model.pkl', 'rb') as f:
    model = pickle.load(f)

with open('scaler.pkl', 'rb') as f:
    scaler = pickle.load(f)

with open('features.pkl', 'rb') as f:
    feature_names = pickle.load(f)

st.title("🧠 Social Behavior Classifier")
st.write("Fill out the form below to predict the behavior class.")

# Collect user input using Streamlit widgets
time_spent_alone = st.slider("Time spent alone (hours/day)", 0.0, 24.0, 4.0)
stage_fear = st.selectbox("Stage fear (0 = No, 1 = Yes)", [0, 1])
social_event_attendance = st.slider("Social event attendance (per month)", 0, 30, 5)
going_outside = st.slider("Going outside (times/week)", 0, 14, 3)
drained = st.selectbox("Drained after socializing? (0 = No, 1 = Yes)", [0, 1])
friend_circle_size = st.slider("Friend circle size", 0, 100, 10)
post_frequency = st.slider("Social media post frequency (per week)", 0, 50, 5)

# Predict on button click
if st.button("Predict"):
    # Create DataFrame in the same feature order as used in training
    input_data = pd.DataFrame([[
        time_spent_alone,
        stage_fear,
        social_event_attendance,
        going_outside,
        drained,
        friend_circle_size,
        post_frequency
    ]], columns=feature_names)

    # Scale input
    input_scaled = scaler.transform(input_data)

    # Predict
    prediction = model.predict(input_scaled)[0]
    
    # Show result
    # Map 0/1 to Yes/No (or any custom labels)
    prediction_label = "Extrovert" if prediction == 1 else "Introvert"
    st.success(f"✅ Prediction: {prediction_label}")
