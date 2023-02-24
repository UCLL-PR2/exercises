def titles(movies):
    result = []
    for movie in movies:
        if movie.year < 2000:
            result.append(movie.title)
    return result
