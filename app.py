import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(layout="wide", page_title="Sales Dashboard")

st.title("📊 Sales Dashboard")

# Sidebar File Upload
uploaded_file = st.sidebar.file_uploader("📁 Upload Your CSV File", type=["csv"])

if uploaded_file:
    df = pd.read_csv(uploaded_file, parse_dates=["Order Date"])

    # Extract Year and Month
    df['Year'] = df['Order Date'].dt.year
    df['Month'] = df['Order Date'].dt.strftime('%b')

    # Sidebar Filters
    st.sidebar.header("🔍 Filter Data")
    year = st.sidebar.selectbox("Select Year", sorted(df['Year'].unique(), reverse=True))
    region = st.sidebar.multiselect("Select Region(s)", options=df['Region'].unique(), default=df['Region'].unique())
    category = st.sidebar.multiselect("Select Category(s)", options=df['Category'].unique(), default=df['Category'].unique())
    sub_category = st.sidebar.multiselect("Select Sub-Category(s)", options=df['Sub-Category'].unique(), default=df['Sub-Category'].unique())

    # Apply Filters
    df = df[df['Year'] == year].reset_index(drop=True)
    df = df[df['Region'].isin(region)]
    df = df[df['Category'].isin(category)]
    df = df[df['Sub-Category'].isin(sub_category)]

    # Dashboard Overview
    st.markdown(f"""
    **Current View:**  
    - 📅 Year: **{year}**  
    - 🌍 Region(s): `{', '.join(region)}`  
    - 📦 Category(s): `{', '.join(category)}`  
    - 🔹 Sub-Category(s): `{', '.join(sub_category)}`
    """)

    # KPI Cards
    col1, col2, col3 = st.columns(3)
    col1.metric("📦 Total Sales", f"${df['Sales'].sum():,.2f}")
    col2.metric("💰 Total Profit", f"${df['Profit'].sum():,.2f}")
    profit_margin = (df['Profit'].sum() / df['Sales'].sum()) * 100
    col3.metric("📊 Profit Margin", f"{profit_margin:.2f}%")

    st.markdown("---")

    # Charts Section
    tab1, tab2, tab3, tab4 = st.tabs(["📈 Overview", "📦 Category Insights", "👤 Customer Analysis", "🌍 Geo Insights"])

    with tab1:
        # Sales over Time
        time_df = df.groupby(df['Order Date'].dt.to_period("M")).agg({'Sales':'sum'}).reset_index()
        time_df['Order Date'] = time_df['Order Date'].dt.to_timestamp()
        fig_time = px.line(time_df, x="Order Date", y="Sales", title="📅 Monthly Sales Trend")
        st.plotly_chart(fig_time, use_container_width=True)

        # Heatmap
        heatmap_data = df.copy()
        pivot_table = heatmap_data.pivot_table(index='Category', columns='Month', values='Sales', aggfunc='sum')
        st.subheader("📊 Monthly Sales Heatmap by Category")
        st.dataframe(pivot_table.style.background_gradient(cmap='Blues'))

    with tab2:
        # Sales by Category
        category_sales = df.groupby("Category")["Sales"].sum().reset_index().sort_values(by="Sales")
        fig_category = px.bar(category_sales, x="Sales", y="Category", orientation="h", title="Sales by Category", text_auto=True)
        st.plotly_chart(fig_category, use_container_width=True)

        # Sub-Category Sales
        subcat_sales = df.groupby("Sub-Category")["Sales"].sum().reset_index().sort_values(by="Sales")
        fig_subcat = px.bar(subcat_sales, x="Sales", y="Sub-Category", orientation="h", title="Sales by Sub-Category", text_auto=True)
        st.plotly_chart(fig_subcat, use_container_width=True)

    with tab3:
        # Top 5 Customers
        st.subheader("🏅 Top 5 Customers by Sales")
        top_sales_customers = df.groupby("Customer Name")["Sales"].sum().reset_index().sort_values(by="Sales", ascending=False).head(5)
        fig_top_sales = px.bar(top_sales_customers, x="Sales", y="Customer Name", orientation='h', title="Top Customers by Sales", text_auto=True)
        st.plotly_chart(fig_top_sales, use_container_width=True)

        # Customer Segmentation
        customer_data = df.groupby("Customer Name")["Sales"].sum().reset_index()
        customer_data['Segment'] = pd.qcut(customer_data['Sales'], q=3, labels=['Low', 'Medium', 'High'])
        fig_seg = px.pie(customer_data, names='Segment', title='Customer Segments by Sales Volume')
        st.plotly_chart(fig_seg, use_container_width=True)

    with tab4:
        # Sales by Region
        region_sales = df.groupby("Region")["Sales"].sum().reset_index()
        fig_region = px.pie(region_sales, values="Sales", names="Region", title="Sales Distribution by Region")
        st.plotly_chart(fig_region, use_container_width=True)

    st.markdown("---")

    # Data Preview with Year Note
    with st.expander("📋 Preview Data (Filtered by Year)"):
        st.markdown(f"ℹ️ Showing first 10 rows for **year {year}** with current filters applied.")
        st.dataframe(df.head(10))
        st.download_button("📥 Download Filtered Data", data=df.to_csv(index=False), file_name="filtered_data.csv")

else:
    st.warning("📎 Please upload a CSV file to continue.")
