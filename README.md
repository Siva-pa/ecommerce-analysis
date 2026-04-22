
# 🛒 E-Commerce Data Analysis & Customer Segmentation

## 📌 Overview
This project presents an end-to-end data analysis pipeline for an e-commerce dataset using Python, SQL, and Machine Learning. It uncovers key business insights such as sales trends, customer behavior, and high-value customer segments, and visualizes them through an interactive dashboard.

---

## 🚀 Key Features

- 📊 Data Cleaning & Preprocessing (Pandas)
- 🧠 Feature Engineering (Revenue, Month, Year)
- 🗄️ SQL-based Data Analysis & Optimization
- 📈 Data Visualization (Matplotlib)
- 🌐 Interactive Dashboard (Streamlit)
- 🤖 Customer Segmentation using K-Means Clustering

---

## 🧰 Tech Stack

- Python (Pandas, NumPy, Matplotlib, Scikit-learn)
- SQL (SQLite)
- Streamlit
- Jupyter Notebook

---

## 📂 Project Structure
```
ecommerce-analysis/
│
├── data/
│   └── ecommerce.csv
│
├── notebooks/
│   └── analysis.ipynb
│
├── src/
│   ├── data_cleaning.py
│   ├── db_connection.py
│   └── analysis.py
│
├── sql/
│   └── queries.sql
│
├── visuals/
│
├── app.py
│
└── README.md
```
---

## ⚙️ Installation & Setup

### 1️⃣ Clone Repository
```bash
git clone https://github.com/your-username/ecommerce-analysis.git
cd ecommerce-analysis
```

### 2️⃣ Create Virtual Environment
```
python -m venv venv
venv\Scripts\activate   # Windows
# source venv/bin/activate   # Mac/Linux
```

### 3️⃣ Install Dependencies
```
pip install -r requirements.txt
```

### ▶️ Run Project
Run Data Pipeline

```
cd src
python data_cleaning.py
python db_connection.py
python analysis.py
```

### Run Dashboard
```
streamlit run app.py
```

### 📊 Dashboard Features
  📈 Monthly Sales Trend
  🌍 Top Countries by Revenue
  🏆 Top Selling Products
  👤 High-Value Customers
  🤖 Customer Segmentation (K-Means)
  
# 🤖 Machine Learning – Customer Segmentation

Customers are grouped based on:

  💰 Total Spending
  🔁 Purchase Frequency
## Segments:
  Segment 0 → Low-value customers
  Segment 1 → Medium-value customers
  Segment 2 → High-value (VIP customers)
# 📈 Key Insights
  A small percentage of customers contribute to a large portion of revenue (Pareto Principle)
  Sales show strong seasonal trends
  Certain products dominate total sales volume
  The United Kingdom leads in revenue generation
  Customer segmentation enables targeted marketing strategies
# ⚡ SQL Optimization

Implemented indexing to improve query performance:
```
CREATE INDEX idx_customer ON orders(customerid);
```
# 📌 Future Improvements
Add Power BI Dashboard
Implement RFM Segmentation
Build Recommendation System
Deploy Dashboard to Cloud
# 🤝 Contributing

Contributions are welcome!
Feel free to fork this repository and submit a pull request.

# 📜 License

This project is licensed under the MIT License.

# 👤 Author

Siva Kishore Pasupuleti

⭐ If you like this project, give it a star!
