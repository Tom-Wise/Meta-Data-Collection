import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import numpy as np
import pandas as pd

plt.style.use('bmh')

data = pd.read_csv(r"C:\Users\ThomasWise\source\repos\META_DATA_JAN_25\RUN_4_Longest_Run_30k\IARO_Plot_Data_Slow.csv")

xdata = len(data["Sim"])
ydata = len(data["Sim"])


# Generate sample data
x = np.linspace(0, xdata, xdata)
y = np.linspace(0, ydata, ydata)
z = np.sin(np.sqrt(x**data["Cost"] + y**data["Cost"])) # data["Cost"]  #np.sin(np.sqrt(x**2 + y**2))  np.sin(np.sqrt(x**data["Cost"] + y**data["Cost"]))


fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# Create scatter plot
ax.scatter(x, y, z)

# Set labels
ax.set_xlabel('X Label')
ax.set_ylabel('Y Label')
ax.set_zlabel('Z Label')

# Show the plot
plt.show()

# # Generate grid data
# x = np.linspace(0, xdata, xdata)
# y = np.linspace(0, ydata, ydata)
# x, y = np.meshgrid(x, y)
# z = np.square[data["Cost"], data["Cost"]]#np.sin(np.sqrt(x**2 + y**2))  # Example function

# # Create a figure
# fig = plt.figure()
# ax = fig.add_subplot(111, projection='3d')

# # Plot the surface
# ax.plot_surface(x, y, z, cmap='viridis')

# # Set labels
# ax.set_xlabel('X Label')
# ax.set_ylabel('Y Label')
# ax.set_zlabel('Z Label')

# # Show the plot
# plt.show()

