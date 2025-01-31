import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
# Generate random data
#data = np.random.randn(1000)
data = pd.read_csv("ABC_Plot_Data_Slow.csv")
cost = data["Cost"]

# Create a histogram with customizations
plt.hist(cost, bins=80, edgecolor='black', color='skyblue', density=True)

# Set labels and title
plt.xlabel('Cost')
plt.ylabel('Not Sure')
plt.title('Cost Histogram')

# Show the plot
plt.show()

data = pd.read_csv("PSO_Plot_Data_Slow.csv")
cost = data["Cost"]

# Create a histogram with customizations
plt.hist(cost, bins=80, edgecolor='black', color='skyblue', density=True)

# Set labels and title
plt.xlabel('Cost')
plt.ylabel('Not Sure')
plt.title('Cost Histogram')

# Show the plot
plt.show()