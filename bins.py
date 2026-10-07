import matplotlib.pyplot as plt

# Marks data
marks = [35, 40, 42, 45, 48, 50, 52, 55, 58, 60,
         62, 65, 68, 70, 72, 75, 78, 80, 82, 85,
         88, 90, 92, 95, 98]

# 1. 5 bins
plt.hist(marks, bins=5, edgecolor="black")
plt.title("Histogram - 5 Bins")
plt.xlabel("Marks")
plt.ylabel("Frequency")
plt.show()

# 2. 3 bins - fewer, broader groups
plt.hist(marks, bins=3, edgecolor="black")
plt.title("Histogram - 3 Bins")
plt.xlabel("Marks")
plt.ylabel("Frequency")
plt.show()

# 3. 10 bins - more detail
plt.hist(marks, bins=10, edgecolor="black")
plt.title("Histogram - 10 Bins")
plt.xlabel("Marks")
plt.ylabel("Frequency")
plt.show()

# 4. 30 bins - very detailed groups
plt.hist(marks, bins=30, edgecolor="black")
plt.title("Histogram - 30 Bins")
plt.xlabel("Marks")
plt.ylabel("Frequency")
plt.show()