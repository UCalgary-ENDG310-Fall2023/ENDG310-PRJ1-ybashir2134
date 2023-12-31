#ChatGPT Prompt: How do I add an animation frame to produce a slider for the years.
#ChatGPT Prompt : How do I change the color scale.

import plotly.express as px
import pandas as pd

# Read GDP and population density data
data1 = pd.read_csv('Data#2/gdp-per-capita-worldbank.csv', comment='#')

# Create a choropleth map
fig = px.choropleth(data1, 
                    locations='Entity',  # Country names
                    locationmode='country names',
                    color='GDP per capita, PPP (constant 2017 international $)',  # Color based on GDP per capita
                    animation_frame='Year',  # Animation frame for years
                    color_continuous_scale='Viridis',  # Color scale
                    title='World GDP per Capita (Year-wise)')

fig.update_geos(
    showcoastlines=True, coastlinecolor="Black", showland=True, landcolor="white",
    showocean=True, oceancolor="lightblue"
)

# Show the map
fig.show()










