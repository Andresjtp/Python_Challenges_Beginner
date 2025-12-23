# 🎬 Movie Library with Ratings

## Challenge Overview

This challenge focuses on building a movie management system using Python's lists, dictionaries, and filtering techniques to organize and analyze movie collections based on genres and ratings.

**Core Skills Practiced:**
- Lists
- Dictionaries
- Filtering
- Data analysis
- List comprehensions

---

## Structure

### Class: `Movie`
Represents an individual movie with three attributes:
- `title` - Movie title
- `genre` - Movie genre (Action, Drama, Sci-Fi, etc.)
- `rating` - Movie rating (typically 0-10 scale)

### Class: `MovieLibrary`
Manages a collection of movies using a list:
- `movies` - List containing all `Movie` objects

---

## Features Implementation

### 1. **Add Movie**
```python
def add_movie(self, movie):
    self.movies.append(movie)
```
**How it works:**
- Accepts a `Movie` object as a parameter
- Appends the entire movie object to the library's list
- Simple and efficient storage of complete movie information

**Example:**
```python
library = MovieLibrary()
movie1 = Movie("Inception", "Sci-Fi", 8.8)
library.add_movie(movie1)
```

---

### 2. **Filter by Genre**
```python
def genre_filter(self, genre):
    filtered = [movie for movie in self.movies if movie.genre.lower() == genre.lower()]
    if not filtered:
        print(f"No movies found in genre: {genre}")
        return

    print(f"\n--- {genre} Movies ---")
    for movie in filtered:
        print(f"{movie.title} - Rating: {movie.rating}/10")
    print("--------------------\n")
```
**How it works:**
- Uses **list comprehension** to create a filtered list of movies
- Performs **case-insensitive comparison** using `.lower()` for flexibility
- Checks if the filtered list is empty and provides feedback
- Iterates through filtered results and displays each movie with its rating

**Key concepts:**
- **List comprehension**: `[movie for movie in self.movies if condition]`
- **Filtering logic**: Only includes movies matching the specified genre
- **User feedback**: Informs when no matches are found

**Example:**
```python
library.genre_filter("Sci-Fi")
# Output:
# --- Sci-Fi Movies ---
# Inception - Rating: 8.8/10
# Interstellar - Rating: 8.6/10
# --------------------
```

---

### 3. **Show Top-Rated Movies**
```python
def top_rated(self, threshold=8.0):
    top_movies = [movie for movie in self.movies if movie.rating >= threshold]
    if not top_movies:
        print(f"No movies with rating >= {threshold}")
        return

    top_movies.sort(key=lambda movie: movie.rating, reverse=True)

    print(f"\n--- Top-Rated Movies (>= {threshold}) ---")
    for movie in top_movies:
        print(f"{movie.title} - Rating: {movie.rating}/10")
    print("--------------------\n")
```
**How it works:**
- Uses **list comprehension** to filter movies above the rating threshold
- Default threshold is 8.0, but can be customized
- **Sorts** the filtered list by rating in descending order (highest first)
- Uses a **lambda function** as the sorting key
- Displays all qualifying movies in order from highest to lowest rating

**Key concepts:**
- **Filtering with threshold**: `if movie.rating >= threshold`
- **Lambda function**: Anonymous function for sorting: `key=lambda movie: movie.rating`
- **Reverse sorting**: `reverse=True` shows highest ratings first
- **Default parameter**: `threshold=8.0` provides flexibility

**Example:**
```python
library.top_rated(9.0)
# Output:
# --- Top-Rated Movies (>= 9.0) ---
# The Shawshank Redemption - Rating: 9.3/10
# The Godfather - Rating: 9.2/10
# The Dark Knight - Rating: 9.0/10
# --------------------
```

---

