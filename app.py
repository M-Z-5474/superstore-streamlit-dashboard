import streamlit as st
import pandas as pd
import plotly.express as px
import io

st.set_page_config(page_title="Global Superstore Dashboard", layout="wide")

# Title
st.title("📊 Global Superstore Dashboard")

# Instructions
st.info(
    "Use the filters in the sidebar to explore sales, profit, and customer trends. "
    "Select at least one Region, Category, and Year to display the dashboard. "
    "The charts and KPIs will update based on your selections."
)

# Load data
@st.cache_data
def load_data():
    df = pd.read_csv("Global_Superstore.csv", encoding='latin1')
    df['Order Date'] = pd.to_datetime(df['Order Date'], errors='coerce')
    df.dropna(subset=['Order Date'], inplace=True)
    df['Year'] = df['Order Date'].dt.year
    return df

df = load_data()

# Sidebar filters
st.sidebar.header("Filter Options")
selected_region = st.sidebar.multiselect("Select Region", sorted(df["Region"].dropna().unique()))
selected_category = st.sidebar.multiselect("Select Category", sorted(df["Category"].dropna().unique()))
selected_subcat = st.sidebar.multiselect("Select Sub-Category", sorted(df["Sub-Category"].dropna().unique()))
selected_year = st.sidebar.multiselect("Select Year", sorted(df["Year"].dropna().unique()))

# Apply filters
if selected_region:
    df = df[df["Region"].isin(selected_region)]
if selected_category:
    df = df[df["Category"].isin(selected_category)]
if selected_subcat:
    df = df[df["Sub-Category"].isin(selected_subcat)]
if selected_year:
    df = df[df["Year"].isin(selected_year)]

# Stop if no data
if df.empty:
    st.warning("⚠️ No data available for the selected filters. Please adjust your selections.")
    st.stop()

# KPIs
total_sales = df['Sales'].sum()
total_profit = df['Profit'].sum()
total_orders = df['Order ID'].nunique()
total_customers = df['Customer ID'].nunique()

kpi1, kpi2, kpi3, kpi4 = st.columns(4)
kpi1.metric("Total Sales", f"${total_sales:,.0f}")
kpi2.metric("Total Profit", f"${total_profit:,.0f}")
kpi3.metric("Total Orders", total_orders)
kpi4.metric("Total Customers", total_customers)

# Sales by Category
fig1 = px.bar(
    df.groupby("Category")["Sales"].sum().reset_index(),
    x="Category",
    y="Sales",
    color="Category",
    title="💰 Sales by Category"
)
st.plotly_chart(fig1, use_container_width=True)

# Profit by Region
fig2 = px.pie(
    df.groupby("Region")["Profit"].sum().reset_index(),
    names="Region",
    values="Profit",
    title="🏆 Profit Distribution by Region",
    hole=0.4
)
st.plotly_chart(fig2, use_container_width=True)

# Monthly Sales Trend
monthly_sales = df.resample("M", on="Order Date")["Sales"].sum().reset_index()
fig3 = px.line(
    monthly_sales,
    x="Order Date",
    y="Sales",
    title="📈 Monthly Sales Trend",
    markers=True
)
st.plotly_chart(fig3, use_container_width=True)

# Data preview
with st.expander("🔍 View Filtered Data"):
    st.dataframe(df)

# Download filtered data
@st.cache_data
def convert_df(df):
    return df.to_csv(index=False).encode('utf-8')

csv = convert_df(df)
st.download_button(
    label="⬇️ Download Filtered Data as CSV",
    data=csv,
    file_name='filtered_superstore_data.csv',
    mime='text/csv'
)
