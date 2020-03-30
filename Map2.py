import folium
import pandas as pd
import os
import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches # needed for waffle Charts

mpl.style.use('ggplot') # for ggplot-like style

# check for latest version of Matplotlib
print ('Matplotlib version: ', mpl.__version__) # >= 2.0.0

states = os.path.join('Data', 'us-states.json')
unemployment_data= os.path.join('Data', 'us_unemployment.csv')
state_data = pd.read_csv(unemployment_data)





m = folium.Map(location =[48, -102], zoom_start=3)

folium.Choropleth(  # Had to change the sentext from m.Choropleth to folium.Choropleth 3/29/2020
    geo_data=states,
    name='choropleth',
    data=state_data,
    columns=['State','Unemployment'],
    key_on='feature.id',
    fill_color='YlOrRd',## YlGn/Green
    fill_opacity=0.7,
    line_opacity=0.2,
    legend_name='Unemployment Rate %',
    reset=True
).add_to(m)

folium.LayerControl().add_to(m)

m.save('map2.html')