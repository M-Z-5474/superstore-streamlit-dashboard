import streamlit as st
import pandas as pd
import plotly.express as px

# Set Streamlit page config
st.set_page_config(page_title="Global Superstore Dashboard", layout="wide")

# Title
st.title("📊 Global Superstore Sales Dashboard")

# Upload or read dataset
@st.cache_data
def load_data():
    df = pd.read_csv("Global_Superstore.csv", encoding='latin1')
    return df

df = load_data()

# Sidebar filters
st.sidebar.header("🔍 Filters")
selected_country = st.sidebar.multiselect("Select Country", df["Country"].unique())
if selected_country:
    df = df[df["Country"].isin(selected_country)]

# Show data sample
st.subheader("🗂️ Data Preview")
st.dataframe(df.head())

# KPIs
st.subheader("📌 Key Metrics")
col1, col2, col3 = st.columns(3)
col1.metric("Total Sales", f"${df['Sales'].sum():,.0f}")
col2.metric("Total Profit", f"${df['Profit'].sum():,.0f}")
col3.metric("Total Orders", f"{df.shape[0]:,}")

# Sales by Category
st.subheader("📦 Sales by Category")
fig1 = px.bar(df.groupby("Category")["Sales"].sum().reset_index(), x="Category", y="Sales", color="Category")
st.plotly_chart(fig1, use_container_width=True)

# Sales by Region
st.subheader("🌍 Sales by Region")
fig2 = px.pie(df, values="Sales", names="Region", title="Sales Distribution by Region")
st.plotly_chart(fig2, use_container_width=True)

# Line chart over time
st.subheader("📈 Sales Over Time")
df['Order Date'] = pd.to_datetime(df['Order Date'], errors='coerce')
df_time = df.groupby(df['Order Date'].dt.to_period("M"))["Sales"].sum().reset_index()
df_time['Order Date'] = df_time['Order Date'].astype(str)
fig3 = px.line(df_time, x="Order Date", y="Sales", title="Monthly Sales Trend")
st.plotly_chart(fig3, use_container_width=True)

st.markdown("---")
st.caption("Made with ❤️ by Muhammad Zain Mushtaq")

