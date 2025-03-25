
import streamlit as st
import pandas as pd

st.set_page_config(page_title="StratAI - Early Warning & Social Impact", layout="wide")

st.title("📊 StratAI Early Warning & Social Risk Dashboard")

uploaded_file = st.file_uploader("Upload Student CSV", type="csv")
if uploaded_file:
    df = pd.read_csv(uploaded_file)

    if "GPA" in df.columns:
        st.subheader("🧠 Early Warning Score")
        df['Score'] = (df['GPA'] / 4.0) * 100 * 0.35 + df['Attendance Rate'] * 0.25 + df['Engagement Score'] * 0.20 +                       df['Financial Risk Flag'].apply(lambda x: 0 if x else 100) * 0.10 +                       df['First-Gen Flag'].apply(lambda x: 60 if x else 100) * 0.10
        df['RAG Status'] = df['Score'].apply(lambda x: 'Green' if x >= 80 else 'Amber' if x >= 60 else 'Red')
        st.dataframe(df)

    elif "Peer Belonging" in df.columns:
        st.subheader("🧍 Social Environment Score")
        df['Score'] = df['Peer Belonging'] * 0.25 + (100 - df['Bullying Reports']) * 0.20 + df['Adult Ally'] * 0.15 +                       df['Activity Participation'] * 0.15 + df['Attendance Score'] * 0.15 +                       (100 - df['Disciplinary Referrals']) * 0.10
        df['RAG Status'] = df['Score'].apply(lambda x: 'Green' if x >= 85 else 'Amber' if x >= 70 else 'Red')
        st.dataframe(df)

    st.download_button("Download Scored CSV", df.to_csv(index=False), file_name="scored_output.csv", mime="text/csv")
