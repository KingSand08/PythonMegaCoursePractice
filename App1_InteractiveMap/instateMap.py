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
map = folium.Map(location=[37.33528976604971, -121.88103394908227], zoom_start=4, tiles="Cartodb Positron"); # This is a builtin tileset

# ---------- ADDING LOCAL DATA FILE IMPORTS ---------- #
projDir = "./App1_InteractiveMap/";
mpParentDirs = projDir + "map_files/";

volcanoesDf = pandas.read_csv(projDir + "data_files/Volcanoes.txt");
vLat = list(volcanoesDf["LAT"]);
vLon = list(volcanoesDf["LON"]);
vName = list(volcanoesDf["NAME"]);
vElev = list(volcanoesDf["ELEV"]);

# Utilizing from given API: https://simplemaps.com/data/world-cities.
capitalsDf = pandas.read_csv(projDir + "data_files/simplemaps_worldcities_basicv1.77/worldcities.csv")
capitalsDf_US = capitalsDf[(capitalsDf["country"]=="United States") & (capitalsDf["capital"]=="state")]
capitalsDf_US = capitalsDf_US.sort_values(by="city_ascii", ascending=True)
cLat = list(capitalsDf_US["lat"]);
cLon = list(capitalsDf_US["lng"]);
cCapitalName = list(capitalsDf_US["city"]);
cStateName = list(capitalsDf_US["admin_name"]);
cStateKey = list(capitalsDf_US["capital"]);

capitalsDf_Global = capitalsDf[(capitalsDf["country"]!="United States") & (capitalsDf["capital"]=="primary")]
gLat = list(capitalsDf_Global["lat"]);
gLon = list(capitalsDf_Global["lng"]);
gCapitalName = list(capitalsDf_Global["city"]);
gCountry = list(capitalsDf_Global["country"]);
gCountryKey = list(capitalsDf_Global["capital"]);

# ---------- ADDING API DATA FILE IMPORTS ---------- #
# Utilizing from given API: https://www.back4app.com/database/back4app/list-of-us-states-and-capitals
usCapitalsAPIDf = apiFetcher(
    'https://parseapi.back4app.com/classes/Capitals',
    {
       'X-Parse-Application-Id': '6a2NWTwXRlwc1BynCf46kYZG1VeWp170GYjZIeXK', # This is the fake app's application id
       'X-Parse-Master-Key': 'WEYdiGWSz0gt91skfDe03wX9yqikQTpiVc9Vn2An' # This is the fake app's readonly master key\
    }
)
usCapitalsAPIDf = usCapitalsAPIDf.sort_values(by="capital", ascending=True)
cAPIWebSite = list(usCapitalsAPIDf["website"])

# ---------- PERSONALISED POPUPS ---------- #
# Utilizes HTML
capitalsHtml = """
<h5>State Capital of %s:</h4>
<h4>Capital Name: <a href="https://%s" target="_blank">%s</a><br></h4>\n
"""
nationalCapitalsHtml = """
<h5>Capital of %s:</h4>
<h4>Capital Name: <a href="https://%s" target="_blank">%s</a><br></h4>\n
"""
volcanosHtml = """
<h5>Volcano information:</h>
<h4>Name: <a href="https://www.google.com/search?q=%%22%s%%22" target="_blank">%s</a><br></h4>\n
Height: %s m
"""

# ---------- SPECIALIZED FUNTIONS ---------- #
# Volcano color mapper
def volcano_color_producer(el):
    if el < 1500:
        return "green"
    elif 1500 <= el < 3000:
        return "orange"
    else:
        return "red" 
# Capital color mapper
def capital_color_producer(st):
    if st == "Washington DC":
        return "red"
    else:
        return "blue"

# ---------- ADDING CHILDREN TO MAP OBJECT(S) ---------- #
# Adding map children (may add directly to map -> map.add_child(...), but it is better practice to add to a feature group, then add that 
# feature group as a child instead. Adding a feature group this way is also essential for later on when making a control layer.)
fg = folium.FeatureGroup(name = "myMap");

# +++++ Add Volcanoes as markers +++++
for lt, ln, nm, el in zip(vLat, vLon, vName, vElev):
    iframe = folium.IFrame(html=volcanosHtml % (nm, nm, str(el)), width=200, height=115) # use popup = folium.Popup(iframe), to use this
    # popup_text = nm + "\n Elevation: " + str(el) + " m"; # use popup = popup_text, to use this
    fg.add_child(folium.CircleMarker(location = [lt, ln], popup = folium.Popup(iframe), radius = 6, color = "black", opacity = 0.6, 
        fill_opacity = 0.7, fill_color =
        #'green' if el < 1500 else ('orange' if el < 3000 else 'red') # OR below V
        volcano_color_producer(el) # OR above ^
         ));

# +++++ Add US Capitals as markers +++++
for lt, ln, cp, st in zip(cLat, cLon, cCapitalName, cStateName):
    # Find the matching row in the API DataFrame
    matching_row = usCapitalsAPIDf[usCapitalsAPIDf["StateName"] == st]
    if not matching_row.empty:
        ws = matching_row.iloc[0]["website"]  # Get the website from the matching row
    else:
        ws = f"www.google.com/search?q={st.replace(' ', '+')}"

    if(st == "District of Columbia"):
        st =  "Washington DC"
        cp = "Washington DC"
        capitalsHtml = """
<h5>USA National Capital:</h4>
<h4>Capital Name: <a href="https://%s" target="_blank">%s</a><br></h4>\n
"""
        iframe = folium.IFrame(html=capitalsHtml % (ws, cp), width=200, height=95)
    else:
        iframe = folium.IFrame(html=capitalsHtml % (st, ws, cp), width=200, height=95)

    fg.add_child(folium.Marker(location = [lt, ln], popup= folium.Popup(iframe), icon = folium.Icon(capital_color_producer(st), icon="star")));
    
# +++++ Add Global National as markers +++++
for lt, ln, ncap, cntry in zip(gLat, gLon, gCapitalName, gCountry):
    ws = f"www.google.com/search?q={ncap.replace(' ', '+') + "+capital+of+" + cntry.replace(' ', '+')}"
    iframe = folium.IFrame(html=nationalCapitalsHtml % (cntry, ws, ncap), width=200, height=95)
    fg.add_child(folium.Marker(location = [lt, ln], popup= folium.Popup(iframe), icon = folium.Icon("red", icon="flag")));
    
# Add all markers to map
map.add_child(fg);

# ---------- SAVING MAP OBJECT(S) TO CORRECT FILE LOCATION ---------- #
map.save(mpParentDirs + "TestMap1.html")