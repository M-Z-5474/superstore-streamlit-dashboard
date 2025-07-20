import streamlit as st
import pandas as pd
import plotly.express as px

# Page configuration
st.set_page_config(page_title="Global Superstore Dashboard", layout="wide")
st.title("📊 Global Superstore Sales Dashboard")

# File uploader for custom data
uploaded_file = st.sidebar.file_uploader("📂 Upload Your CSV", type=["csv"])
if uploaded_file:
    df = pd.read_csv(uploaded_file)
    df['Order Date'] = pd.to_datetime(df['Order Date'], errors='coerce')
    df['Year'] = df['Order Date'].dt.year
else:
    @st.cache_data
    def load_data():
        df = pd.read_csv("Global_Superstore.csv", encoding='latin1')
        df['Order Date'] = pd.to_datetime(df['Order Date'], errors='coerce')
        df['Year'] = df['Order Date'].dt.year
        return df

    df = load_data()

# Sidebar filters
st.sidebar.header("🔍 Filters")
region = st.sidebar.multiselect("Select Region", df["Region"].dropna().unique())
category = st.sidebar.multiselect("Select Category", df["Category"].dropna().unique())
sub_category = st.sidebar.multiselect("Select Sub-Category", df["Sub-Category"].dropna().unique())
year = st.sidebar.selectbox("Select Year", sorted(df['Year'].dropna().unique()), index=0)

# Apply filters
if region:
    df = df[df['Region'].isin(region)]
if category:
    df = df[df['Category'].isin(category)]
if sub_category:
    df = df[df['Sub-Category'].isin(sub_category)]
df = df[df['Year'] == year]

# Tabs for multi-section layout
tab1, tab2, tab3, tab4 = st.tabs(["📌 Overview", "📦 Category Insights", "👥 Customer Analysis", "🌍 Geo Insights"])

# --- Overview Tab ---
with tab1:
    st.subheader("📌 Key Metrics")
    k1, k2, k3, k4, k5 = st.columns(5)
    k1.metric("Total Sales", f"${df['Sales'].sum():,.0f}")
    k2.metric("Total Profit", f"${df['Profit'].sum():,.0f}")
    k3.metric("Total Orders", f"{df.shape[0]:,}")
    k4.metric("Total Customers", f"{df['Customer Name'].nunique():,}")
    profit_margin = (df['Profit'].sum() / df['Sales'].sum()) * 100
    k5.metric("📊 Profit Margin", f"{profit_margin:.2f}%")

    with st.expander("📋 Preview Filtered Data"):
        st.dataframe(df.head(10))
        st.download_button("Download CSV", data=df.to_csv(index=False), file_name="filtered_data.csv")

    st.subheader("📈 Monthly Sales Trend")
    df_time = df.groupby(df['Order Date'].dt.to_period("M"))['Sales'].sum().reset_index()
    df_time['Order Date'] = df_time['Order Date'].astype(str)
    fig3 = px.line(df_time, x="Order Date", y="Sales", markers=True)
    st.plotly_chart(fig3, use_container_width=True)

# --- Category Insights Tab ---
with tab2:
    st.subheader("📦 Sales by Category")
    fig1 = px.bar(df.groupby("Category")['Sales'].sum().reset_index(),
                  x="Category", y="Sales", color="Category",
                  title="Sales by Category", text_auto=True)
    st.plotly_chart(fig1, use_container_width=True)

    st.subheader("📊 Monthly Sales Heatmap by Category")
    heatmap_data = df.copy()
    heatmap_data['Month'] = heatmap_data['Order Date'].dt.strftime('%b')
    pivot_table = heatmap_data.pivot_table(index='Category', columns='Month', values='Sales', aggfunc='sum')
    st.dataframe(pivot_table.style.background_gradient(cmap='Blues'))

# --- Customer Analysis Tab ---
with tab3:
    st.subheader("🏆 Top 10 Customers by Profit")
    top_profit_customers = df.groupby("Customer Name")["Profit"].sum().reset_index().sort_values(by="Profit", ascending=False).head(10)
    fig5 = px.bar(top_profit_customers, x="Profit", y="Customer Name", orientation='h', title="Top Customers by Profit", text_auto=True)
    st.plotly_chart(fig5, use_container_width=True)

    st.subheader("🏅 Top 5 Customers by Sales")
    top_sales_customers = df.groupby("Customer Name")["Sales"].sum().reset_index().sort_values(by="Sales", ascending=False).head(5)
    fig_top_sales = px.bar(top_sales_customers, x="Sales", y="Customer Name", orientation='h', title="Top Customers by Sales", text_auto=True)
    st.plotly_chart(fig_top_sales, use_container_width=True)

    st.subheader("👤 Customer Segments by Sales Volume")
    customer_data = df.groupby("Customer Name")["Sales"].sum().reset_index()
    customer_data['Segment'] = pd.qcut(customer_data['Sales'], q=3, labels=['Low', 'Medium', 'High'])
    fig_seg = px.pie(customer_data, names='Segment', title='Customer Segments by Sales Volume')
    st.plotly_chart(fig_seg, use_container_width=True)

# --- Geo Insights Tab ---
with tab4:
    st.subheader("💰 Profit Distribution by Region")
    fig2 = px.pie(df, values="Profit", names="Region",
                  title="Profit by Region", hole=0.3)
    st.plotly_chart(fig2, use_container_width=True)

    st.subheader("🌍 City-wise Sales Distribution")
    city_sales = df.groupby(["City", "State", "Country"])["Sales"].sum().reset_index().sort_values(by="Sales", ascending=False).head(50)
    city_sales['City Label'] = city_sales['City'] + ", " + city_sales['State']
    fig6 = px.scatter_geo(city_sales, locations="Country", locationmode="country names",
                          hover_name="City Label", size="Sales", title="Top Cities by Sales")
    st.plotly_chart(fig6, use_container_width=True)

st.markdown("---")
st.caption("Made with ❤️ by Muhammad Zain Mushtaq")
