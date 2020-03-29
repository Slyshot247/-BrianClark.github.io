''' This map will help give a heat map of high crime / low crime stats in your area '''

import folium
import branca
import geojson
import json
import os
import requests
# map of a small town in Mississippi USA
m = folium.Map(
    location=[32.348141,-90.882462], ## Reference for lat/long coordinates : https://www.latlong.net/
    tiles='Stamen Terrain',  ## default setttings
    zoom_start=10,           ## The lower these settings the farther zoomed in when map is opened
    min_lat=90,
    max_lat=90,
    prefer_canvas=True,
    control_scale=True
)
##  Message bubble for markers on the map
Parktip = 'Across The World '
Ameristar = 'Best steakhouse you ever had at Bourbons.'
Deer = 'You can see beautiful deer in this little town.'

## Crates a custom marker icon

logoIcon= folium.features.CustomIcon('Deer .jpg', icon_size=50,)
## Vega Data
vis = os.path.join('Data','vis.json')
## Geo Json Data
overlay = os.path.join('Data','overlay.json')
###______________________________________________________________________________
'''                                 MARKERS                                     '''
##_______________________________________________________________________________

folium.Marker(
    [32.307447, -90.874272],
    popup='<strong><i> Different Region </i></strong>',
    tooltip=Parktip,
    icon=folium.Icon(icon='cloud')).add_to(m)
folium.Marker(
    [32.336750, -90.829177],
    popup='<strong><i>Different Place</i></strong>',
    tooltip=Parktip,
    icon=folium.Icon(color='purple')).add_to(m)

folium.Marker(
    [32.317160, -90.899330],
    popup='<b>Ameristar Casino</b>',
    tooltip=Ameristar ).add_to(m)
folium.Marker(
    [32.335988, -90.872309],
    popup='<strong><i>Military Park </i></strong>',
    tooltip=Parktip,
    icon=folium.Icon(color='green', icon='leaf')).add_to(m)
# Image Marker
folium.Marker(
    [32.336988, -90.772309],
    popup='<strong><i>Deer Image/i></strong>',
    tooltip=Parktip,
    icon=logoIcon).add_to(m)
# Circle Marker
folium.CircleMarker(
    location=[32.331470,-90.612720],
    radius=70,
    popup='Community College ',
    color='#428bca',
    fill=True,
    fill_color='#428bca'

).add_to(m)

# Vega Data
folium.Marker(
    [32.333559, -90.266873],
    popup=folium.Popup(max_width=450).add_child(folium.Vega(json.load(open(vis))))).add_to(m)

# Geojson Overlay
folium.GeoJson(overlay, name='Jackson').add_to(m)
###______________________________________________________________________________
'''                                Various Layers                               '''
##_______________________________________________________________________________
# add tiles layers to map top right corner icon of the map
folium.raster_layers.TileLayer('Open Street Map').add_to(m)
folium.raster_layers.TileLayer('Stamen Terrain').add_to(m)
folium.raster_layers.TileLayer('Stamen Watercolor').add_to(m)
folium.raster_layers.TileLayer('CartoDB Positron').add_to(m)
folium.raster_layers.TileLayer('CartoDB Dark_Matter').add_to(m)

# add layer control to show different maps top right corner icon
folium.LayerControl().add_to(m)

##________________________________________________________________
##                          Heatmap                             ##
##______________________________________________________________##

# Save to an html file to display the map on local host
m.save('index.html')
##


###______________________________________________________________________________
'''                              MINI MAP                                       '''
##_______________________________________________________________________________
# display map


'''
folium.Map(
    location=[32.348141, -90.882462],
    tiles='Mapbox Bright',
    zoom_start=13
)'''
#
