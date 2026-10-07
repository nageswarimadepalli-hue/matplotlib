import matplotlib.pyplot as plt
years = [2015, 2016, 2017, 2018, 2019]
sales = [200, 15, 40, 25, 30]
plt.plot(years, sales,linestyle='--', marker='D', color='b')
plt.title("Sales Data")
plt.xlabel("Year")
plt.ylabel("Sales")
plt.grid(True)
plt.show()