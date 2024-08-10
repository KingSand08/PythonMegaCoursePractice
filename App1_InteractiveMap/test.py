import http.client
from apiFetcher import apiFetcher
import pandas
import json

# Convert to DataFrame
# apidf = pandas.DataFrame(data)  # Convert to DataFrame

# Print the columns
# print("Columns in the DataFrame:")
# print(apidf)

# print(data.decode("utf-8"))
  
usCapitals = apiFetcher('https://freetestapi.com/api/v1/us-states');
print(usCapitals.columns)
# print(usCapitals['longitude'])
# cLng = list(usCapitals["longitude"]);
# print(usCapitals['latitude'])
# cLat = list(usCapitals["latitude"]);
