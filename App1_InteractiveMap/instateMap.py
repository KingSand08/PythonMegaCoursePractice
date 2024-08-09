import folium, pandas
# attr = (
#     '&copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> '
#     'contributors, &copy; <a href="https://cartodb.com/attributions">CartoDB</a>'
# )
# tiles = "https://{s}.basemaps.cartocdn.com/light_nolabels/{z}/{x}/{y}.png"

# Instantiating map
# map = folium.Map(location=[37.33528976604971, -121.88103394908227], zoom_start=12);
# map = folium.Map(location=[37.33528976604971, -121.88103394908227], zoom_start=8, tiles=tiles, attr=attr); # This is a custom/imported tileset
map = folium.Map(location=[37.33528976604971, -121.88103394908227], zoom_start=8, tiles="Cartodb Positron"); # This is a builtin tileset


# Adding data file imports
projDir = "./App1_InteractiveMap/";
dfParentDirs = projDir + "data_files/";
volcanoesData = pandas.read_csv(dfParentDirs + "Volcanoes.txt");
vLat = list(volcanoesData["LAT"]);
vLon = list(volcanoesData["LON"]);
vName = list(volcanoesData["NAME"]);
vElev = list(volcanoesData["ELEV"]);

# For personalized popups we user HTML:
html = """
<h4>Volcano information:</h4>
<h5>Name: <a href="https://www.google.com/search?q=%%22%s%%22" target="_blank">%s</a><br></h5>\n
Height: %s m
"""
def color_producer(el):
    if el < 1500:
        return "green"
    elif 1500 <= el < 3000:
        return "orange"
    else:
        return "red" 

# Adding map children (may add directly to map -> map.add_child(...), but it is better practice to add to a feature group, then add that 
# feature group as a child instead. Adding a feature group this way is also essential for later on when making a control layer.)
fg = folium.FeatureGroup(name = "myMap");
    
for lt, ln, nm, el in zip(vLat, vLon, vName, vElev):
    iframe = folium.IFrame(html=html % (nm, nm, str(el)), width=200, height=115) # use popup = folium.Popup(iframe), to use this
    # popup_text = nm + "\n Elevation: " + str(el) + " m"; # use popup = popup_text, to use this
    # fg.add_child(folium.Marker(location = [lt, ln], popup= folium.Popup(iframe), icon = folium.Icon(
    #     # color= 'green' if el < 1500 else ('orange' if el < 3000 else 'red') # OR below V
    #     color= color_producer(el) # OR above ^
    #     # , icon="star" # This changes what the folium.Marker will look like
    #     )));
    fg.add_child(folium.CircleMarker(location = [lt, ln], popup= folium.Popup(iframe), radius=6, color="black", opacity=0.6, fill_color= color_producer(el), fill_opacity=0.7));


map.add_child(fg);

map.save(projDir + "TestMap1.html")