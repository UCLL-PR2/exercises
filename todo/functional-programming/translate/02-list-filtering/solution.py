def from_previous_century(movies):
    return [movie.title for movie in movies if movie.year < 2000]
