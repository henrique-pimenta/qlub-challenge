from apiflask import APIBlueprint
from flask import current_app, request, Response
from helpers import *
from schemas.closest_restaurant_schemas import *
import dotenv, json, os


dotenv.load_dotenv()
google_api_key = os.getenv('GOOGLE_API_KEY')


views = APIBlueprint('views', __name__)

@views.route('/')
@views.input(InputClosestRestaurantSchema, location="query")
@views.output(OutputClosestRestaurantSchema)
def closest_restaurant_view(self):
    if not google_api_key:
        return Response('Environment variable GOOGLE_API_KEY not set.', status=401)

    city = request.args.get('city')
    reference = (
        request.args.get('lat'),
        request.args.get('long')
    )

    current_app.logger.info(
        'Running "closest_restaurant_view" with '
        f'city={city} '
        f'and reference={reference}.'
    )

    restaurants = list_up_to_60_restaurants(city, google_api_key)
    if not restaurants:
        return Response('No restaurant found.', status=404)
    return Response(
        json.dumps(get_closest_restaurant(restaurants, reference)),
        status=200,
        content_type='application/json'
    )
