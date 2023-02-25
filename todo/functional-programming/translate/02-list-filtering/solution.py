def movies_from_year(movies, year):
    return [movie.title for movie in movies if movie.year == year]
