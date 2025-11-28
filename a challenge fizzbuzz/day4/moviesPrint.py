# Print both movies in the movies collection.
movies = [
    (
        "Star Trek: The Motion Picture", 
        "Robert Wise", 
        1979, 
        "$44 mi"
    )
    ]

title = input("Title: ")
director = input("Director's name: ")
releaseYear = input("Release year of the movie: ")
budget = input ("Budget of the movie: ")

new_movie = title, director, releaseYear, budget

movies.append(new_movie)

print(f"{movies[0]} \n {movies[1]}")