def genres(movies):
    return {
        genres
        for movie in movies
        for genre in movie.genre
    }


def actors(movies):
    return {
        actor
        for movie in movies
        for actor in movie.actors
    }
