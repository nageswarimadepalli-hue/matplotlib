import pandas as pd
import matplotlib.pyplot as plt

# Create DataFrame
df = pd.DataFrame({
    "Month": ["Jan", "Feb", "Mar", "Apr", "May", "Jun"],
    "Sales": [120, 150, 130, 180, 210, 190],
    "Orders": [40, 45, 42, 55, 62, 58]
})

# 1. Sales Trend
plt.plot(df["Month"], df["Sales"], marker="o")
plt.title("Monthly Sales")
plt.xlabel("Month")
plt.ylabel("Sales")
plt.grid()
plt.show()

# 2. Sales Comparison
plt.bar(df["Month"], df["Sales"])
plt.title("Monthly Sales Comparison")
plt.show()

# 3. Orders Distribution
plt.hist(df["Orders"], bins=4, edgecolor="black")
plt.title("Orders Distribution")
plt.xlabel("Orders")
plt.ylabel("Frequency")
plt.show()

# 4. Sales vs Orders
plt.scatter(df["Orders"], df["Sales"])
plt.title("Orders vs Sales")
plt.xlabel("Orders")
plt.ylabel("Sales")
plt.show()