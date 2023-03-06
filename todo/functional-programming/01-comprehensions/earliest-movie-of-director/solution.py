def earliest_movie_of_director(movies, director):
    return min([movie for movie in movies if movie.director==director], key=lambda movie: movie.year).title
