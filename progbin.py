import matplotlib.pyplot as plt

data = [10, 12, 15, 18, 20, 22, 25, 27, 30, 35]

frequency, bins, patches = plt.hist(
    data,
    bins=3,
    edgecolor="black"
)

print("Frequency:")
print(frequency)

print("Bin Boundaries:")
print(bins)

plt.title("Histogram Values")
plt.xlabel("Values")
plt.ylabel("Frequency")

plt.show()