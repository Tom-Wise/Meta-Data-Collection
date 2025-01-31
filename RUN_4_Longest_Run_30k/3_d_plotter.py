import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import numpy as np
import pandas as pd

data = pd.read_csv("ABC_Plot_Data_Slow.csv")


# Generate sample data
x = np.linspace(-5, 5, 100)
y = np.linspace(-5, 5, 100)
z = np.sin(np.sqrt(x**2 + y**2))  # Example function

# Create a figure
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
x = np.linspace(-5, 5, 100)
y = np.linspace(-5, 5, 100)
x, y = np.meshgrid(x, y)
z = np.sin(np.sqrt(x**2 + y**2))  # Example function

# Create a figure
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# Plot the surface
ax.plot_surface(x, y, z, cmap='viridis')

# Set labels
ax.set_xlabel('X Label')
ax.set_ylabel('Y Label')
ax.set_zlabel('Z Label')

# Show the plot
plt.show()

