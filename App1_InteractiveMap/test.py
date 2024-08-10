import pandas
from apiFetcher import apiFetcher

# projDir = "./App1_InteractiveMap/"
# usCapitalsDf = pandas.read_csv(projDir + "data_files/simplemaps_worldcities_basicv1.77/worldcities.csv")
# usCapitalsDf_US = usCapitalsDf[(usCapitalsDf["country"]=="United States") & (usCapitalsDf["capital"]=="state")]
# usCapitalsDf_US = usCapitalsDf_US.sort_values(by="city_ascii", ascending=True)
# cLat = list(usCapitalsDf_US["lat"]);
# cLon = list(usCapitalsDf_US["lng"]);
# cCapitaleName = list(usCapitalsDf_US["city"]);
# cStateName = list(usCapitalsDf_US["admin_name"]);
# cStateKey = list(usCapitalsDf_US["capital"]);
# # print(usCapitalsDf)
# print(usCapitalsDf_US)

usCapitalsAPIDf = apiFetcher(
    'https://parseapi.back4app.com/classes/Capitals',
    {
       'X-Parse-Application-Id': '6a2NWTwXRlwc1BynCf46kYZG1VeWp170GYjZIeXK', # This is the fake app's application id
       'X-Parse-Master-Key': 'WEYdiGWSz0gt91skfDe03wX9yqikQTpiVc9Vn2An' # This is the fake app's readonly master key\
    }
)
# cWebSite = list(usCapitalsAPIDf[we])
print(usCapitalsAPIDf.columns)

