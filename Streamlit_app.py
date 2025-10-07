# app.py (debug-ready)
import pandas as pd
from pathlib import Path
import streamlit as st
import plotly.express as px

st.set_page_config(page_title="IBM HR — Attrition Dashboard", page_icon="📊", layout="wide")
st.title("IBM Employee Attrition Dashboard")

CSV_PATH = Path(r"D:\UM\IBM-HR-Analytics-Employee-Attrition-Performance\WA_Fn-UseC_-HR-Employee-Attrition.csv")

st.sidebar.write("**CSV Path:**", str(CSV_PATH))

@st.cache_data(show_spinner=False)
def load_data(p: Path):
    if not p.exists():
        raise FileNotFoundError(f"CSV not found at:\n{p}")
    df = pd.read_csv(p)
    df['Attrition'] = df['Attrition'].astype(str).str.strip()
    df['AttritionFlag'] = (df['Attrition'].str.lower() == 'yes').astype(int)
    return df

try:
    df = load_data(CSV_PATH)
    st.success(f"Loaded: {CSV_PATH.name}  |  shape={df.shape}")
    with st.expander("Preview data (first 5 rows)"):
        st.dataframe(df.head())
except Exception as e:
    st.error("Failed to load CSV. See details below.")
    st.exception(e)
    st.stop()

# Quick KPIs (safe defaults)
total_emp = int(df.shape[0])
attr_rate = float(df['AttritionFlag'].mean()*100) if total_emp else 0.0
avg_tenure = float(df.get('YearsAtCompany', pd.Series([0])).mean())
avg_income = float(df.get('MonthlyIncome', pd.Series([0])).mean())

c1,c2,c3,c4 = st.columns(4)
c1.metric("Employees", f"{total_emp:,}")
c2.metric("Attrition Rate", f"{attr_rate:.2f}%")
c3.metric("Avg Tenure (yrs)", f"{avg_tenure:.1f}")
c4.metric("Avg Monthly Income", f"₹{avg_income:,.0f}")

st.markdown("---")

# Safe plots: each checks the column first
def safe_hist(col, title):
    if col in df.columns:
        fig = px.histogram(df, x=col, nbins=30, height=320)
        fig.update_layout(margin=dict(l=10,r=10,t=30,b=10), title=title)
        st.plotly_chart(fig, use_container_width=True)
    else:
        st.info(f"Column not found: **{col}**")

def safe_pie(col, title):
    if col in df.columns:
        data = df[col].value_counts().reset_index()
        data.columns = [col, "Count"]
        fig = px.pie(data, values="Count", names=col, hole=0.55, height=320, title=title)
        fig.update_layout(margin=dict(l=10,r=10,t=30,b=10))
        st.plotly_chart(fig, use_container_width=True)
    else:
        st.info(f"Column not found: **{col}**")

def rate_by(col):
    if col not in df.columns:
        st.info(f"Column not found: **{col}**")
        return
    t = df.groupby(col)['AttritionFlag'].agg(['mean','count']).reset_index()
    t['AttritionRate(%)'] = (t['mean']*100).round(2)
    t.rename(columns={'count':'Employees'}, inplace=True)
    fig = px.bar(t.sort_values('AttritionRate(%)', ascending=False),
                 x=col, y='AttritionRate(%)', text='AttritionRate(%)', height=360,
                 title=f'Attrition Rate by {col}')
    fig.update_traces(textposition="outside")
    fig.update_layout(margin=dict(l=10,r=10,t=30,b=10), yaxis_title="Attrition Rate (%)")
    st.plotly_chart(fig, use_container_width=True)

r1c1, r1c2, r1c3 = st.columns(3)
with r1c1: safe_hist("Age", "Employees by Age")
with r1c2: safe_pie("Gender", "Employees by Gender")
with r1c3: safe_hist("HourlyRate", "Employees by Hourly Rate")

r2c1, r2c2, r2c3 = st.columns(3)
with r2c1: rate_by("JobRole")
with r2c2: rate_by("EducationField")
with r2c3: safe_hist("MonthlyIncome", "Distribution: Monthly Income")

r3c1, r3c2 = st.columns(2)
with r3c1: rate_by("Department")
with r3c2: rate_by("BusinessTravel")

st.markdown("---")
st.subheader("Conclusion")
st.write(
    f"- **Attrition ~ {attr_rate:.2f}%**.  \n"
    "- Younger employees and certain roles show higher attrition.  \n"
    "- Lower income correlates with attrition; consider compensation & growth."
)
