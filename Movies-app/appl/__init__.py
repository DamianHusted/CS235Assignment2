import os

from flask import Flask, render_template, request
# from wtforms import Form
import appl.adaptors.repository as repo
from appl.adaptors.memory_repository import MemoryRepository, read_and_load_user_file, read_and_load_movie_file




def create_app():
    app = Flask(__name__)

    app.config.from_object('config.Config')
    data_path = os.path.join('appl', 'adaptors', 'datafiles')

    repo.repo_instance = MemoryRepository()
    read_and_load_movie_file("appl/datafiles/Data1000Movies.csv", repo.repo_instance)
    read_and_load_user_file("appl/datafiles/users.csv", repo.repo_instance)
    

    @app.route("/", methods=["POST", "GET"])
    def home():
        movie_list = repo.repo_instance.get_movies()
        actor_list = repo.repo_instance.get_actors()
        director_list = repo.repo_instance.get_directors()
        genre_list = repo.repo_instance.get_genres()
        review_list = repo.repo_instance.get_reviews()
        watchlist_list = repo.repo_instance.get_watchlists()
        return render_template("home.html", movies=movie_list, actors=actor_list, directors=director_list, genres=genre_list, reviews=review_list, watchlists=watchlist_list)



    @app.route("/login")
    def login():
        return render_template("login.html")


    return app