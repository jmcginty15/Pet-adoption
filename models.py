"""Models for pet adoption app"""

from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

def connect_db(app):
    """Connect to database."""

    db.app = app
    db.init_app(app)

class Pet(db.Model):
    """Pet"""

    __tablename__ = 'Pets'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(), nullable=False)
    species = db.Column(db.String(), nullable=False)
    photo_url = db.Column(db.String, default='https://thumbs.dreamstime.com/b/no-image-available-icon-photo-camera-flat-vector-illustration-132483141.jpg')
    age = db.Column(db.Integer)
    notes = db.Column(db.String)
    available = db.Column(db.Boolean, default=True)

    def __repr__(self):
        """Show info about user."""
        url = self.photo_url[0:20] + '...'
        return f'<Pet id: {self.id}, name: {self.name}, species: {self.species}, photo_url: {url}, age: {self.age}, notes: {self.notes}, available: {self.available}>'
