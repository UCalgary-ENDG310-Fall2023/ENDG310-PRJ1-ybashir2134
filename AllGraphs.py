import plotly.express as px
import pandas as pd
import pycountry
import country_converter as coco

# Read GDP and population density data
data1 = pd.read_csv('ENDG310-PRJ1-ybashir2134/Data#2/gdp-per-capita-worldbank.csv', comment='#')
data2 = pd.read_csv('ENDG310-PRJ1-ybashir2134/Data#2/population-density.csv', comment='#')

# GRAPH 1
# Merge the dataframes based on 'Year' and 'Entity'
merged_data = pd.merge(data1, data2, on=['Year', 'Entity'], how='inner')
# Group the merged data by 'Year' and calculate the annual averages
annual_averages = merged_data.groupby('Year')[['Population density', 'GDP per capita, PPP (constant 2017 international $)']].mean()

# Reset the index to make 'Year' a regular column
annual_averages = annual_averages.reset_index()

fig1 = px.line(annual_averages, x="Year", y=['Population density', 'GDP per capita, PPP (constant 2017 international $)'],
              title="Global Population Density and GDP Over Time")
fig1.update_layout(xaxis_title="Year", yaxis_title="Value")

# Display Graph 1
fig1.show()

# Add text or instructions
print("Graph 1: Global Population Density and GDP Over Time")
print("This graph shows the changes in global population density and GDP over time.")

# GRAPH 2
# Read GDP and population density data
data1 = pd.read_csv('Data#2/gdp-per-capita-worldbank.csv', comment='#')
data2 = pd.read_csv('Data#2/population-density.csv', comment='#')

# Specify the year you want to visualize (e.g., 2021)
year_to_visualize = 2021

# Filter the data for the specified year
data1_year = data1[data1['Year'] == year_to_visualize]
data2_year = data2[data2['Year'] == year_to_visualize]

# Use country_converter to map countries to continents
cc = coco.CountryConverter()
data1_year['Continent'] = data1_year['Entity'].apply(lambda x: cc.convert(names=x, to='continent'))

# Merge the two datasets based on the 'Entity' column
merged_data = pd.merge(data1_year, data2_year, on='Entity', how='inner')

# Filter out outliers (e.g., GDP > 100,000)
max_gdp_threshold = 100000
merged_data = merged_data[merged_data['Population density'] < 5000]
merged_data = merged_data[merged_data['GDP per capita, PPP (constant 2017 international $)'] <= max_gdp_threshold]

fig2 = px.scatter(
    merged_data,
    x='GDP per capita, PPP (constant 2017 international $)',
    y='Population density',
    color='Continent',
    hover_name='Entity',
    title=f'Scatter Plot of GDP per capita vs. Population Density ({year_to_visualize})',
    facet_col='Continent',  # Create subplots for each continent
    facet_col_wrap=3,       # Limit the number of subplots per row
)

fig2.update_xaxes(title_text='GDP per capita', type='log')
fig2.update_layout(
    showlegend=True,
    legend_title='Continent',
    legend_traceorder='reversed'
)

# Display Graph 2
fig2.show()

# Add text or instructions
print("Graph 2: Scatter Plot of GDP per capita vs. Population Density")
print("This scatter plot shows the relationship between GDP per capita and population density in different continents.")

# GRAPH 3
# Specify the income groups you want to include, including 'European Countries (27)'
income_groups = ['Lower-income countries', 'Lower-middle-income countries', 'Upper-middle-income countries', 'High-income countries', 'European Countries (27)']

# Filter data for the specified income groups
filtered_data = merged_data[merged_data['Entity'].isin(income_groups)]

fig3 = px.bar(filtered_data, x='Entity', y='Population density',
             animation_frame='Year',
             color='Entity',
             title='Population Density Over Time by Income Group',
             labels={'Entity': 'Income Group', 'Population density': 'Population Density'})

fig3.update_layout(yaxis=dict(range=[0, filtered_data['Population density'].max() + 100]))


# Display Graph 3
fig3.show()

# Add text or instructions
print("Graph 3: Population Density Over Time by Income Group")
print("This animated bar chart displays the population density over time for different income groups.")

