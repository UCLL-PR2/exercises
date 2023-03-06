def titles(movies):
    result = []
    for movie in movies:
        result.append(movie.title)
    return result


def titles_and_years(movies):
    result = []
    for movie in movies:
        pair = (movie.title, movie.year)
        result.append(pair)
    return result


def titles_and_actor_counts(movies):
    result = []
    for movie in movies:
        pair = (movie.title, len(movie.actors))
        result.append(pair)
    return result


def longest_runtime(movies):
    result = []
    for movie in movies:
        result.append(movie.runtime)
    return max(result)
