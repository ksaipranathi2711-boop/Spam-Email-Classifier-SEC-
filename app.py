import streamlit as st
import pickle

# Load model and vectorizer
model = pickle.load(open("spam_model.pkl", "rb"))
vectorizer = pickle.load(open("vectorizer.pkl", "rb"))

# Page Config
st.set_page_config(
    page_title="AI Spam Email Detector",
    page_icon="📧",
    layout="centered"
)

# Custom CSS
st.markdown("""
<style>

.stApp{
    background: linear-gradient(135deg,#0f172a,#1e293b);
}

.hero{
    text-align:center;
    padding:20px;
}

.hero h1{
    color:white;
    font-size:3rem;
}

.hero p{
    color:#cbd5e1;
    font-size:1.1rem;
}

.card{
    background: rgba(255,255,255,0.08);
    backdrop-filter: blur(12px);
    padding:25px;
    border-radius:20px;
    box-shadow:0px 8px 32px rgba(0,0,0,0.3);
}

div.stTextArea textarea{
    background-color:white;
    color:black;
    border-radius:10px;
}

div.stButton > button{
    width:100%;
    height:55px;
    border:none;
    border-radius:12px;
    background:linear-gradient(90deg,#6366f1,#8b5cf6);
    color:white;
    font-size:18px;
    font-weight:bold;
}

.metric-card{
    background: rgba(255,255,255,0.08);
    padding:15px;
    border-radius:15px;
    text-align:center;
    color:white;
}

.footer{
    text-align:center;
    color:#cbd5e1;
    margin-top:30px;
}

</style>
""", unsafe_allow_html=True)

# Hero Section
st.markdown("""
<div class="hero">
    <h1>📧 AI Spam Email Detector</h1>
    <p>Detect Spam Emails Instantly Using Machine Learning</p>
</div>
""", unsafe_allow_html=True)

# Stats
col1, col2, col3 = st.columns(3)

with col1:
    st.markdown("""
    <div class="metric-card">
        <h3>98%</h3>
        <p>Accuracy</p>
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown("""
    <div class="metric-card">
        <h3>ML</h3>
        <p>Powered</p>
    </div>
    """, unsafe_allow_html=True)

with col3:
    st.markdown("""
    <div class="metric-card">
        <h3>24/7</h3>
        <p>Detection</p>
    </div>
    """, unsafe_allow_html=True)

st.write("")

# Main Card
st.markdown('<div class="card">', unsafe_allow_html=True)

email_text = st.text_area(
    "✍️ Enter Email Content",
    height=250,
    placeholder="Paste your email content here..."
)

predict_btn = st.button("🚀 Predict")

st.markdown('</div>', unsafe_allow_html=True)

# Prediction
if predict_btn:

    if email_text.strip() == "":
        st.warning("Please enter an email message.")
    else:

        transformed_text = vectorizer.transform([email_text])
        prediction = model.predict(transformed_text)[0]

        st.write("")

        if prediction == 1:
            st.markdown("""
            <div style="
            background:#dc2626;
            padding:20px;
            border-radius:15px;
            color:white;
            text-align:center;
            font-size:24px;
            font-weight:bold;">
            🚨 SPAM EMAIL DETECTED
            </div>
            """, unsafe_allow_html=True)

        else:
            st.markdown("""
            <div style="
            background:#16a34a;
            padding:20px;
            border-radius:15px;
            color:white;
            text-align:center;
            font-size:24px;
            font-weight:bold;">
            ✅ LEGITIMATE EMAIL
            </div>
            """, unsafe_allow_html=True)

# Footer
st.markdown("""
<div class="footer">
<hr>
Built with ❤️ using Streamlit & Machine Learning
</div>
""", unsafe_allow_html=True)
