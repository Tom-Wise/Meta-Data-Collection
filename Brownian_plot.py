import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import pandas as pd



# Number of steps and time points
steps = 1000
dt = 0.01  # Time step

data = pd.read_csv(r"C:\Users\ThomasWise\source\repos\META_DATA_JAN_25\RUN_Laptop_Found_Bug\IARO_Plot_Data_Slow.csv")
a = data["Cost"]
b = data["Sim"]
c = data["Switch_State_Indx"]

# Generate random steps for x, y, z directions
dx = np.sqrt(dt) * a  # np.random.randn(steps)
dy = np.sqrt(dt) * b  # np.random.randn(steps)
dz = np.sqrt(dt) * c  # np.random.randn(steps)

# Cumulative sum to simulate the Brownian motion path
x = np.cumsum(dx)
y = np.cumsum(dy)
z = np.cumsum(dz)

# Plot the 3D Brownian motion
fig = plt.figure(figsize=(10, 7))
ax = fig.add_subplot(111, projection='3d')

ax.plot(x, y, z, lw=0.5, color='b')  # Plot the path of Brownian motion

# Set labels and title
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')
ax.set_title('3D Brownian Motion')

# Show the plot
plt.show()
