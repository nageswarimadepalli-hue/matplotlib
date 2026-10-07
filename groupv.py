import pandas as pd
import matplotlib.pyplot as plt

# Create DataFrame
df = pd.DataFrame({
    "Department": ["IT", "HR", "IT", "Sales", "HR", "Sales"],
    "Salary": [50000, 40000, 60000, 45000, 50000, 55000]
})

# Calculate average salary for each department
summary = df.groupby("Department")["Salary"].mean()

# Create bar chart
plt.bar(summary.index, summary.values)

plt.title("Average Salary by Department")
plt.xlabel("Department")
plt.ylabel("Average Salary")

plt.show()