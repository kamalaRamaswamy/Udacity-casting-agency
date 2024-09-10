import os
from flask import Flask, request, jsonify, abort
from sqlalchemy import exc
import json
from flask_cors import CORS

from models import setup_db, Actor, Movie
from auth import AuthError, requires_auth


QUESTIONS_PER_PAGE = 10

def paginate_questions(request, data):
    page = request.args.get('page', 1, type=int)
    start = (page -1 ) * QUESTIONS_PER_PAGE
    end = start + QUESTIONS_PER_PAGE
    data = [item.format() for item in data]
    return data[start:end]

def create_app(test_config=None):
    # create and configure the app
    app = Flask(__name__)

    if test_config is None:
        setup_db(app)
    else:
        # database_path = test_config.get('SQLALCHEMY_DATABASE_URI')
        setup_db(app, database_path=test_config)

    """
    @TODO: Set up CORS. Allow '*' for origins. Delete the sample route after completing the TODOs
    """
    CORS(app)

    """
    @TODO: Use the after_request decorator to set Access-Control-Allow
    """
    @app.after_request
    def after_request(response):
        response.headers.add('Access-Control-Allow-Headers', 'Content-Type,Authorization,true')
        response.headers.add('Access-Control-Allow-Methods', 'GET,POST,DELETE')
        return response

    
    @app.route('/actors', methods=['GET'])
    @requires_auth('get:actors')
    def get_actors_info(payload):
        actors_query = Actor.query.all()
        actors_result = [actor.get_info() for actor in actors_query]
        return jsonify({
          "actors": actors_result})

      
    @app.route('/movies', methods=['GET'])
    @requires_auth('get:movies')
    def get_movies_info(payload):
        movies_query = Movie.query.all()
        movies_result = [movie.get_info() for movie in movies_query]
        return jsonify({
          "movies": movies_result})


    @app.route('/actors/<id>', methods=['DELETE'])
    @requires_auth('delete:actors')
    def delete_actors_info(id):
        actor = Actor.query.get(id)
        if actor is None:
            abort(404)
        try:
            actor.delete()
        except Exception:
            abort(500)
        return jsonify({
          "success": True
        })


    @app.route('/movies/<id>', methods=['DELETE'])
    @requires_auth('delete:movies')
    def delete_movies_info(id):
        movie = Movie.query.get(id)
        if movie is None:
            abort(404)
        try:
            movie.delete()
        except Exception:
            abort(500)
        return jsonify({
          "success": True
        })


    @app.route('/actors', methods=['POST'])
    @requires_auth('post:actors')
    def post_actors_info(payload):
        actor = request.get_json()
        print('post actor', actor)
    
        try:
            if 'id' in actor:
                actor_ins = Actor(id=actor['id'], name=actor['name'], age=actor['age'], gender=actor['gender'])
            else:
                actor_ins = Actor(name=actor['name'], age=actor['age'], gender=actor['gender'])       
        except Exception:
            abort(422)
        try:
            actor_ins.insert()
        except Exception:
            abort(500)
        return jsonify(actor)


    @app.route('/movies', methods=['POST'])
    @requires_auth('post:movies')
    def post_movies_info(payload):
        try:
            movie = request.get_json()
        except Exception:
            abort(400)
        try:
            if 'id' in movie:
                movie_ins = Movie(id=movie['id'], title=movie['title'], release_data=movie['release_data'])
            else:
                movie_ins = Movie(title=movie['title'], release_data=movie['release_data'])
        except Exception:
            abort(422)
        try:
            movie_ins.insert()
        except Exception:
            abort(500)
        return jsonify(movie)


    @app.route('/actors/<int:id>', methods=['PATCH'])
    @requires_auth('patch:actors')
    def patch_actors_info(payload, id):
        try:
            actor = Actor.query.get(id)
        except Exception:
            abort(404)
        try:
            patch_info = request.get_json()
            print('patch info', patch_info)
        except Exception:
            abort(400)

        try:
            name = patch_info.get('name', None)
            print('patch name', name)
            age = patch_info.get('age', None)
            gender = patch_info.get('gender', None)
            actor = Actor(id=id, name=name, age=age, gender=gender)
            actor.update()
        except:
            abort(422)
        return jsonify({
          "success": True
        })


    @app.route('/movies/<id>', methods=['PATCH'])
    @requires_auth('patch:movies')
    def patch_movies_info(id):
        try:
            movie = Movie.query.get(id)
        except Exception:
            abort(404)
        try:
            patch_info = request.get_json()  
        except Exception:
            abort(400)

        try:
            title = patch_info.get('title', None)
            release_data = patch_info.get('release_data', None)

            movie = Movie(title=title, release_data=release_data)
            movie.update()
        except:
            abort(422)

        return jsonify({
          "success": True
        })


    # Error Handling
    '''
    Example error handling for unprocessable entity
    '''
    @app.errorhandler(422)
    def unprocessable(error):
        return jsonify({
                        "success": False,
                        "error": 422,
                        "message": "unprocessable"
                        }), 422


    '''
    @TODO implement error handlers using the @app.errorhandler(error) decorator
        each error handler should return (with approprate messages):
                jsonify({
                        "success": False,
                        "error": 404,
                        "message": "resource not found"
                        }), 404

    '''

    '''
        error handler for not found
    '''
    @app.errorhandler(404)
    def not_found(error):
        return jsonify({
                        "success": False,
                        "error": 404,
                        "message": "not found"
                        }), 404


    '''
      error handler for authorization error 
    '''
    @app.errorhandler(AuthError)
    def auth_error(error):
        if error.status_code == 401:
            return jsonify({
                        "success": False,
                        "error": 401,
                        "message": "unauthorized"
                        }), 401
        elif error.status_code == 403:
            return jsonify({
                        "success": False,
                        "error": 403,
                        "message": "forbidden"
                        }), 403


    '''
      error handler for internal service error
    '''
    @app.errorhandler(500)
    def internal_error(error):
        return jsonify({
                        "success": False,
                        "error": 500,
                        "message": "internal service error"
                        }), 500


    '''
      error handler for no appropriate key 
    '''
    @app.errorhandler(400)
    def no_appropriate_key(error):
        return jsonify({
                    "success": False,
                    "error": 400,
                    "message": "no appropriate key"
                    }), 400


    '''
      error handler for no processable entity
    '''
    @app.errorhandler(422)
    def unprocessable_entity(error):
        return jsonify({
                    "success": False,
                    "error": 422,
                    "message": "unprocessable entity"
                    }), 422
    

    return app

app = create_app()

if __name__ == '__main__':
    app = create_app()
    app.run(host='0.0.0.0', port=5000, debug=True)

