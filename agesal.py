import pandas as pd
import matplotlib.pyplot as plt

df = pd.DataFrame({
    "Age": [
        21, 22, 23, 24, 25,
        26, 27, 28, 30, 32,
        35, 36, 38, 40, 42
    ],

    "Salary": [
        22000, 25000, 27000, 28000, 30000,
        32000, 35000, 38000, 40000, 45000,
        48000, 50000, 55000, 75000, 120000
    ]
})

plt.hist(df["Age"], bins=5, edgecolor="black")

plt.title("Employee Age Distribution")
plt.xlabel("Age")
plt.ylabel("Frequency")

plt.show()

plt.hist(df["Salary"], bins=5, edgecolor="black")

plt.title("Employee Salary Distribution")
plt.xlabel("Salary")
plt.ylabel("Frequency")

plt.show()