import streamlit as st
import pickle

# Load model and vectorizer
model = pickle.load(open("model.pkl", "rb"))
vectorizer = pickle.load(open("vectorizer.pkl", "rb"))

# Page config
st.set_page_config(page_title="Spam Email Classifier", page_icon="📩")

# Title
st.title("📩 Spam Email Classifier")
st.write("Enter an email/message below and check if it's Spam or Not Spam")

# Input box
message = st.text_area("✉️ Enter Email Content:")

# Button
if st.button("Predict"):
    if message.strip() == "":
        st.warning("Please enter a message first!")
    else:
        # Transform input
        data = vectorizer.transform([message])

        # Predict
        result = model.predict(data)[0]

        # Output
        if result == 1:
            st.error("🚨 This is a SPAM email")
        else:
            st.success("✅ This is NOT spam (Ham email)")

# Footer
st.markdown("---")
st.caption("Built with ❤️ using Streamlit")
