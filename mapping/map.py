import pandas
import folium

data = pandas.read_csv("Volcanoes.txt")

lat = list(data["LAT"])
lon = list(data["LON"])
elev = list(data["ELEV"])

def color_producer(elevation):
    if elevation < 1000.0:
        return 'green'
    elif 1000.0 <= elevation < 3000.0:
        return 'orange'
    else:
        return 'red'

map = folium.Map(location=[-34.0, -59.0], zoom_start=6, tile_layer="Stamen Terrain")
fgv = folium.FeatureGroup(name="Volcanoes")

for lt, ln, el in zip(lat, lon, elev):
    fgv.add_child(folium.CircleMarker(location=[lt, ln], popup=str(el)+" m", radius=7, 
    fill_color=color_producer(el), color='black', fill_opacity=0.7))


fgp = folium.FeatureGroup(name="Population")

fgp.add_child(folium.GeoJson(data=open('world.json', 'r', encoding='utf-8-sig').read(), 
style_function=lambda x:{'fillColor':'green' if x['properties']['POP2005'] < 10000000 else 'orange' 
if 10000000 <= x['properties']['POP2005'] < 20000000 else 'red'}))

map.add_child(fgv)
map.add_child(fgp)
map.add_child(folium.LayerControl())

map.save("Map1.html")
