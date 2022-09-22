import flask, json, requests, time


def list_up_to_60_restaurants(city, google_api_key):
    flask.current_app.logger.info(f'Running "list_up_to_60_restaurants" with city={city}.')

    restaurants = []
    page_token = ''
    base_url = (
        'https://maps.googleapis.com/maps/api/place/textsearch/json'
        f'?type=restaurant&query=city+{city}&key={google_api_key}'
    )

    for delay in (2, 2, 0): # minimum (integer) delays required by Google Places API.
        places_api_url = f'{base_url}&pagetoken={page_token}'
        response_dict = json.loads(requests.get(places_api_url).text)
        restaurants += response_dict.get('results', [])

        page_token = response_dict.get('next_page_token')
        if page_token:
            time.sleep(delay)
        else:
            break

    return restaurants
