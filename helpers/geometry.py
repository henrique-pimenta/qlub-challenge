from geopy.distance import geodesic # based on an ellipsoidal model of the Earth.


def get_closest_restaurant(restaurants, reference):
    distances = [
        geodesic(reference, get_position_coordinates(restaurant)).m
        for restaurant in restaurants
    ]

    shortest_distance = min(distances)
    closest_restaurant = restaurants[distances.index(shortest_distance)] # both lists have the same size and order.

    return {
        "name": closest_restaurant.get('name'),
        "geodesic_distance_from_reference": f'{int(shortest_distance)} m',
        "position": {
            "lat": get_position_coordinates(closest_restaurant)[0],
            "long": get_position_coordinates(closest_restaurant)[1]
        }
    }


def get_position_coordinates(restaurant):
    position = restaurant.get('geometry').get('location')
    return (position['lat'], position['lng'])
