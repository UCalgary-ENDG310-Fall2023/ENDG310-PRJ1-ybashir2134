import matplotlib.pyplot as plt
import pandas as pd

# Read GDP and population density data
data1 = pd.read_csv('Data#2/gdp-per-capita-worldbank.csv', comment='#')
data2 = pd.read_csv('Data#2/population-density.csv', comment='#')

# Merge the dataframes based on 'Year' and 'Entity'
merged_data = pd.merge(data1, data2, on=['Year', 'Entity'], how='inner')

# Group the merged data by 'Year' and calculate the annual averages
annual_averages = merged_data.groupby('Year')[['Population density', 'GDP per capita, PPP (constant 2017 international $)']].mean()

# Create a figure with two subplots
fig, ax1 = plt.subplots(figsize=(10, 6))

# Plot Population Density on the left y-axis
ax1.plot(annual_averages.index, annual_averages['Population density'], color='blue', label='Average Global Population Density')
ax1.set_xlabel('Year')
ax1.set_ylabel('Average Global Population Density', color='blue')
ax1.tick_params(axis='y', labelcolor='blue')

# Create a second y-axis on the right
ax2 = ax1.twinx()

# Plot GDP per capita on the right y-axis
ax2.plot(annual_averages.index, annual_averages['GDP per capita, PPP (constant 2017 international $)'], color='orange', label='Average Global GDP per capita (2017 $)')
ax2.set_ylabel('Average Global GDP per capita (2017 $)', color='orange')
ax2.tick_params(axis='y', labelcolor='orange')

# Add a legend
lines, labels = ax1.get_legend_handles_labels()
lines2, labels2 = ax2.get_legend_handles_labels()
ax2.legend(lines + lines2, labels + labels2, loc='upper left')

# Set the title
plt.title("Average Global Population Density and GDP Over Time")

# Show
plt.show()







