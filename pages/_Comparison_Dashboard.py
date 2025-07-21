import streamlit as st
import plotly.graph_objects as go
from pathlib import Path

st.set_page_config(layout="wide")
st.title("📊 Competitor Comparison Dashboard")

# Sample data
weeks = ["Week 1", "Week 2", "Week 3"]
notion = [3, 5, 7]
linear = [2, 4, 6]
height = [1, 3, 6]
yourstartup = [1, 2, 3]

fig = go.Figure()
fig.add_trace(go.Scatter(x=weeks, y=notion, mode='lines+markers', name='Notion'))
fig.add_trace(go.Scatter(x=weeks, y=linear, mode='lines+markers', name='Linear'))
fig.add_trace(go.Scatter(x=weeks, y=height, mode='lines+markers', name='Height'))
fig.add_trace(go.Scatter(x=weeks, y=yourstartup, mode='lines+markers', name='YourStartup'))

fig.update_layout(title="📈 Feature Progress Over Time", xaxis_title="Week", yaxis_title="Features Released")
st.plotly_chart(fig, use_container_width=True)

st.markdown("## 🤖 AI Suggestion")
if yourstartup[-1] < height[-1]:
    st.warning("YourStartup is lagging behind in feature delivery compared to Notion and Height.")
    st.info("💡 Focus on faster release cycles, better integrations, and AI-powered enhancements to compete.")

st.markdown("## 🗂 Weekly Summaries by Company")
base_dir = Path("data")
competitors = sorted([d for d in base_dir.iterdir() if d.is_dir()])
tabs = st.tabs([comp.name.capitalize() for comp in competitors])

for tab, comp in zip(tabs, competitors):
    with tab:
        st.subheader(f"📌 {comp.name.capitalize()} Updates")
        summary_file = comp / "summary.txt"
        if summary_file.exists():
            with open(summary_file, "r", encoding="utf-8") as f:
                st.code(f.read(), language="markdown")
        else:
            st.warning("No summary available.")