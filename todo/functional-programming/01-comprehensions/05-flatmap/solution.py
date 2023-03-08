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


def repeat(xs, k):
    return [
        x
        for x in xs
        for _ in range(k)
    ]
