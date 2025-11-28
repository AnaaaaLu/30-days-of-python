# Create a new tuple from the values you gathered using input. 
# Make sure they’re in the same order as the tuple you wrote in the
# movies list.

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