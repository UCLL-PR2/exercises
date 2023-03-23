from util import Card


def genres(movies):
    return {
        genre
        for movie in movies
        for genre in movie.genres
    }


def actors(movies):
    return {
        actor
        for movie in movies
        for actor in movie.actors
    }


def repeat_consecutive(xs, k):
    return [
        x
        for x in xs
        for _ in range(k)
    ]


def repeat_alternating(xs, k):
    return [
        x
        for _ in range(k)
        for x in xs
    ]


def cards(values, suits):
    return {
        Card(value, suit)
        for value in values
        for suit in suits
    }
