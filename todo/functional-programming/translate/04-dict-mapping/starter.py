def directors(movies):
    result = {}
    for movie in movies:
        result[movie.title] = movie.director
    return result
