

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns

plt.style.use('bmh')

# sns.set_palette('Set3')

model_names = [
    "ABC", "ACOR", "AGTO", "ALO", "AO", "AOA", "ARO", "AVOA", "BA", "BADPT", 
    "BDEV", "DE", "HC", "IARO", "LARO", "PSO", "SA", "SHADE" 
]

data = pd.read_csv(r"C:\Users\ThomasWise\source\repos\META_DATA_JAN_25\RUN_Laptop_Found_Bug\HC_Plot_Data_Slow.csv")
cost = data["Cost"]

# Create a histogram with customizations
plt.hist(cost, bins=80, edgecolor='black', density=True)

# Set labels and title
plt.xlabel('Cost')
plt.ylabel('Density')
plt.title('HC Cost Histogram')

plt.plot()
plt.savefig('HC.png')
# Show the plot
plt.show()


data1 = pd.read_csv(r"C:\Users\ThomasWise\source\repos\META_DATA_JAN_25\RUN_Laptop_Found_Bug\PSO_Plot_Data_Slow.csv")
cost1 = data1["Cost"]

# Create a histogram with customizations
plt.hist(cost1, bins=80, edgecolor='black', density=True)

# Set labels and title
plt.xlabel('Cost')
plt.ylabel('Density')
plt.title('PSO Cost Histogram')

# Show the plot
plt.show()