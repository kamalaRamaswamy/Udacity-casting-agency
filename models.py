import os
from sqlalchemy import Column, String, Integer, create_engine
from flask_sqlalchemy import SQLAlchemy
import json
from dotenv import load_dotenv

load_dotenv()
# database_username = os.getenv("database_username")
# database_password = os.getenv("database_password")
# database_name = os.getenv("database_name")

# database_path = 'postgresql://{}:{}@{}/{}'.format(database_username, database_password, 'localhost:5432', database_name)

database_path = os.getenv("DATABASE_URL")

db = SQLAlchemy()

"""
setup_db(app)
    binds a flask application and a SQLAlchemy service
"""
def setup_db(app, database_path=database_path):
    app.config["SQLALCHEMY_DATABASE_URI"] = database_path
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    db.app = app
    db.init_app(app)
    with app.app_context():
        db.create_all()

movie_shows = db.Table('Movie_shows',
    db.Column('movie_id', db.Integer, db.ForeignKey('Movie.id'), primary_key=True),
    db.Column('actor_id', db.Integer, db.ForeignKey('Actor.id'), primary_key=True)
)

class Movie(db.Model):
    __tablename__ = 'Movie'

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String, nullable=False)
    release_data = db.Column(db.DateTime, nullable=False)
    actors = db.relationship('Actor', secondary=movie_shows,
      backref=db.backref('movies', lazy=True))

    def __rept__(self):
        print(f'<Movie {self.id} - {self.title} - {self.release_data}>')

    def insert(self):
        db.session.add(self)
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()

    def update(self):
        db.session.commit()

    def get_info(self):
        return {
            'id': self.id,
            'title': self.title,
            'release_data': self.release_data
        }


'''
Actor
    Actors with attributes name, age and gender, it's the child class of the movie 
'''
class Actor(db.Model):
    __tablename__ = 'Actor'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    age = db.Column(db.Integer, nullable=False)
    gender = db.Column(db.String, nullable=False)

    def __rept__(self):
        print(f'<Actor {self.id} - {self.name} - {self.age} - {self.gender}>')

    def insert(self):
        db.session.add(self)
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()

    def update(self):
        db.session.commit()

    def get_info(self):
        return {
            'id': self.id,
            'name': self.name,
            'age': self.age,
            'gender': self.gender
        }