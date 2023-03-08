def directors(movies):
    return {movie.director for movie in movies}


def common_elements(xs, ys):
    return {x for x in xs if x in ys}
