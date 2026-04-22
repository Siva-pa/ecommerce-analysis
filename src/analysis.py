import pandas as pd
import matplotlib.pyplot as plt
from db_connection import create_connection

conn = create_connection()

# Monthly sales
monthly_sales = pd.read_sql("""
    SELECT month, SUM(total_amount) as revenue
    FROM orders
    GROUP BY month
    ORDER BY month
""", conn)

plt.figure()
plt.plot(monthly_sales['month'], monthly_sales['revenue'])
plt.title("Monthly Sales Trend")
plt.xlabel("Month")
plt.ylabel("Revenue")
plt.savefig("../visuals/monthly_sales.png")
plt.show()

# Top customers
top_customers = pd.read_sql("""
    SELECT customerid, SUM(total_amount) as revenue
    FROM orders
    GROUP BY customerid
    ORDER BY revenue DESC
    LIMIT 10
""", conn)

plt.figure()
plt.bar(top_customers['customerid'].astype(str), top_customers['revenue'])
plt.title("Top Customers")
plt.xticks(rotation=45)
plt.savefig("../visuals/top_customers.png")
plt.show()