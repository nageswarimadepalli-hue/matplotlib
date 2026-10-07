import matplotlib.pyplot as plt

months = ["Jan", "Feb", "Mar", "Apr"]
sales = [100, 150, 120, 180]

# Create 2 rows and 2 columns of subplots
fig, axes = plt.subplots(2, 2, figsize=(10, 7))

# 1. Line Chart
axes[0, 0].plot(months, sales)
axes[0, 0].set_title("Line Chart")

# 2. Bar Chart
axes[0, 1].bar(months, sales)
axes[0, 1].set_title("Bar Chart")

# 3. Histogram
axes[1, 0].hist(sales)
axes[1, 0].set_title("Histogram")

# 4. Scatter Plot
axes[1, 1].scatter(range(4), sales)
axes[1, 1].set_title("Scatter Plot")

# Adjust spacing
plt.tight_layout()

# Display the figure
plt.show()