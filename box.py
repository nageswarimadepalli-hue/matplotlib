import matplotlib.pyplot as plt

salary = [30000, 40000, 50000, 60000, 70000, 80000, 90000]
plt.boxplot(salary)
plt.title("Salary Distribution")
plt.ylabel("Salary")
plt.show()