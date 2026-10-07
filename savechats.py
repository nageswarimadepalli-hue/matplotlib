import matplotlib.pyplot as plt

months = ["Jan", "Feb", "Mar", "Apr"]
sales = [100, 150, 120, 180]

plt.plot(months, sales)
plt.title("Monthly Sales")
plt.xlabel("Month")
plt.ylabel("Sales")

# Save the chart as PNG
plt.savefig("sales_chart.png")

# Save the chart as PDF
plt.savefig("sales_chart.pdf")

# Display the chart
plt.show()