import streamlit as st
import pandas as pd
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler

st.set_page_config(page_title="E-Commerce Dashboard", layout="wide")

# Load Data
@st.cache_data
def load_data():
    df = pd.read_csv("data/ecommerce.csv", encoding='latin1')
    df.columns = df.columns.str.lower().str.strip()

    df = df.dropna()
    df['invoicedate'] = pd.to_datetime(df['invoicedate'])

    df['month'] = df['invoicedate'].dt.month
    df['year'] = df['invoicedate'].dt.year
    df['total_amount'] = df['unitprice'] * df['quantity']

    return df

df = load_data()

st.title("🛒 E-Commerce Analytics Dashboard")

# -------------------------------
# 📊 KPIs
# -------------------------------
col1, col2, col3 = st.columns(3)

col1.metric("Total Revenue", f"{df['total_amount'].sum():,.0f}")
col2.metric("Total Orders", df['invoiceno'].nunique())
col3.metric("Total Customers", df['customerid'].nunique())

# -------------------------------
# 📈 Monthly Sales
# -------------------------------
st.subheader("📈 Monthly Sales Trend")

monthly_sales = df.groupby('month')['total_amount'].sum()
st.line_chart(monthly_sales)

# -------------------------------
# 🌍 Country Analysis
# -------------------------------
st.subheader("🌍 Top Countries")

country_sales = df.groupby('country')['total_amount'].sum().sort_values(ascending=False).head(10)
st.bar_chart(country_sales)

# -------------------------------
# 🏆 Top Products
# -------------------------------
st.subheader("🏆 Top Products")

top_products = df.groupby('description')['quantity'].sum().sort_values(ascending=False).head(10)
st.bar_chart(top_products)

# -------------------------------
# 👤 Customer Segmentation (ML)
# -------------------------------
st.subheader("🤖 Customer Segmentation")

customer_df = df.groupby('customerid').agg({
    'total_amount': 'sum',
    'invoiceno': 'count'
}).rename(columns={
    'total_amount': 'spending',
    'invoiceno': 'frequency'
})

# Scaling
scaler = StandardScaler()
scaled = scaler.fit_transform(customer_df)

# KMeans
kmeans = KMeans(n_clusters=3, random_state=42)
customer_df['segment'] = kmeans.fit_predict(scaled)

# Segment summary
segment_summary = customer_df.groupby('segment').mean()
st.write("### Segment Summary")
st.dataframe(segment_summary)

# ✅ NEW VISUAL HERE
import matplotlib.pyplot as plt

fig, ax = plt.subplots()

for i in range(3):
    subset = customer_df[customer_df['segment'] == i]
    ax.scatter(subset['spending'], subset['frequency'], label=f"Segment {i}")

ax.set_xlabel("Spending")
ax.set_ylabel("Frequency")
ax.legend()

st.pyplot(fig)