from flask_restful import abort


class UserErrors():
    def abort_if_user_doesnt_exist(pk):
        abort(404, message=f"User with ID: {pk} doesn't exist. Check user ID.")

    def abort_if_user_already_exists():
        abort(500, message=f"User already exists")


class VenueErrors():
    def abort_if_user_doesnt_exist(pk):
        abort(404, message=f"Venue with ID: {pk} doesn't exist")


class PhotoErrors():
    def abort_if_venue_has_no_photos(venueId):
        abort(404, message=f"Venue with ID: {venueId} doesn't have any photos")

    def abort_if_photo_doesnt_exist(pk):
        abort(
            404, message=f"Photo with ID: {pk} doesn't exist. Check venue ID or photo ID.")

    def abort_if_photo_wasnt_added():
        abort(500, message=f"Photo wasn't added to database.")
