import matplotlib.pyplot as plt

data = [
    10, 12, 15, 18, 20,
    22, 25, 28, 30, 32,
    35, 38, 40, 42, 45,
    48, 50, 52, 55, 58
]

plt.hist(data, bins=5, edgecolor="black")

plt.title("Uniform Distribution")
plt.xlabel("Values")
plt.ylabel("Frequency")

plt.show()