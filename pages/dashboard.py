import streamlit as st
from pathlib import Path

# Set up the page
st.set_page_config(page_title="Competitor Tracker", layout="wide")
st.markdown("<h1 style='text-align: center;'>🕵 Competitor Feature Tracker</h1>", unsafe_allow_html=True)

# Sidebar: Fake login section
with st.sidebar:
    st.title("👤 User Login")
    username = st.text_input("Username")
    password = st.text_input("Password", type="password")
    if st.button("Login"):
        st.success(f"Welcome, {username}!")

    st.markdown("---")
    st.header("📤 Upload Update")
    uploaded_file = st.file_uploader("Upload new changelog (.txt)", type="txt")
    if uploaded_file:
        st.info("File uploaded (just UI – not saving).")

# Base directory setup
base_dir = Path("data")
competitors = sorted([d for d in base_dir.iterdir() if d.is_dir()])

# UI Tabs for each company
tabs = st.tabs([comp.name.capitalize() for comp in competitors])

for tab, comp in zip(tabs, competitors):
    with tab:
        st.subheader(f"📌 {comp.name.capitalize()} Updates")

        col1, col2 = st.columns([2, 1])

        # Summary view
        summary_file = comp / "summary.txt"
        if summary_file.exists():
            with open(summary_file, "r", encoding="utf-8") as f:
                col1.markdown("### 📄 Weekly Summary")
                col1.code(f.read(), language="markdown")
        else:
            col1.warning("No summary found.")

        # Diff view
        diff_file = comp / "diff_output.txt"
        if diff_file.exists():
            with open(diff_file, "r", encoding="utf-8") as f:
                col2.markdown("### 🔍 Diff Output")
                col2.text(f.read())
        else:
            col2.warning("No diff output found.")

# Optional: Footer
st.markdown("---")
st.markdown("<center>Made with ❤ by Our Startup Team</center>", unsafe_allow_html=True)
st.header(f"📌 {comp.name.capitalize()}")

summary_file = comp / "summary.txt"
diff_file = comp / "diff_output.txt"

if summary_file.exists():
        with open(summary_file, "r", encoding="utf-8") as f:
            st.subheader("📄 Weekly Summary")
            st.code(f.read(), language="markdown")
else:
        st.warning("No summary found.")

if diff_file.exists():
        with open(diff_file, "r", encoding="utf-8") as f:
            st.subheader("🔍 Diff Output")
            st.text(f.read())
import plotly.graph_objects as go

# 🚀 Feature count per company (just example data)
feature_count = {
    "Notion": 3,
    "Linear": 3,
    "Height": 3,
    "YourStartup": 3  # You can make it 2 or 4 depending on actual summary count
}

# 📊 Bar chart of feature count
st.markdown("## 📊 Feature Release Count")
st.bar_chart(feature_count)

# 📈 Radar chart categories
categories = ["AI/ML", "Integrations", "UI/UX", "Automation", "Mobile", "Performance"]

# Fake scoring data (scale of 0–5)
data = {
    "Notion": [4, 5, 4, 2, 4, 3],
    "Linear": [2, 4, 3, 1, 4, 3],
    "Height": [2, 3, 4, 4, 4, 3],
    "YourStartup": [5, 2, 2, 3, 3, 3]
}

fig = go.Figure()
for company, scores in data.items():
    fig.add_trace(go.Scatterpolar(
        r=scores,
        theta=categories,
        fill='toself',
        name=company
    ))

fig.update_layout(
    polar=dict(radialaxis=dict(visible=True, range=[0, 5])),
    showlegend=True
)

st.markdown("## 🕸 Feature Area Radar Chart")
st.plotly_chart(fig, use_container_width=True)

# 🧠 Auto-insight logic (simple rule-based for now)
st.markdown("## 🤖 AI Insight Summary")

weak_areas = []
if data["YourStartup"][1] < 3:
    weak_areas.append("Integrations")
if data["YourStartup"][2] < 3:
    weak_areas.append("UI/UX")
if data["YourStartup"][3] < 3:
    weak_areas.append("Automation")

if weak_areas:
    st.error(f"⚠ YourStartup is falling behind in: {', '.join(weak_areas)}")
    st.info("💡 To stay competitive, focus on enhancing these areas and monitor how Notion and Height lead with frequent improvements.")
else:
    st.success("✅ YourStartup is on par or ahead in all key areas!")