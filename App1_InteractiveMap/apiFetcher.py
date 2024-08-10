import requests
import pandas as pd

def apiFetcher(api_url, given_headers=None):
    # API endpoint and headers
    url = api_url
    headers = given_headers

    # Fetch data from the API
    try:
        if headers:
            response = requests.get(url, headers=headers)
        else:
            response = requests.get(url)

        # Ensure the request was successful
        if response.status_code == 200:
            data = response.json()  # Directly get the JSON response
            
            # If data is a dictionary and has a 'results' key
            if isinstance(data, dict):
                results = data.get('results', data)  # Use 'results' if present, otherwise use data
            
            # If data is a list, use it directly
            elif isinstance(data, list):
                results = data
            
            else:
                print("Unexpected data format")
                return None

            # Convert to DataFrame
            apidf = pd.DataFrame(results)
                        
            return apidf
        else:
            print(f"Failed to fetch data: {response.status_code}")
            return None  # Return None if the request failed
            
    except Exception as e:
        print(f"An error occurred: {e}")
        return None  # Return None in case of exception
