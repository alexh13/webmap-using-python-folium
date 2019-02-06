# pip install folium
# pip install pandas

import folium
import pandas

# use pandas to access data file
data = pandas.read_csv("Volcanoes.txt")  # accessing file
lat = list(data["LAT"])  # gets LON from data and stores in list
lon = list(data["LON"])
elev = list(data["ELEV"])


def color_producer(elevation):
    if elevation < 1000:
        return 'yellow'
    elif 1000 < elevation < 3000:
        return 'orange'
    else:
        return 'red'


# set map's starting location
map = folium.Map(location=[36.778259, -119.417931], zoom_start=6, tiles="Mapbox Bright")
fg = folium.FeatureGroup(name="My Map")

# data from file implemented on the map
for lt, ln, el in zip(lat, lon, elev):  # need to use zip func when iterating through lists at the same time
    fg.add_child(folium.CircleMarker(location=[lt, ln], radius=6, popup="Elevation: " + str(el) + " m",
                                     fill_color=color_producer(el), color='black', fill_opacity=0.7))

# set custom markers
for coordinates in [[36.9, -119.6], [32.9, -110.6]]:
    fg.add_child(folium.Marker(location=coordinates, popup="Hi I am a marker", icon=folium.Icon(color='blue')))


map.add_child(fg)
map.save("Map1.html")  # pass the name for the map file that will be created













































