import folium, pandas
from screeninfo import get_monitors
from apiFetcher import apiFetcher

# ---------- SET THE MONITOR ATTRIBUTES ---------- #
m = get_monitors()
m_width = m[0].width
m_height = m[0].height
# ---------- BELOW IS THE REQS FOR ADDING NEW TILEMAPS ---------- #
# attr = (
#     '&copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> '
#     'contributors, &copy; <a href="https://cartodb.com/attributions">CartoDB</a>'
# )
# tiles = "https://{s}.basemaps.cartocdn.com/light_nolabels/{z}/{x}/{y}.png"

# ---------- INSTANTIATING MAP OBJECT ---------- #
# map = folium.Map(location=[37.33528976604971, -121.88103394908227], zoom_start=8, tiles=tiles, attr=attr); # This is a custom/imported tileset
map = folium.Map(width = m_width, height = m_height, location=[37.33528976604971, -121.88103394908227], zoom_start = 4, min_zoom = 0.9, max_bounds=True, tiles = "Cartodb Positron"); # This is a builtin tileset
# ---------- ADDING LOCAL DATA FILE IMPORTS ---------- #
projDir = "./App1_InteractiveMap/";
filesDir = projDir + "data_files/"
mpParentDirs = projDir + "map_files/";

volcanoesDf = pandas.read_csv(filesDir + "Volcanoes.txt");
vLat = list(volcanoesDf["LAT"]);
vLon = list(volcanoesDf["LON"]);
vName = list(volcanoesDf["NAME"]);
vElev = list(volcanoesDf["ELEV"]);

# Utilizing from given API: https://simplemaps.com/data/world-cities.
capitalsDf = pandas.read_csv(filesDir + "simplemaps_worldcities_basicv1.77/worldcities.csv")
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

# +++++ Add Volcanoes as Markers +++++
fgv = folium.FeatureGroup(name = "Western US Volcanoes");
for lt, ln, nm, el in zip(vLat, vLon, vName, vElev):
    iframe = folium.IFrame(html=volcanosHtml % (nm, nm, str(el)), width=200, height=115) # use popup = folium.Popup(iframe), to use this
    # popup_text = nm + "\n Elevation: " + str(el) + " m"; # use popup = popup_text, to use this
    fgv.add_child(folium.CircleMarker(location = [lt, ln], popup = folium.Popup(iframe), radius = 6, color = "black", opacity = 0.6, 
        fill_opacity = 0.7, fill_color =
        #'green' if el < 1500 else ('orange' if el < 3000 else 'red') # OR below V
        volcano_color_producer(el) # OR above ^
         ));

# +++++ Add US Capitals as Markers +++++
fgusa = folium.FeatureGroup(name = "US State Capitals");
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

    fgusa.add_child(folium.Marker(location = [lt, ln], popup= folium.Popup(iframe), icon = folium.Icon(capital_color_producer(st), icon="star")));
    
# +++++ Add Global National as Markers +++++
fgns = folium.FeatureGroup(name = "Global State Capitals");
for lt, ln, ncap, cntry in zip(gLat, gLon, gCapitalName, gCountry):
    ws = f"www.google.com/search?q={ncap.replace(' ', '+') + "+capital+of+" + cntry.replace(' ', '+')}"
    iframe = folium.IFrame(html=nationalCapitalsHtml % (cntry, ws, ncap), width=200, height=95)
    fgns.add_child(folium.Marker(location = [lt, ln], popup= folium.Popup(iframe), icon = folium.Icon("red", icon="flag")));
    
# +++++ Add Population Layer Attriubte to map +++++
fgp = folium.FeatureGroup(name = "Global 2005 Population Map");
fgp.add_child(folium.GeoJson(data=open(filesDir + "world.json", 'r', encoding='utf-8-sig').read(),
    style_function = lambda x : {
        "fillColor" : "blue" if x["properties"]["POP2005"] < 1000000 
        else "green" if 1000000 <= x["properties"]["POP2005"] < 10000000
        else "yellow" if 10000000 <= x["properties"]["POP2005"] < 20000000
        else "orange" if 20000000 <= x["properties"]["POP2005"] < 40000000 
        else "red" }))
    
# Add All Layers to map
map.add_child(fgv);
map.add_child(fgusa);
map.add_child(fgns);
map.add_child(fgp);

map.add_child(folium.LayerControl());

# ---------- SAVING MAP OBJECT(S) TO CORRECT FILE LOCATION ---------- #
map.save(mpParentDirs + "TestMap1.html")