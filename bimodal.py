import matplotlib.pyplot as plt

data = [
    20, 21, 22, 23, 24, 25,
    26, 27, 28, 29,
    70, 71, 72, 73, 74, 75,
    76, 77, 78, 79
]

plt.hist(data, bins=8, edgecolor="black")

plt.title("Bimodal Distribution")
plt.xlabel("Values")
plt.ylabel("Frequency")

plt.show()