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


# volcano data from file implemented on the map with custom markers
fgv = folium.FeatureGroup(name="Volcanoes")  # layer control added
for lt, ln, el in zip(lat, lon, elev):  # need to use zip func when iterating through lists at the same time
    fgv.add_child(folium.CircleMarker(location=[lt, ln], radius=6, popup="Elevation: " + str(el) + " m",
                                      fill_color=color_producer(el), color='black', fill_opacity=0.7))


# set custom markers for starting coordinates
fg = folium.FeatureGroup(name="Custom Marker")
for coordinates in [[36.9, -119.6], [32.9, -110.6]]:
    fg.add_child(folium.Marker(location=coordinates, popup="Hi I am a marker", icon=folium.Icon(color='blue')))


# Polygon layer added from world.json file, set colors based on population
fgp = folium.FeatureGroup(name="Population")
fgp.add_child(folium.GeoJson(data=open('world.json', 'r', encoding='utf-8-sig').read(),
                             style_function=lambda x: {'fillColor': 'green' if x['properties']['POP2005'] < 10000000
                             else 'orange' if 10000000 <= x['properties']['POP2005'] < 20000000 else 'red'}))


map.add_child(fg)
map.add_child(fgv)
map.add_child(fgp)
map.add_child(folium.LayerControl())  # layer control
map.save("Map1.html")  # pass the name for the map file that will be created
