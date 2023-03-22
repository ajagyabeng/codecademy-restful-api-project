from flask_restful import Resource, marshal_with, fields, reqparse
from flask import request
from flask_cors import cross_origin

from ..common.models import Venue
from ..common.errors import VenueErrors as VE


"""reqparse: """
post_parser = reqparse.RequestParser()
post_parser.add_argument("name", type=str, help="Name of Venue")
post_parser.add_argument("address", type=str, help="Street Adress")

"""dict of how you want the api data to be returned"""
venue_fields = {
    "venue": {
        "id": fields.Integer,
        "name": fields.String,
        "address": fields.String
    }
}


class VenuesApi(Resource):
    """Venues resource that handles requests to get all venues and request to add a venue"""
    @cross_origin()
    @marshal_with(venue_fields)
    def get(self):
        """
        Handles get requests
        returns: All the venues in database
        """
        venues = Venue.query.all()
        return venues, 200

    @marshal_with(venue_fields)
    def post(self):
        """
        Handles post requests to add a venue to the database.
        returns: All the venues in database
        """
        data = post_parser.parse_args()
        venue = Venue(name=data.name, address=data.address)
        venue.insert()
        return {
            "message": "Success! The venue has been added to the database."
        }, 201


class VenueApi(Resource):
    """
    Venue resource that handles get, put, and delete requests on individual venues.
    pk: primary_key
    """
    @cross_origin()
    @marshal_with(venue_fields)
    def get(self, pk):
        """
        Handle get requests.
        returns: A venue with the ID provided.
        """
        venue = Venue.query.get(pk)
        if not venue:
            VE.abort_if_venue_doesnt_exist(pk)
        return venue, 200

    @marshal_with(venue_fields)
    def put(self, pk):
        """
        Handle put requests to update a venue.
        returns: A venue with the ID provided.
        """
        data = post_parser.parse_args()
        venue = Venue.query.get(pk)
        if data.name:
            venue.name = data.name
        elif data.address:
            venue.address = data.address
        venue.update()
        return venue, 200

    @marshal_with(venue_fields)
    def delete(self, pk):
        """
        Handle delete requests.
        returns: All venues in the database.
        """
        venue = Venue.query.get(pk)
        if not venue:
            VE.abort_if_user_doesnt_exist(pk)
        venue.delete()
        return {
            "message": "Success! The venue has been deleted."
        }, 204
