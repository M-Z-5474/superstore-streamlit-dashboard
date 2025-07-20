

# 📦 Global Superstore Dataset

An extensive international retail dataset containing over **51,000 sales transactions** across **multiple countries, markets, and customer segments**. This dataset is widely used in business intelligence, sales forecasting, and dashboard development projects.

---

## 📊 Dataset Overview

| Attribute   | Details                                                                                        |
| ----------- | ---------------------------------------------------------------------------------------------- |
| 📈 Rows     | 51,290                                                                                         |
| 📂 Columns  | 24                                                                                             |
| 📁 Format   | CSV                                                                                            |
| 🌐 Coverage | Global: US, EU, APAC, Africa...                                                                |
| 🧾 Source   | [Kaggle]([https://www.kaggle.com/datasets/apoorvaappz/global-super-store-datase](https://www.kaggle.com/datasets/apoorvaappz/global-super-store-dataset)t) |

---

## 🧮 Schema (Column Descriptions)

| Column Name      | Description                                                   |
| ---------------- | ------------------------------------------------------------- |
| `Row ID`         | Internal row identifier (not useful analytically)             |
| `Order ID`       | Unique ID for each order                                      |
| `Order Date`     | Date the order was placed *(parsed as datetime)*              |
| `Ship Date`      | Shipping date of the order *(parsed as datetime)*             |
| `Ship Mode`      | Shipping method: Same Day, First Class, etc.                  |
| `Customer ID`    | Unique identifier for the customer                            |
| `Customer Name`  | Full name of the customer                                     |
| `Segment`        | Customer segment: Consumer, Corporate, Home Office            |
| `City`           | Customer's city                                               |
| `State`          | Customer's state/province                                     |
| `Country`        | Country of the customer                                       |
| `Postal Code`    | Postal code *(many values missing — optional use)*            |
| `Market`         | Global market region (e.g., EU, APAC, Africa, US)             |
| `Region`         | Sub-region within market (e.g., West, Central)                |
| `Product ID`     | Unique product identifier                                     |
| `Category`       | Main product category: Furniture, Technology, Office Supplies |
| `Sub-Category`   | Subcategory: Binders, Phones, Chairs, etc.                    |
| `Product Name`   | Name and description of the product                           |
| `Sales`          | Sales value in local currency (numeric)                       |
| `Quantity`       | Number of units sold                                          |
| `Discount`       | Discount applied to the order                                 |
| `Profit`         | Profit margin from the sale                                   |
| `Shipping Cost`  | Shipping cost incurred on the order                           |
| `Order Priority` | Priority status: Critical, High, Medium, Low                  |

---

## 🧹 Cleaning Notes

* ✔️ Converted `Order Date` and `Ship Date` to `datetime` using `dayfirst=True` to ensure format accuracy
* ✔️ Cleaned and renamed columns to follow Python naming conventions (e.g., `Order_ID`, `Product_Name`)
* ✔️ Handled missing `Postal Code` values (`~80%` are null – safe to drop or exclude)
* ✔️ Verified numerical columns (`Sales`, `Profit`, `Shipping Cost`, etc.) are valid `float64` types

---

## 🔍 Sample Records (First 5 Rows)

| Order\_ID       | Order\_Date | Ship\_Mode   | Customer\_Name   | Country   | Category   | Sales   | Profit  |
| --------------- | ----------- | ------------ | ---------------- | --------- | ---------- | ------- | ------- |
| CA-2012-124891  | 2012-07-31  | Same Day     | Rick Hansen      | USA       | Technology | 2309.65 | 762.18  |
| IN-2013-77878   | 2013-02-05  | Second Class | Justin Ritter    | Australia | Furniture  | 3709.39 | -288.77 |
| IN-2013-71249   | 2013-10-17  | First Class  | Craig Reiter     | Australia | Technology | 5175.17 | 919.97  |
| ES-2013-1579342 | 2013-01-28  | First Class  | Katherine Murray | Germany   | Technology | 2892.51 | -96.54  |
| SG-2013-4320    | 2013-11-05  | Same Day     | Rick Hansen      | Senegal   | Technology | 2832.96 | 311.52  |

---

## 📈 Ideal Use Cases

This dataset is excellent for:

* 📊 Sales Performance Dashboards (e.g., Streamlit, Power BI, Tableau)
* 📦 Product and Category Analysis
* 🕒 Time Series Forecasting (e.g., Monthly Sales Trends)
* 🧮 Profitability and Discount Analysis
* 🌍 Geographic Mapping (Country/State/City)
* 👥 Customer Segmentation (e.g., High-Value vs Low-Value)

---

## 🧰 Example Analysis Tools

| Tool                    | Use                                   |
| ----------------------- | ------------------------------------- |
| **Pandas**              | Data cleaning and transformation      |
| **Plotly / Matplotlib** | Visualizing trends and KPIs           |
| **Streamlit**           | Interactive business dashboards       |
| **Scikit-learn**        | Customer clustering, RFM segmentation |

---

