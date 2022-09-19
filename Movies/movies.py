from flask import Flask,request,jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_restful import Api,Resource
from http import HTTPStatus

app = Flask(__name__)
api = Api(app)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:welcome$1234@localhost/MovieDatabase'
db = SQLAlchemy(app)

class Movie(db.Model):
    id = db.Column(db.Integer,primary_key = True)
    title = db.Column(db.String(80), nullable = False)
    year = db.Column(db.Integer, nullable = False)
    genre = db.Column(db.String(80), nullable=False)

    @staticmethod
    def add_movie(title,year,genre):
        new_movie = Movie(title=title,year=year,genre=genre)
        db.session.add(new_movie)
        db.session.commit()

    @staticmethod
    def get_movie():
        data = Movie.query.all()
        return data

    @staticmethod
    def get_movieId(id):
        data = Movie.query.filter_by(id=id).first()
        print(data)
        return data

    @staticmethod
    def update_movie(id):
        data = Movie.query.filter_by(id=id).update(request.get_json())
        db.session.commit()
        return jsonify(data)

    @staticmethod
    def count_movies():
        count = Movie.query.count()
        return count

    @staticmethod
    def delete_movie(id):
        # data = Movie.get_movieId(id)
        data = Movie.query.filter_by(id=id).delete()
        db.session.commit()

class AllMovies(Resource):
    def get(self):
        data = Movie.get_movie()
        print(data)
        return jsonify(data)

    def post(self):
        data = request.get_json()
        Movie.add_movie(title=data["title"],year=data["year"],genre=data["genre"])
        return jsonify(Movie.get_movie())

        # movie_list = []
        # for i in data:
        #     movie = {"title": i.title, "year": i.year, "genre": i.genre}
        #     movie_list.append(movie)
        # return movie_list

class OneMovie(Resource):
    def get(self,id):
        movie= Movie.get_movieId(id)
        # movie = {}
        # for i in movie_list:
        #     if i["id"]== id:
        #         movie['title']=i.title
        #         movie['year'] = i.year
        #         movie['genre'] = i.genre
        print(movie)
        if movie:
            return jsonify(movie,{"status":HTTPStatus.OK})
        else:
            return jsonify({"message":"Not found in Movie Database"})

        # d = {}
        # data = Movie.get_movieId(id)
        # if data:
        #     d["title"] = data.title
        #     d["year"] = data.year
        #     d["genre"] = data.genre
        #
        # return

    def delete(self,id):
        # movie = request.get_json()
        # for i in movie:
        #     if i["id"] == id:
        #         movie.remove(i)
        #         return movie

        movie = Movie.delete_movie(id)
        if movie:
            return HTTPStatus.OK
        else:
            return HTTPStatus.NOT_FOUND

    def put(self,id):
        data = request.get_json()
        movie = Movie.update_movie(id)
        return jsonify(movie,{"message":"Updated Successfully","Status":HTTPStatus.OK})

api.add_resource(AllMovies,"/movies")
api.add_resource(OneMovie,"/movies/<int:id>")
app.run()
