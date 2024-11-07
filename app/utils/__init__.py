import requests
import json
import config

# The URL for the Google Places API
url = 'https://places.googleapis.com/v1/places:searchNearby'

# Request payload
data = {
    "includedTypes": ["hotel"],
    "maxResultCount": 100,
    "locationRestriction": {
        "circle": {
            "center": {
                "latitude": 37.983768,
                "longitude": 23.727909
            },
            "radius": 500
        }
    }
}

# Headers including the API Key and Field Mask
headers = {
    'Content-Type': 'application/json',
    'X-Goog-Api-Key': config.PLACES_API_KEY,  # Replace 'YOUR_API_KEY' with your actual API key
    'X-Goog-FieldMask': 'places.displayName,places.formattedAddress,places.types,places.websiteUri'
}

# Send the POST request
response = requests.post(url, headers=headers, json=data)

# Handle the response
if response.status_code == 200:
    places = response.json().get('places', [])
    if places:
        print(len(place))
        for place in places:
            print(f"Name: {place.get('displayName')}, Address: {place.get('formattedAddress')}, Types: {place.get('types')}, Website: {place.get('websiteUri')}")
    else:
        print("No results found.")
else:
    print(f"Error {response.status_code}: {response.text}")
