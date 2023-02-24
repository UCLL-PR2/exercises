def directors(movies):
    result = set()
    for movie in movies:
        result.add(movie.director)
    return result
