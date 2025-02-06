import os
import pandas as pd
import matplotlib.pyplot as plt


model_names = [
    "ABC", "ACOR", "AGTO", "ALO", "AO", "AOA", "ARO", "AVOA", "BA", "BADPT", 
    "BDEV", "DE", "HC", "IARO", "LARO", "PSO", "SA", "SHADE" 
]

#print(f"List of Directory: {os.listdir()}")
# DIRECTORY = "C:\Users\ThomasWise\source\repos\META_DATA_JAN_25\RUN_Laptop_Found_Bug"
# file_name = "ABC_Plot_Data_Slow.csv"
# path = os.join(DIRECTORY, file_name)

# Load the CSV data into a DataFrame
data = pd.read_csv(r"C:\Users\ThomasWise\source\repos\META_DATA_JAN_25\RUN_Laptop_Found_Bug\ALO_Plot_Data_Slow.csv")

# Display basic information - Verify Quality
print(data.head(10))  

# Set Values for ease of use
cost = data["Cost"]
sim = data["Sim"]
indx = data["Switch_State_Indx"]
b1p  = data["Batt1_power_kW"]
b1p  = data["Batt2_power_kW"]

# Stylize the graphs
plt.style.use('bmh')

# Histogram
plt.figure(figsize=(10, 10))
plt.hist(cost, bins=80, edgecolor='black', density=True)
plt.xlabel('Cost')
plt.ylabel('Density')
plt.title('ALO Cost Histogram')
# This order for saving .png
plt.plot()
plt.savefig('ALO_Histogram.png')
plt.show()

# Plotting
## Line Plot: Cost over Simulations
plt.figure(figsize=(10, 10))
plt.scatter(data["Sim"], data["Cost"], color='grey')
plt.title("Cost over Simulations")
plt.xlabel("Sim")
plt.ylabel("Cost")
plt.grid(True)
plt.show()

plt.figure(figsize=(10, 10))
plt.scatter(data["Sim"], data["Switch_State_Indx"], color='grey')
plt.title("Switching State over Simulations")
plt.xlabel("Simulation Index")
plt.ylabel("Switch_State_Indx")
plt.grid(True)
plt.show()


# Combo Scatter Plot 
plt.figure(figsize=(10, 10))
plt.scatter(data["Sim"], data["Switch_State_Indx"], color='b')
plt.plot(data["Sim"], data["Cost"], marker='x', color='grey', label="Cost")
plt.title("Switch_State_Indx and Cost over Simulations")
plt.xlabel("Simulation Index")
plt.ylabel("Switch Index")
plt.legend()
plt.grid(True)
plt.show()


# Combo Scatter Plot
plt.figure(figsize=(10, 10))
plt.scatter(data["Sim"], data["Batt1_power_kW"], color='b')
plt.plot(data["Sim"], data["Cost"], marker='x', color='grey', label="Cost")
plt.title("Switch_State_Indx and Cost over Simulations")
plt.xlabel("Simulation Index")
plt.ylabel("Switch Index")
plt.legend()
plt.grid(True)
plt.show()


#plt.savefig(r"C:\Users\ThomasWise\source\repos\META_DATA_JAN_25\RUN_Laptop_Found_Bug\LARO_Plot.fig")





# ## Bar Plot: B2p values per Switch_State_Indx
# plt.figure(figsize=(10, 10))
# plt.bar(data["Switch_State_Indx"], data["Batt1_power_kW"], color='green')
# plt.title("B1 Power vs Switch_State_Indx")
# plt.xlabel("Switch_State_Indx")
# plt.ylabel("B1 Pwr kW")
# plt.show()

# ## Bar Plot: B2p values per Switch_State_Indx
# plt.figure(figsize=(10, 10))
# plt.bar(data["Switch_State_Indx"], data["Batt2_power_kW"], color='green')
# plt.title("B2 Power vs Switch_State_Indx")
# plt.xlabel("Switch_State_Indx")
# plt.ylabel("B2 Pwr kW")
# plt.show()

## Scatter Plot: B1p vs. B2p

# plt.figure(figsize=(10, 10))
# plt.scatter(data["Sim"], data["Batt1_power_kW"], color='grey')
# plt.title("B1 PWR over Simulations")
# plt.xlabel("Simulation")
# plt.ylabel("B2PWR (kW)")
# plt.grid(True)
# plt.show()


# plt.figure(figsize=(10, 10))
# plt.scatter(data["Sim"], data["Batt2_power_kW"], color='grey')
# plt.title("B2 PWR over Simulations")
# plt.xlabel("Simulation")
# plt.ylabel("B2PWR (kW)")
# plt.grid(True)
# plt.show()