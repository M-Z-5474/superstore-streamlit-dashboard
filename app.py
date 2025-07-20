import streamlit as st
import pandas as pd
import plotly.express as px

# Load data
df = pd.read_csv("Global_Superstore.csv", encoding='latin1')

# Data preprocessing
df['Order Date'] = pd.to_datetime(df['Order Date'], errors='coerce')
df['Year'] = df['Order Date'].dt.year
df.dropna(subset=['Order Date', 'Sales', 'Profit', 'Customer Name'], inplace=True)

# Sidebar filters
st.sidebar.header("Filter Options")
years = sorted(df['Year'].dropna().unique())
year_filter = st.sidebar.selectbox("Select Year", years)

regions = st.sidebar.multiselect("Select Region", df['Region'].unique(), default=df['Region'].unique())
categories = st.sidebar.multiselect("Select Category", df['Category'].unique(), default=df['Category'].unique())
sub_categories = st.sidebar.multiselect("Select Sub-Category", df['Sub-Category'].unique(), default=df['Sub-Category'].unique())
segments = st.sidebar.multiselect("Select Segment", df['Segment'].unique(), default=df['Segment'].unique())

# Apply filters
filtered_df = df[
    (df['Year'] == year_filter) &
    (df['Region'].isin(regions)) &
    (df['Category'].isin(categories)) &
    (df['Sub-Category'].isin(sub_categories)) &
    (df['Segment'].isin(segments))
]

st.title("📊 Global Superstore Dashboard")

# KPIs
total_sales = filtered_df['Sales'].sum()
total_profit = filtered_df['Profit'].sum()
total_orders = filtered_df['Order ID'].nunique()

col1, col2, col3 = st.columns(3)
col1.metric("💰 Total Sales", f"${total_sales:,.0f}")
col2.metric("📈 Total Profit", f"${total_profit:,.0f}")
col3.metric("🧾 Total Orders", f"{total_orders}")

# Sales by Category
fig_cat = px.bar(filtered_df.groupby('Category')['Sales'].sum().reset_index(),
                 x='Category', y='Sales', title="Sales by Category", text_auto='.2s')
st.plotly_chart(fig_cat, use_container_width=True)

# Sales by Region
fig_region = px.pie(filtered_df, names='Region', values='Sales', title="Sales by Region", hole=0.4)
st.plotly_chart(fig_region, use_container_width=True)

# Monthly Sales Trend
monthly_sales = filtered_df.groupby(filtered_df['Order Date'].dt.to_period('M')).sum(numeric_only=True).reset_index()
monthly_sales['Order Date'] = monthly_sales['Order Date'].astype(str)
fig_time = px.line(monthly_sales, x='Order Date', y='Sales', title='Monthly Sales Trend')
st.plotly_chart(fig_time, use_container_width=True)

# Top Customers by Sales
top_customers = filtered_df.groupby('Customer Name')['Sales'].sum().nlargest(5).reset_index()
fig_top_sales = px.bar(top_customers, x='Customer Name', y='Sales', title="Top 5 Customers by Sales", text_auto='.2s')
st.plotly_chart(fig_top_sales, use_container_width=True)

# Top Customers by Profit
top_profit_customers = filtered_df.groupby('Customer Name')['Profit'].sum().nlargest(10).reset_index()
fig_top_profit = px.bar(top_profit_customers, x='Customer Name', y='Profit', title="Top 10 Customers by Profit", text_auto='.2s')
st.plotly_chart(fig_top_profit, use_container_width=True)

# Footer
st.markdown("---")
st.markdown("🚀 Built with Streamlit | By Muhammad Zain Mushtaq")
