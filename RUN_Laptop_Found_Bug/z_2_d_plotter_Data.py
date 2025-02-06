import os
import pandas as pd
import matplotlib.pyplot as plt


print(f"List of Directory: {os.listdir()}")

# DIRECTORY = "C:\Users\ThomasWise\source\repos\META_DATA_JAN_25\RUN_Laptop_Found_Bug"

# file_name = "ABC_Plot_Data_Slow.csv"

# path = os.join(DIRECTORY, file_name)


# Load the CSV data into a DataFrame
data = pd.read_csv(r"C:\Users\ThomasWise\source\repos\META_DATA_JAN_25\RUN_Laptop_Found_Bug\ALO_Plot_Data_Slow.csv")

# Display basic information
print(data.head(10))  # Shows the first few rows

# Plotting
## Line Plot: Cost over Simulations
plt.figure(figsize=(10, 10))
plt.scatter(data["Sim"], data["Cost"], color='grey')
plt.title("Cost over Simulations")
plt.xlabel("Sim")
plt.ylabel("Cost")
plt.grid(True)
plt.show()

# plt.figure(figsize=(10, 10))
# plt.scatter(data["Sim"], data["Switch_State_Indx"], color='grey')
# plt.title("Switching State over Simulations")
# plt.xlabel("Simulation Index")
# plt.ylabel("Switch_State_Indx")
# plt.grid(True)
# plt.show()

## Bar Plot: B2p values per Switch_State_Indx
# plt.figure(figsize=(20, 5))
# plt.bar(data["Switch_State_Indx"], data["Batt2_power_kW"], color='green')
# plt.title("B2 Power vs Switch_State_Indx")
# plt.xlabel("Switch_State_Indx")
# plt.ylabel("B2p (kW)")
# plt.show()

## Scatter Plot: B1p vs. B2p

plt.figure(figsize=(10, 10))
plt.scatter(data["Sim"], data["Batt1_power_kW"], color='grey')
plt.title("B1 PWR over Simulations")
plt.xlabel("Simulation")
plt.ylabel("B2PWR (kW)")
plt.grid(True)
plt.show()


plt.figure(figsize=(10, 10))
plt.scatter(data["Sim"], data["Batt2_power_kW"], color='grey')
plt.title("B2 PWR over Simulations")
plt.xlabel("Simulation")
plt.ylabel("B2PWR (kW)")
plt.grid(True)
plt.show()


# Create a figure and axis
plt.figure(figsize=(10, 10))

# Plot Switch_State_Indx vs. Sim
plt.scatter(data["Sim"], data["Switch_State_Indx"], color='grey')

# Plot Cost vs. Sim on the same graph with a different color
plt.plot(data["Sim"], data["Cost"], marker='x', color='orange', label="Cost")

# Add a title and labels
plt.title("Switch_State_Indx and Cost over Simulations")
plt.xlabel("Simulation Index")
plt.ylabel("Switch Index")

# Add a legend to distinguish between datasets
plt.legend()

# Show grid
plt.grid(True)

# Display the plot
plt.show()
#plt.savefig(r"C:\Users\ThomasWise\source\repos\META_DATA_JAN_25\RUN_Laptop_Found_Bug\LARO_Plot.fig")