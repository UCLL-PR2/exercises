def earliest_movie_of_director(movies, director):
    earliest = None
    for movie in movies:
        if movie.director == director:
            if earliest is None or earliest.year > movie.year:
                earliest = movie
    return earliest.title
