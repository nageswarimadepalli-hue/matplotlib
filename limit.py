import matplotlib.pyplot as plt
limits = [1, 2, 3, 4, 5]
plt.plot(limits)
plt.xlim(0, 10)
plt.ylim(0, 20)
plt.title("Limit Example")
plt.xlabel("X-axis")
plt.ylabel("Y-axis")
plt.show()