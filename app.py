import streamlit as st
import joblib

# Load the trained model
model = joblib.load("spam_classifier.pkl")  # Make sure this path is correct

# Streamlit UI setup
st.set_page_config(page_title="Spam Detector", layout="centered")
st.title("📩 Spam Message Detector")
st.write("Enter a message below to classify it as spam or ham (not spam).")

# User input
user_input = st.text_area("Enter your message here:", height=150)

# Button to trigger prediction
if st.button("Check Message"):
    if user_input.strip() == "":
        st.warning("⚠️ Please enter a message.")
    else:
        prediction = model.predict([user_input])[0]
        if prediction == "spam":
            st.error("❌ This is a Spam Message.")
        else:
            st.success("✅ This is a Ham (Not Spam) Message.")
