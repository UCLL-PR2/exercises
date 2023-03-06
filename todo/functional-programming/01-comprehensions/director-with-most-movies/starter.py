def director_with_most_movies(movies):
    counts_by_director = {}
    for movie in movies:
        counts_by_director[movie.director] = counts_by_director.get(movie.director, 0) + 1
    directors = list(counts_by_director.keys())
    director_with_most = directors[0]
    for director in directors[1:]:
        if counts_by_director[director] > counts_by_director[director_with_most]:
            director_with_most = director
    return director_with_most
