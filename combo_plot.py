import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns
import pandas as pd

plt.style.use('bmh')

model = "PSO"

# Extract data from csv to plot
# C:\Users\ThomasWise\source\repos\META_DATA_JAN_25\META_DATA_TRACKING_JAN_SUCCESS\MODELS_1-10_5E_50_POP
data = pd.read_csv(fr"C:\Users\ThomasWise\source\repos\META_DATA_JAN_25\RUN_4_Longest_Run_30k\{model}_Plot_Data_Slow.csv")
# data = pd.read_csv(fr"C:\Users\ThomasWise\source\repos\META_DATA_JAN_25\META_DATA_TRACKING_JAN_SUCCESS\MODELS_1-10_5E_50_POP\{model}_Plot_Data.csv")

cost = data["Cost"]
sim = data["Sim"]
indx = data["Switch_State_Indx"]
b1p  = data["Batt1_power_kW"]
b1p  = data["Batt2_power_kW"]


x = sim
y = cost 

# Create a figure with subplots
fig = plt.figure(figsize=(10, 10))

# Creating subplots
ax1 = fig.add_subplot(221)  # Main scatter plot
ax1.scatter(cost, sim)
ax1.set_xlabel('Sim')
ax1.set_ylabel('Cost')
ax1.set_title(f'{model} Scatter Plot Cost/Sim')

# Histogram of x in the second subplot
ax2 = fig.add_subplot(222)  # Histogram for x
ax2.hist(cost, bins=60)
ax2.set_xlabel('Cost')
ax2.set_ylabel('Frequency')
ax2.set_title(f"{model} Histogram of Cost")


ax3 = fig.add_subplot(223)
ax3.scatter(data["Sim"], data["Switch_State_Indx"])
ax3.plot(data["Sim"], data["Cost"], marker='x', color='grey', label="Cost")
ax3.set_xlabel("Simulation Index")
ax3.set_ylabel("Switch Index")
ax3.set_title(f"{model} Switch_S Indx & Cost/Simulations")

# Add a legend to distinguish between datasets
plt.legend()
plt.grid(True)

# 3D Plot
xdata = len(sim) 
ydata = len(sim)

# Generate sample data
x = np.linspace(0, xdata, xdata)
y = np.linspace(0, ydata, ydata)
z = cost  #np.sin(np.sqrt(x**2 + y**2))  np.sin(np.sqrt(x**data["Cost"] + y**data["Cost"]))

ax4 = fig.add_subplot(224, projection='3d') 
ax4.scatter(x, y, z,)
ax4.set_xlabel("Sim")
ax4.set_ylabel("Sim")
ax4.set_zlabel("Cost")
ax3.set_title(f"{model} Cost/Simulations")

# Adjust layout and show the plot - Then Save it to file
plt.tight_layout()
# plt.plot(x, y)
# plt.savefig(f'{model}.png')
plt.show()


x = cost # np.random.randn(1000)
y = sim # np.random.randn(1000)

# Create a scatter plot with marginal histograms
sns.jointplot(x=x, y=y, kind='scatter', marginal_kws=dict(bins=30, fill=True)) # height=7, ratio=7

# Show the plot
plt.show()

# Combo Scatter Plot 
plt.figure(figsize=(10, 10))
plt.scatter(data["Sim"], data["Switch_State_Indx"])
plt.plot(data["Sim"], data["Cost"], marker='x', color='grey', label="Cost")
plt.title("Switch_State_Indx and Cost over Simulations")
plt.xlabel("Simulation Index")
plt.ylabel("Switch Index")
plt.legend()
plt.grid(True)
# plt.plot()
# plt.savefig(f'{model}.png')
plt.show()


# Combo Scatter Plot
plt.figure(figsize=(10, 10))
plt.scatter(data["Sim"], data["Batt1_power_kW"])
plt.plot(data["Sim"], data["Cost"], marker='x', color='grey', label="Cost")
plt.title(f"{model} Batt1_power_kW & Cost/Simulations")
plt.xlabel("Simulation Index")
plt.ylabel("Batt1_power_kw")
plt.legend()
plt.grid(True)
# plt.plot()
# plt.savefig(f'{model}.png')
plt.show()


plt.figure(figsize=(10, 10))
plt.scatter(data["Sim"], data["Batt2_power_kW"])
plt.plot(data["Sim"], data["Cost"], marker='x', color='grey', label="Cost")
plt.title(f"{model} Batt2_power_kW & Cost/Simulations")
plt.xlabel("Simulation Index")
plt.ylabel("Batt2_power_kW")
plt.legend()
plt.grid(True)
# plt.plot()
# plt.savefig(f'{model}.png')
plt.show()