from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

from dotenv import find_dotenv, load_dotenv
import os

# Locate .env file
dotenv_path = find_dotenv()
load_dotenv(dotenv_path)

db = SQLAlchemy()
migrate = Migrate()


class Venue(db.Model):
    __tablename__ = "venue"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(150))
    address = db.Column(db.String(150))
    photos = db.relationship("Photo")

    def __init__(self, name, address):
        self.name = name
        self.address = address

    def insert(self):
        """Inserts a contact to the database"""
        db.session.add(self)
        db.session.commit()

    def update(self):
        """Updates a contact in the database"""
        db.session.commit()

    def delete(self):
        """Deletes a contact from the database"""
        db.session.delete(self)
        db.session.commit()


class User(db.Model):
    __tablename__ = "user"
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(150))
    password = db.Column(db.String(150))
    photos = db.relationship("Photo")

    def __init__(self, username, password):
        self.username = username
        self.password = password

    def insert(self):
        """Inserts a contact to the database"""
        db.session.add(self)
        db.session.commit()

    def update(self):
        """Updates a contact in the database"""
        db.session.commit()

    def delete(self):
        """Deletes a contact from the database"""
        db.session.delete(self)
        db.session.commit()


class Photo(db.Model):
    __tablename__ = "photos"
    id = db.Column(db.Integer, primary_key=True)
    image_url = db.Column(db.String(250))
    author_id = db.Column(db.Integer, db.ForeignKey("user.id"))
    venue_id = db.Column(db.Integer, db.ForeignKey("venue.id"))

    def __init__(self, image_url, author_id, venue_id):
        self.image_url = image_url
        self.author_id = author_id
        self.venue_id = venue_id

    def insert(self):
        """Inserts a contact to the database"""
        db.session.add(self)
        db.session.commit()

    def update(self):
        """Updates a contact in the database"""
        db.session.commit()

    def delete(self):
        """Deletes a contact from the database"""
        db.session.delete(self)
        db.session.commit()


def setup_db(app):
    app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///venues.db"
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    db.init_app(app)
    migrate.init_app(app)
    with app.app_context():
        db.create_all()
