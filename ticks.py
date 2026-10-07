import matplotlib.pyplot as plt

ticket = [1, 2, 3, 4, 5]

plt.plot(ticket)

plt.xticks([0, 2, 4, 6, 8, 10])
plt.yticks([0, 5, 10, 15, 20])

plt.title("Limit Example")
plt.xlabel("X-axis")
plt.ylabel("Y-axis")

plt.show()