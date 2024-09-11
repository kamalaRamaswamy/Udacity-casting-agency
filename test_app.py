import os
from app import create_app
from models import setup_db, Movie, Actor
import unittest
import json
from dotenv import load_dotenv

load_dotenv()
database_username = os.getenv("database_username")
database_password = os.getenv("database_password")
database_name = os.getenv("database_name")


test_actor = Actor(
    name='aaa',
    age='32',
    gender='female')

test_movie = Movie(
    title='Home Alone',
    release_data='2000-03-08')

class CapstoneTest(unittest.TestCase):
    def setUp(self):

        DB_PATH = os.getenv("database_username")
        producer_token = os.getenv("PRODUCER_TOKEN")
        self.app = create_app()
        self.client = self.app.test_client
        self.producer_token = producer_token
        self.test_actor_data = {"name": "Vanessa", "age": 32, "gender":"female"}
        self.test_movie_data = {"title": "Mission Impossible", "release_data":"2018-08-31"}


    def tearDown(self):
        """Executed after each test"""
        pass


    def test_get_actors(self):
        response = self.client().get('/actors',
            headers={'Authorization': f'Bearer {self.producer_token}'})
        data = json.loads(response.data)

        self.assertEqual(response.status_code, 200)

    def test_get_movies(self):
        response = self.client().get('/movies',
            headers={'Authorization': f'Bearer {self.producer_token}'})
        data = json.loads(response.data)

        self.assertEqual(response.status_code, 200)


    def test_post_actor(self):
        response = self.client().post('/actors',
            json=self.test_actor_data,
            headers={'Authorization': f'Bearer {self.producer_token}'})

        data = json.loads(response.data)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(data['name'], 'Vanessa')
        self.assertEqual(data['age'], 32)
        self.assertEqual(data['gender'], 'female')

    def test_post_movie(self):
        response = self.client().post('/movies',
            json=self.test_movie_data,
            headers={'Authorization': f'Bearer {self.producer_token}'})

        data = json.loads(response.data)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(data['title'], 'Mission Impossible')
        self.assertEqual(data['release_data'],'2018-08-31')

    
    def test_patch_actor(self):
        new_actor = {"name": "Lily", "age": 19, "gender": "female"}
        response = self.client().patch('/actors/1',
            json=new_actor,
            headers={'Authorization': f'Bearer {self.producer_token}'})

        data = json.loads(response.data)
        self.assertEqual(response.status_code, 200)

    def test_post_actor_fail(self):
        response = self.client().post('/actors',
            json=self.test_actor_data)

        data = json.loads(response.data)
        self.assertEqual(response.status_code, 500)

    def test_post_movie_fail(self):
        response = self.client().post('/movies',
            json=self.test_actor_data)

        data = json.loads(response.data)
        self.assertEqual(response.status_code, 500)


if __name__ == "__main__":
    unittest.main()