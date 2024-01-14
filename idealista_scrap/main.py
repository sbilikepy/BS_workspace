import api_access.secret
from api_access.secret import apikey, secret
import requests
import base64
import json


def main():
    # Error handling
    try:
        apikey = "f8axl8z51v4pjpdarvosdgufrkc2bre7"
        secret = "JVXEDkENILNo"
        access_token = get_auth(apikey, secret, creds.OATH_URL)

        sess = create_session(access_token["access_token"])
        loc, op, ptype, country, dist = read_filter_params("filters.json")

        base_url = "https://api.idealista.com/3.5"  # Base URL for the API
        endpoint = f"/{country}/search"  # Endpoint for the property search

        # Construct the full URL
        full_url = f"{base_url}{endpoint}?center={loc}&operation={op}&propertyType={ptype}&country={country}&maxItems=50&distance={dist}"

        resp = sess.post(full_url)

        print(f"HTTP Status Code: {resp.status_code}")
        print("Response Body:")
        print(resp.text)

        search_response = json.loads(resp.text)

        properties = search_response.get("elementList", [])[
            :5
        ]  # Get the first 5 properties

        print("Fetched 5 properties:")
        for property_data in properties:
            print(property_data)

    except requests.exceptions.HTTPError as error:
        print(f"HTTP error occurred: {error}")
    except Exception as error:
        print(f"Other error occurred: {error}")


if __name__ == "__main__":
    main()
