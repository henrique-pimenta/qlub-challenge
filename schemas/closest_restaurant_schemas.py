from apiflask import Schema
from apiflask.fields import Float, Integer, Nested, String


class InputClosestRestaurantSchema(Schema):
    city = String(required=True)
    lat = Float(required=True)
    long = Float(required=True)


class NestedPositionSchema(Schema):
    lat = Float()
    long = Float()


class OutputClosestRestaurantSchema(Schema):
    name = String()
    geodesic_distance_from_reference = Integer()
    position = Nested(nested=NestedPositionSchema)