### 4. **Calculate Average Rating**
```python
def average_rating(self):
    if not self.movies:
        print("No movies in library")
        return 0

    total = sum(movie.rating for movie in self.movies)
    average = total / len(self.movies)
    print(f"Average rating: {average:.2f}/10")
    return average
```
**How it works:**
- Validates that the library isn't empty to avoid division by zero
- Uses **generator expression** with `sum()` to calculate total ratings
- Divides total by the number of movies to get average
- Formats output to 2 decimal places using `.2f`
- Returns the average for potential further use

**Key concepts:**
- **Generator expression**: `sum(movie.rating for movie in self.movies)` - memory efficient
- **Edge case handling**: Checks for empty library
- **String formatting**: `{average:.2f}` for clean decimal display
- **Dual purpose**: Prints result AND returns value

**Formula:** `Average = Σ(all ratings) / number of movies`

**Example:**
```python
avg = library.average_rating()
# Output: Average rating: 8.76/10
# Returns: 8.76
```

---

## Key Concepts Demonstrated

### 1. **List Comprehensions**
```python
filtered = [movie for movie in self.movies if movie.genre.lower() == genre.lower()]
```
- Concise way to filter and transform lists
- More Pythonic than traditional for loops
- Combines iteration and conditional logic in one line

### 2. **Lambda Functions**
```python
top_movies.sort(key=lambda movie: movie.rating, reverse=True)
```
- Anonymous functions for simple operations
- Commonly used for sorting by specific attributes
- Cleaner alternative to defining separate functions

### 3. **Generator Expressions**
```python
total = sum(movie.rating for movie in self.movies)
```
- Memory-efficient iteration
- Similar to list comprehension but doesn't create intermediate list
- Ideal for aggregation operations like `sum()`

### 4. **Object-Oriented Design**
- **Encapsulation**: Movie data bundled in Movie class
- **Separation of concerns**: Movie stores data, MovieLibrary manages operations
- **List of objects**: Movies stored as complete objects preserving all attributes

### 5. **Defensive Programming**
- Checks for empty lists before operations
- Provides user feedback when filters return no results
- Prevents runtime errors (like division by zero)

---

## Usage Example

```python
# Create library
library = MovieLibrary()

# Create and add movies
library.add_movie(Movie("The Shawshank Redemption", "Drama", 9.3))
library.add_movie(Movie("The Dark Knight", "Action", 9.0))
library.add_movie(Movie("Inception", "Sci-Fi", 8.8))
library.add_movie(Movie("The Godfather", "Drama", 9.2))
library.add_movie(Movie("Interstellar", "Sci-Fi", 8.6))
library.add_movie(Movie("The Matrix", "Sci-Fi", 8.7))
library.add_movie(Movie("Pulp Fiction", "Crime", 8.9))

# Filter by genre
library.genre_filter("Sci-Fi")
# Shows: Inception, Interstellar, The Matrix

# Show top-rated movies (default threshold 8.0)
library.top_rated()
# Shows all movies sorted by rating

# Show only exceptional movies
library.top_rated(9.0)
# Shows: The Shawshank Redemption, The Godfather, The Dark Knight

# Calculate average rating
avg = library.average_rating()
# Output: Average rating: 8.93/10
```

---

## Data Flow Visualization

```
Movie Object Creation:
Movie("Inception", "Sci-Fi", 8.8)
    ↓
Add to Library:
library.movies = [movie1, movie2, movie3, ...]
    ↓
Filter by Genre:
[movie for movie in movies if genre matches]
    ↓
Display Results:
Print formatted movie information
```

---

## Potential Enhancements

- Add movie removal functionality
- Search by title (partial matching)
- Filter by rating range (e.g., 7.0-8.5)
- Sort by multiple criteria (genre + rating)
- Add release year attribute
- Track watched/unwatched status
- Add movie reviews or descriptions
- Export library to file (JSON/CSV)
- Import movies from external data source
- Add duplicate detection
- Create genre statistics (count per genre)
- Find lowest-rated movies
- Add actors/directors attributes
- Implement a simple recommendation system
