def group_movies_by_year(movies):
    result = {}
    for movie in movies:
        result.setdefault(movie.year, []).append(movie.title)
    return result
