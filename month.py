import matplotlib.pyplot as plt
month=['January', 'February', 'March', 'April', 'May']
sales2025=[100, 150, 200, 250, 300]
sales2026=[120, 180, 220, 270, 350]
plt.plot(month, sales2025, linestyle='--', marker='D', color='b')
plt.plot(month, sales2026, linestyle='--', marker='D', color='g')
plt.title("Sales Comparison")
plt.xlabel("Month")
plt.ylabel("Sales")
plt.show()