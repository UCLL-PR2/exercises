def titles(movies):
    return [movie.title for movie in movies if movie.year < 2000]
