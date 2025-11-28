# Add the new movie tuple to the movies collection using append.
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

print(f"{new_movie[0]} ({new_movie[2]})")

movies.append(new_movie)