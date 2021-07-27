#Folium turns python code into html, css, and javascript in order to create the web map.
import folium
import pandas

#Using Pandas to read the .csv file.
data = pandas.read_csv(r"C:/Users/jjt45_000/Desktop/Python/MountainWebMap/Volcanoes.csv", engine = 'python')
lat = list(data["LAT"])
lon = list(data["LON"])
elev = list(data["ELEV"]) 

#Function that determines marker color based on mountain elevation.
def color_producer(elevation): 
    if elevation < 1000:
        return 'green'
    elif 1000 <= elevation <3000:
        return 'orange'
    else:
        return 'red'

#Map variable
map = folium.Map(location=[41.34551, -81.52960], zoom_start=6, tiles="Stamen Terrain")     

#feature groups allow you to add multiple features
fgv = folium.FeatureGroup(name="Volcanoes")
 


#For loop to add multiple map markers.
for lt, ln, el in zip(lat, lon, elev): 
    fgv.add_child(folium.CircleMarker(location=[lt, ln,], radius = 6, popup=str(el)+ "m",                                                                     
    fill_color=color_producer(el), color = 'grey', fill_opacity=0.7))


fgp = folium.FeatureGroup(name="Population")

#creates geojson object for polygons
fgp.add_child(folium.GeoJson(data=open(r"C:/Users/jjt45_000/Desktop/Python/MountainWebMap/world.json", 'r', 
encoding='utf-8-sig').read(), style_function=lambda x: {'fillColor':'green' if x['properties']['POP2005'] < 10000000
else 'orange' if 10000000 <= x['properties']['POP2005'] < 20000000 else 'red'}))


map.add_child(fgv)
map.add_child(fgp)
map.add_child(folium.LayerControl()) #put after you add the feature group
map.save("Map1.html")
#Add points


#Some Folium tips:

# Add feature group then everything below will go to that feature group. Then add map.add_child(fg name).
# You can use dir(folium)  to look for possible methods of creating circle #markers. 
# Among the methods you will see Marker, which we previously used. 
# Once you locate the method consider using the help function for that method.




