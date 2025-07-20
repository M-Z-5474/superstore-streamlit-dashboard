
## 📊 Global Superstore Sales Dashboard

An interactive Streamlit web app to analyze and visualize Global Superstore sales data across various dimensions — including category, region, customer segments, and time trends.

---

### 🚀 Features

* 🔍 **Interactive Sidebar Filters**: Region, Category, Sub-Category, and Year
* 📌 **Key Metrics Dashboard**:

  * Total Sales
  * Total Profit
  * Total Orders
  * Unique Customers
  * 📈 Profit Margin (%)
* 📦 **Sales by Category** (Bar Chart)
* 💰 **Profit Distribution by Region** (Pie Chart)
* 📈 **Monthly Sales Trend** (Line Chart)
* 🧾 **Product-Level Sales Analysis** (Top 10 Products)
* 🏆 **Top Customers by Profit**
* 🥇 **Top Customers by Sales**
* 🧮 **Customer Segmentation**:

  * Based on Sales (Low, Medium, High)
  * Visualized using a pie chart
* 📊 **Monthly Sales Heatmap** by Product Category
* 🌍 **City-Wise Sales Distribution** (Geographic Map)
* 📋 **Downloadable Filtered Data**
* ❤️ Designed with an intuitive, professional UI

---

### 📂 Project Structure

```
📁 Global_Superstore_Dashboard/
├── 📄 app.py                 ← Main Streamlit dashboard code
├── 📄 Global_Superstore.csv  ← Dataset (input file)
├── 📄 README.md              ← Project documentation
```

---

### 📦 Requirements

Create a virtual environment and install dependencies:

```bash
pip install -r requirements.txt
```

If `requirements.txt` isn't available, install manually:

```bash
pip install streamlit pandas plotly
```

---

### ▶️ How to Run

1. **Clone this repository** or copy the project files.
2. Place the `Global_Superstore.csv` file in the same directory as `app.py`.
3. Run the Streamlit app:

```bash
streamlit run app.py
```

---

### 📈 Data Info

* **Dataset**: Global Superstore Sales (Sample data)
* **Columns Used**:

  * Sales, Profit, Order Date, Category, Sub-Category, Region, City, State, Country, Customer Name, Product Name

---

### 📌 Notes

* Ensure the `Order Date` column is correctly parsed as datetime.
* You can customize the dashboard further by using `st.tabs()` or splitting into multipage layout for enhanced UX.
* CSV download is available for filtered data.

---

### 📸 Dashboard Preview

You can upload screenshots or demo gifs here to showcase different sections of the dashboard.

---

### 👨‍💻 Developed By

**Muhammad Zain Mushtaq**
📧 \[m.zainmushtaq74@gmail.com)]
🔗 \[(https://github.com/M-Z-5474]

---

