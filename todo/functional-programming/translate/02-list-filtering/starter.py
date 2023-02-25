def movies_from_year(movies, year):
    result = []
    for movie in movies:
        if movie.year == year:
            result.append(movie.title)
    return result
