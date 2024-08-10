import folium, pandas
from apiFetcher import apiFetcher
import formatCoords
from decimal import Decimal
# ---------- BELOW IS THE REQS FOR ADDING NEW TILEMAPS ---------- #
# attr = (
#     '&copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> '
#     'contributors, &copy; <a href="https://cartodb.com/attributions">CartoDB</a>'
# )
# tiles = "https://{s}.basemaps.cartocdn.com/light_nolabels/{z}/{x}/{y}.png"

# ---------- INSTANTIATING MAP OBJECT ---------- #
# map = folium.Map(location=[37.33528976604971, -121.88103394908227], zoom_start=8, tiles=tiles, attr=attr); # This is a custom/imported tileset
map = folium.Map(location=[37.33528976604971, -121.88103394908227], zoom_start=8, tiles="Cartodb Positron"); # This is a builtin tileset

# ---------- ADDING LOCAL DATA FILE IMPORTS ---------- #
projDir = "./App1_InteractiveMap/";
dfParentDirs = projDir + "data_files/";
mpParentDirs = projDir + "map_files/";

volcanoesDf = pandas.read_csv(dfParentDirs + "Volcanoes.txt");
vLat = list(volcanoesDf["LAT"]);
vLon = list(volcanoesDf["LON"]);
vName = list(volcanoesDf["NAME"]);
vElev = list(volcanoesDf["ELEV"]);

# ---------- ADDING API DATA FILE IMPORTS ---------- #
usCapitals = apiFetcher('https://parseapi.back4app.com/classes/Capitals?limit=50', 
        {'X-Parse-Application-Id': '6a2NWTwXRlwc1BynCf46kYZG1VeWp170GYjZIeXK',  # This is the fake app's application id
        'X-Parse-Master-Key': 'WEYdiGWSz0gt91skfDe03wX9yqikQTpiVc9Vn2An'        # This is the fake app's readonly master key}
        });
for i in range(50):
    usCapitals.at[i, 'latitude'] = formatCoords.fixCoord(list(usCapitals["latitude"])[i])
    usCapitals.at[i, 'longitude'] = formatCoords.fixCoord(list(usCapitals["longitude"])[i])
cLat = list(usCapitals["latitude"]);
cLon = list(usCapitals["longitude"]);
cCapital = list(usCapitals["capital"]);
cState = list(usCapitals["StateName"]);
cWebSite = list(usCapitals["website"]);

# ---------- PERSONALISED POPUPS ---------- #
# Utilizes HTML
capitalsHtml = """
<h5>State Capital of %s:</h4>
<h4>Capital Name: <a href="%s" target="_blank">%s</a><br></h4>\n
"""
volcanosHtml = """
<h5>Volcano information:</h>
<h4>Name: <a href="https://www.google.com/search?q=%%22%s%%22" target="_blank">%s</a><br></h4>\n
Height: %s m
"""

# ---------- SPECIALIZED FUNTIONS ---------- #
# Volcano color mapper
def color_producer(el):
    if el < 1500:
        return "green"
    elif 1500 <= el < 3000:
        return "orange"
    else:
        return "red" 

# ---------- ADDING CHILDREN TO MAP OBJECT(S) ---------- #
# Adding map children (may add directly to map -> map.add_child(...), but it is better practice to add to a feature group, then add that 
# feature group as a child instead. Adding a feature group this way is also essential for later on when making a control layer.)
fg = folium.FeatureGroup(name = "myMap");

# Add Volcanoes as markers
for lt, ln, nm, el in zip(vLat, vLon, vName, vElev):
    iframe = folium.IFrame(html=volcanosHtml % (nm, nm, str(el)), width=200, height=115) # use popup = folium.Popup(iframe), to use this
    fg.add_child(folium.CircleMarker(location = [lt, ln], popup = folium.Popup(iframe), radius = 6, color = "black", opacity = 0.6, 
        fill_opacity = 0.7, fill_color =
        #'green' if el < 1500 else ('orange' if el < 3000 else 'red') # OR below V
        color_producer(el) # OR above ^
         ));
print(cLat)
# Add Volcanoes as markers
for lt, ln, cp, st, wb in zip(cLat, cLon, cCapital, cState, cWebSite):
    print(f"{st}->{cp}: ({str(lt)}, {str(ln)})")
    iframe = folium.IFrame(html=capitalsHtml % (st, wb, cp), width=200, height=115) # use popup = folium.Popup(iframe), to use this
    # popup_text = nm + "\n Elevation: " + str(el) + " m"; # use popup = popup_text, to use this
    fg.add_child(folium.Marker(location = [lt, ln], popup= folium.Popup(iframe), icon = folium.Icon("blue", icon="star")));

# Add all markers to map
map.add_child(fg);

# ---------- SAVING MAP OBJECT(S) TO CORRECT FILE LOCATION ---------- #
map.save(mpParentDirs + "TestMap1.html")