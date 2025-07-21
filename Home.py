import streamlit as st

# ✅ Set page configuration
st.set_page_config(page_title="CompeteBot", layout="centered")

# ✅ Custom styles and animations
st.markdown("""
    <style>
        @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;600;800&display=swap');

        html, body, [class*="css"] {
            font-family: 'Inter', sans-serif;
            background-color: #0B132B;
            color: white;
        }

        .block-container {
            padding-top: 2rem;
            padding-bottom: 2rem;
        }

        .stButton>button {
            background-color: #1565C0;
            color: white;
            font-weight: 600;
            border-radius: 8px;
            padding: 0.6rem 1.4rem;
            font-size: 1rem;
            transition: all 0.3s ease-in-out;
        }

        .stButton>button:hover {
            background-color: #0D47A1;
            transform: scale(1.05);
            box-shadow: 0 0 10px rgba(21,101,192,0.6);
        }

        .title {
            font-size: 3rem;
            font-weight: 800;
            color: #64ffda;
            animation: slideInFade 1s ease-out forwards;
            opacity: 0;
        }

        .subtitle {
            font-size: 1.3rem;
            color: #CCCCCC;
            margin-top: 0.5rem;
            margin-bottom: 2rem;
            animation: slideInFade 1.4s ease-out forwards;
            opacity: 0;
        }

        .features {
            font-size: 1.1rem;
            line-height: 1.8;
            animation: fadeIn 2s ease-in-out forwards;
            opacity: 0;
        }

        h4 {
            margin-top: 3rem;
            color: #90CAF9;
        }

        a {
            color: #64ffda;
            text-decoration: none;
        }

        a:hover {
            text-decoration: underline;
        }

        @keyframes slideInFade {
            0% { opacity: 0; transform: translateY(20px); }
            100% { opacity: 1; transform: translateY(0); }
        }

        @keyframes fadeIn {
            to { opacity: 1; }
        }
    </style>
""", unsafe_allow_html=True)

# ✅ Title and subtitle
st.markdown("<div class='title'>🤖 Welcome to CompeteBot</div>", unsafe_allow_html=True)
st.markdown("<div class='subtitle'>Your AI-powered Competitive Intelligence Assistant</div>", unsafe_allow_html=True)

# ✅ Features
st.markdown("""
<div class='features'>
    <ul>
        <li>📡 Track competitor feature updates</li>
        <li>🧠 Summarize and detect product changes</li>
        <li>📊 Compare across multiple products</li>
        <li>📈 Visualize clean summaries</li>
    </ul>
</div>
""", unsafe_allow_html=True)

# ✅ Explore button
st.markdown("###")
if st.button("Start Exploring 🚀"):
    st.switch_page("pages/dashboard.py")  # Make sure the path matches your file

# ✅ Contact section
st.markdown("### 📬 Contact")
st.markdown("Email: [support@competebot.ai](mailto:support@competebot.ai)")