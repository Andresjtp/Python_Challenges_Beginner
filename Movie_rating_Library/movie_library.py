class Movie:
    def __init__(self, title, genre, rating):
        self.title = title
        self.genre = genre
        self.rating = rating


class MovieLibrary:
    def __init__(self):
        self.movies = []

    def add_movie(self, movie):
        self.movies.append(movie)

    def genre_filter(self, genre):
        filtered = [movie for movie in self.movies if movie.genre.lower() == genre.lower()]
        # filtered = []
        # for movie in self.movies:
        #     if movie.genre.lower() == genre.lower():
        #         filtered.append(movie)

        if not filtered:
            print(f"No movies found in genre: {genre}")
            return

        print(f"\n--- {genre} Movies ---")
        for movie in filtered:
            print(f"{movie.title} - Rating: {movie.rating}/10")
        print("--------------------\n")


def top_rated(self, threshold=8.0):
    top_movies = [movie for movie in self.movies if movie.rating >= threshold]
    # top_movies = []
    # for movie in self.movies:
    #     if movie.rating >= threshold:
    #         top_movies.append(movie)

    if not top_movies:
        print(f"No movies with rating >= {threshold}")
        return

    top_movies.sort(key=lambda movie: movie.rating, reverse=True)

    print(f"\n--- Top-Rated Movies (>= {threshold}) ---")
    for movie in top_movies:
        print(f"{movie.title} - Rating: {movie.rating}/10")
    print("--------------------\n")


def average_rating(self):
    if not self.movies:
        print("No movies in library")
        return 0

    total = sum(movie.rating for movie in self.movies)
    average = total / len(self.movies)
    print(f"Average rating: {average:.2f}/10")
    return average
