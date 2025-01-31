import pandas as pd
import matplotlib.pyplot as plt

# Load the CSV data into a DataFrame
data = pd.read_csv("ABC_Plot_Data_Slow.csv")

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

# ## Bar Plot: B2p values per Switch_State_Indx
# plt.figure(figsize=(10, 5))
# plt.bar(data["Switch_State_Indx"], data["B2p (kW)"], color='green')
# plt.title("B2p Power Output per Switch_State_Indx")
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
#plt.plot(data["Sim"], data["Cost"], marker='x', color='orange', label="Cost")

# Add a title and labels
plt.title("Switch_State_Indx and Cost over Simulations")
plt.xlabel("Simulation Index (Sim)")
plt.ylabel("Values")

# Add a legend to distinguish between datasets
plt.legend()

# Show grid
plt.grid(True)

# Display the plot
plt.show()