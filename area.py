import matplotlib.pyplot as plt
months = ["Jan", "Feb", "Mar", "Apr", "May"]
sales = [100, 200, 300, 400, 500]
plt.fill_between(range(len(sales)), sales, color="skyblue", alpha=0.4)
plt.plot(months,sales)

plt.title(" Sales Area Chart")
plt.xlabel("Months")
plt.ylabel("Sales")
plt.show()