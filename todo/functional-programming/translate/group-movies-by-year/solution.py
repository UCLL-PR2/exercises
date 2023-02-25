def group_movies_by_year(movies):
    years = {movie.year for movie in movies}
    return {
        year: [movie.title for movie in movies if movie.year == year]
        for year in years
    }
