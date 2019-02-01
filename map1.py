# pip install folium

import folium


map = folium.Map(location=[36.778259, -119.417931], zoom_start=6, tiles="Mapbox Bright")  # set map's starting location
# set starting zoom level for this location

fg = folium.FeatureGroup(name="My Map")

for coordinates in [[36.9, -119.6], [32.9, -110.6]]:
    fg.add_child(folium.Marker(location=coordinates, popup="Hi I am a marker", icon=folium.Icon(color='blue')))


map.add_child(fg)


map.save("Map1.html")  # pass the name for the map file that will be created













































