def movies_with_actor(movies, actor):
    return [movie.title for movie in movies if actor in movie.actors]
