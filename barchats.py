#Barchats are used for categorical comaperision

import matplotlib.pyplot as plt
products = ['mobile', 'laptop', 'headphones', 'tablet', 'smartwatch']
sales = [1000, 1500, 2000, 2500, 3000]
plt.barh(products, sales, color='b')
plt.title("Sales Data")
plt.xlabel("Product")
plt.ylabel("Sales")
plt.show()