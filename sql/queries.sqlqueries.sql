-- Total Sales
SELECT SUM(total_amount) AS total_sales FROM orders;

-- Monthly Sales Trend
SELECT month, SUM(total_amount) AS revenue
FROM orders
GROUP BY month
ORDER BY month;

-- Top 10 Products
SELECT product_name, SUM(quantity) AS total_sold
FROM orders
GROUP BY product_name
ORDER BY total_sold DESC
LIMIT 10;

-- Customer Behavior
SELECT customer_id, COUNT(order_id) AS total_orders
FROM orders
GROUP BY customer_id
ORDER BY total_orders DESC;

-- Optimization
CREATE INDEX idx_customer ON orders(customer_id);