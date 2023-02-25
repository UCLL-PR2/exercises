def movies_with_actor(movies, actor):
    result = []
    for movie in movies:
        if actor in movie.actors:
            result.append(movie.title)
    return result
