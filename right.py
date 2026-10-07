import matplotlib.pyplot as plt

salary = [
    25000, 27000, 28000, 30000,
    32000, 35000, 36000, 38000,
    40000, 42000, 45000, 50000,
    55000, 60000, 80000, 120000
]

plt.hist(salary, bins=6, edgecolor="black")

plt.title("Salary Distribution")
plt.xlabel("Salary")
plt.ylabel("Frequency")

plt.show()