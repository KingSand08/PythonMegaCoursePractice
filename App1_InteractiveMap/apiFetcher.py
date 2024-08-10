import requests
import pandas

def apiFetcher(api_url, given_headers):
    # API endpoint and headers
    url = api_url
    headers = given_headers

    # Fetch data from the API
    response = requests.get(url, headers=headers)

    # Ensure the request was successful
    if response.status_code == 200:
        data = response.json()  # Directly get the JSON response
        results = data.get('results', [])  # Extract the 'results' key if it exists

        # Convert to DataFrame
        if isinstance(results, list) and len(results) > 0 and isinstance(results[0], dict):
            apidf = pandas.DataFrame(results)
        else:
            apidf = pandas.DataFrame()

        return apidf
    else:
        print(f"Failed to fetch data: {response.status_code}")
        return pandas.DataFrame()  # Return an empty DataFrame in case of failure
