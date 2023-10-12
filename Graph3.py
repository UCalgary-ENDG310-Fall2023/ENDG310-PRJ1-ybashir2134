#ChatGPT Prompt: How do I make group countries based on their continent
#ChatGPT Prompt: How can I filter out outliers to avoid the scale from being immensely skewed by them

import plotly.express as px
import pandas as pd
import country_converter as coco

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

# Create a scatter plot with color-coded points by continent, faceted by continent
fig = px.scatter(
    merged_data,
    x='GDP per capita, PPP (constant 2017 international $)',
    y='Population density',
    color='Continent',
    hover_name='Entity',
    title=f'Scatter Plot of GDP per capita vs. Population Density ({year_to_visualize})',
    facet_col='Continent',  # Create subplots for each continent
    facet_col_wrap=3,       # Limit the number of subplots per row
)

# Update subplot titles for countries without a continent label
for i in range(len(fig.data)):
    if fig.data[i].facet_row == 'Different income groups countries':
        fig.data[i].facet_row = 'Different income groups countries'

# Update axis labels and layout for better readability
fig.update_xaxes(title_text='GDP per capita', type='log')
fig.update_layout(
    showlegend=True,
    legend_title='Continent',
    legend_traceorder='reversed'
)

# Show the plot
fig.show()



