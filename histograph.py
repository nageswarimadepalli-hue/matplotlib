#the distribution of numerical data
 
import matplotlib.pyplot as plt
ages = [100, 71, 62, 20, 24, 25, 56, 47, 35, 29,10,]
plt.hist(ages, bins=5, color='b', edgecolor='black')
plt.title("Age Distribution")
plt.xlabel("Age")
plt.ylabel("Frequency")
plt.show()

