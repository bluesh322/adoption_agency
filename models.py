from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import backref
from datetime import datetime

db = SQLAlchemy()


def connect_db(app):
    db.app = app
    db.init_app(app)

# Models go below


class Pet(db.Model):
    """Pet"""

    # @classmethod
    # def get_by_species(cls, species):
    #     return cls.query.filter_by(species=species).all()
    def __repr__(self):
        """Show info about a user"""
        p = self
        return f"<Pet {p.id} {p.name} {p.species} {p.age} {p.notes} {p.available}>"

    __tablename__ = "pets"

    id = db.Column(db.Integer,
                   primary_key=True,
                   autoincrement=True)
    name = db.Column(db.Text,
                           nullable=False)
    species = db.Column(db.Text,
                          nullable=False)
    photo_url = db.Column(db.Text)
    age = db.Column(db.Integer)
    notes = db.Column(db.Text)
    available = db.Column(db.Boolean, default=True)
