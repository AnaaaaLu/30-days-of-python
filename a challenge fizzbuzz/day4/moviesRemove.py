# Remove the first movie from movies. Use any method you like.
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

movies.remove(movies[0])

print(f"{movies}")