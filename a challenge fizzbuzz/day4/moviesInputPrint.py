#Use an f-string to print the movie name and release year by 
# accessing your new movie tuple.

movie = [
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