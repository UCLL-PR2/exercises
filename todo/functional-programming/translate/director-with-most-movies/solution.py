def director_with_most_movies(movies):
    return max(
        {movie.director for movie in movies},
        key=lambda director: len([movie for movie in movies if movie.director==director])
    )
