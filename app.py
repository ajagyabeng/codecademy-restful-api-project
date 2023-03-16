from api import create_app
from flask_restful import Api
from api.resources.venues_api import VenuesApi, VenueApi
from api.resources.users_api import UsersApi, UserApi
from api.resources.photos_api import PhotosApi, PhotoApi

app = create_app()

api = Api(app)

"""Resources for Venues"""
api.add_resource(VenuesApi, "/api/venues")
api.add_resource(VenueApi, "/api/venues/<int:pk>")

"""Resources for Users"""
api.add_resource(UsersApi, "/api/users")
api.add_resource(UserApi, "/api/users/<int:pk>")

"""Resources for Photos"""
api.add_resource(PhotosApi, "/api/venues/<int:venueId>/photos")
api.add_resource(PhotoApi, "/api/venues/<int:venueId>/photos/<int:pk>")


if __name__ == "__main__":
    app.run(debug=True, port=8080)
