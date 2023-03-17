from flask_restful import Resource, marshal_with, fields, reqparse
from flask_cors import cross_origin

from ..common.models import Photo
from ..common.errors import PhotoErrors as PE


post_parser = reqparse.RequestParser()
post_parser.add_argument("image_url", type=str, help="Url to Photo")
post_parser.add_argument("author_id", type=int, help="ID of User")
post_parser.add_argument("venue_id", type=int, help="ID of Venue")

photo_fields = {
    "photo": {
        "id": fields.Integer,
        "image_url": fields.String,
        "author_id": fields.Integer,
        "venue_id": fields.Integer
    }
}


class PhotosApi(Resource):
    @cross_origin()
    @marshal_with(photo_fields)
    def get(self, venueId):
        image = Photo.query.filter_by(venue_id=venueId).all()
        if not image:
            PE.abort_if_venue_has_no_photos(venueId)
        return image, 200

    @marshal_with(photo_fields)
    def post(self, venueId):
        data = post_parser.parse_args()
        image = Photo(
            image_url=data.image_url, author_id=data.author_id, venue_id=venueId)
        try:
            image.insert()
        except:
            PE.abort_if_photo_wasnt_added()
        return image, 201


class PhotoApi(Resource):
    @cross_origin()
    @marshal_with(photo_fields)
    def get(self, pk, venueId):
        image = Photo.query.filter_by(
            venue_id=venueId).filter_by(id=pk).first()
        if not image:
            PE.abort_if_photo_doesnt_exist(pk)
        return image, 200

    @marshal_with(photo_fields)
    def put(self, pk, venueId):
        data = post_parser.parse_args()
        try:
            image = Photo.query.filter_by(
                venue_id=venueId).filter_by(id=pk).first()
            if data.image_url:
                image.image_url = data.image_url
            elif data.venue_id:
                image.venue_id = data.venue_id
            image.update()
        except:
            PE.abort_if_photo_doesnt_exist(pk)
        return image, 200

    @marshal_with(photo_fields)
    def delete(self, pk, venueId):
        try:
            image = Photo.query.get(pk)
            image.delete()
        except:
            PE.abort_if_photo_doesnt_exist(pk)
        images = Photo.query.filter_by(venue_id=venueId).all()
        return images, 204
