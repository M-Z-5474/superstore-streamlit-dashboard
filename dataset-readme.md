
# 🗂️ Global Superstore Dataset
The **Global Superstore Dataset** is a popular sample dataset widely used in Business Intelligence (BI), data analytics, and dashboard development. It contains thousands of records simulating retail transactions across various regions, helping analysts practice real-world business insight extraction.

---

## 📋 Dataset Summary

| Feature | Description                                                                                   |
| ------- | --------------------------------------------------------------------------------------------- |
| Rows    | \~10,000+ retail transactions                                                                 |
| Columns | 24 fields including Sales, Profit, Region, Category, Product, and Customer                    |
| Format  | CSV (`Global_Superstore.csv`)                                                                 |
| Size    | \~1 MB                                                                                        |
| Source  | [Kaggle Dataset Link](https://www.kaggle.com/datasets/apoorvaappz/global-super-store-dataset) |

---

## 🧾 Column Description

| Column Name      | Description                                                         |
| ---------------- | ------------------------------------------------------------------- |
| `Order ID`       | Unique identifier for each order                                    |
| `Order Date`     | Date the order was placed                                           |
| `Ship Date`      | Shipping date of the order                                          |
| `Ship Mode`      | Shipping method (e.g., Standard Class, First Class)                 |
| `Customer ID`    | Unique ID for each customer                                         |
| `Customer Name`  | Name of the customer                                                |
| `Segment`        | Customer type: Consumer, Corporate, or Home Office                  |
| `Country`        | Country of sale (mostly United States data)                         |
| `City`           | City where the order was placed                                     |
| `State`          | U.S. State                                                          |
| `Postal Code`    | Postal/ZIP code                                                     |
| `Region`         | Region of sale (West, East, Central, South)                         |
| `Product ID`     | Unique ID for the product                                           |
| `Category`       | Category (Furniture, Office Supplies, Technology)                   |
| `Sub-Category`   | Sub-category within each category                                   |
| `Product Name`   | Name of the product                                                 |
| `Sales`          | Total sales amount for the order                                    |
| `Quantity`       | Number of units ordered                                             |
| `Discount`       | Discount applied to the order                                       |
| `Profit`         | Profit earned from the order                                        |
| `Row ID`         | Row index (mostly used for internal reference)                      |
| `Market`         | Market/continent name (e.g., APAC, EU, US, Africa) *(if available)* |
| `Shipping Cost`  | Cost of shipping *(may be added in some versions)*                  |
| `Order Priority` | Priority level: Low, Medium, High, Critical *(if available)*        |

---

## 📊 Use Cases

This dataset is ideal for:

* 📈 **Sales & Profit Analysis**
* 📍 **Geo Visualization (State/City-wise Sales)**
* 📦 **Product and Category Performance**
* 👥 **Customer Segmentation**
* 🕒 **Time Series Forecasting**
* 📉 **Discount vs Profit Impact**

---

## 🧹 Cleaning & Preprocessing Notes

* Dates are converted to `datetime` format
* Missing values handled appropriately
* Monetary columns (`Sales`, `Profit`) are converted to float
* Regions and Segments are categorized for filtering

---


