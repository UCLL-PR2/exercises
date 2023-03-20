def title_to_director(movies):
    return {movie.title: movie.director for movie in movies}


def director_to_titles(movies):
    return {
        movie.director: {movie.title for m in movies if m == movie.director}
        for movie in movies
    }
