import streamlit as st
import pandas as pd
import plotly.express as px

# Set Streamlit page configuration
st.set_page_config(page_title="Global Superstore Dashboard", layout="wide")

# Title
st.title("📊 Global Superstore Sales Dashboard")

# Load and clean dataset
@st.cache_data
def load_data():
    df = pd.read_csv("Global_Superstore.csv", encoding='latin1')
    
    # Convert dates
    df['Order Date'] = pd.to_datetime(df['Order Date'], errors='coerce')
    df['Year'] = df['Order Date'].dt.year
    
    # Drop rows with missing critical values
    df = df.dropna(subset=['Sales', 'Profit', 'Customer Name', 'Category', 'Region', 'Sub-Category', 'Order Date'])
    
    return df

df = load_data()

# Sidebar Filters
st.sidebar.header("🔍 Filter Data")
selected_region = st.sidebar.multiselect("Select Region", sorted(df["Region"].unique()))
selected_category = st.sidebar.multiselect("Select Category", sorted(df["Category"].unique()))
selected_subcat = st.sidebar.multiselect("Select Sub-Category", sorted(df["Sub-Category"].unique()))
selected_year = st.sidebar.multiselect("Select Year", sorted(df["Year"].unique()))

# Apply filters
if selected_region:
    df = df[df["Region"].isin(selected_region)]
if selected_category:
    df = df[df["Category"].isin(selected_category)]
if selected_subcat:
    df = df[df["Sub-Category"].isin(selected_subcat)]
if selected_year:
    df = df[df["Year"].isin(selected_year)]

# Data Preview
st.subheader("🗂️ Data Preview")
st.dataframe(df.head(10))

# KPIs
st.subheader("📌 Key Performance Indicators")
col1, col2, col3 = st.columns(3)
col1.metric("Total Sales", f"${df['Sales'].sum():,.0f}")
col2.metric("Total Profit", f"${df['Profit'].sum():,.0f}")
col3.metric("Total Orders", f"{df.shape[0]:,}")

# Sales by Category
st.subheader("📦 Sales by Category")
fig1 = px.bar(
    df.groupby("Category")["Sales"].sum().reset_index(),
    x="Category",
    y="Sales",
    color="Category",
    hover_data=["Sales"],
    title="Total Sales by Category"
)
st.plotly_chart(fig1, use_container_width=True)

# Sales by Region
st.subheader("🌍 Sales by Region")
fig2 = px.pie(
    df,
    values="Sales",
    names="Region",
    title="Sales Distribution by Region",
    hole=0.4
)
st.plotly_chart(fig2, use_container_width=True)

# Monthly Sales Trend
st.subheader("📈 Monthly Sales Trend")
df_month = df.copy()
df_month['Month'] = df_month['Order Date'].dt.to_period("M").astype(str)
df_time = df_month.groupby("Month")["Sales"].sum().reset_index()
fig3 = px.line(
    df_time,
    x="Month",
    y="Sales",
    title="Sales Trend Over Time",
    markers=True,
    hover_data=["Sales"]
)
st.plotly_chart(fig3, use_container_width=True)

# Top 5 Customers by Sales
st.subheader("🏆 Top 5 Customers by Sales")
top_customers_sales = df.groupby("Customer Name")["Sales"].sum().reset_index().sort_values(by="Sales", ascending=False).head(5)
fig4 = px.bar(
    top_customers_sales,
    x="Customer Name",
    y="Sales",
    color="Sales",
    title="Top 5 Customers by Sales",
    hover_data=["Sales"]
)
st.plotly_chart(fig4, use_container_width=True)

# Top 10 Customers by Profit
st.subheader("💰 Top 10 Customers by Profit")
top_customers_profit = df.groupby("Customer Name")["Profit"].sum().reset_index().sort_values(by="Profit", ascending=False).head(10)
fig5 = px.bar(
    top_customers_profit,
    x="Customer Name",
    y="Profit",
    color="Profit",
    title="Top 10 Customers by Profit",
    hover_data=["Profit"]
)
st.plotly_chart(fig5, use_container_width=True)

st.markdown("---")
st.caption("Made with ❤️ by Muhammad Zain Mushtaq")
