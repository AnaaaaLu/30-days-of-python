# Below you'll find a list which contains the relevant data about a 
# selection of movies. Each item in the list is a tuple containing a 
# movie name and movie budget in that order:
#   movies = [
#       ("Eternal Sunshine of the Spotless Mind", 20000000),
#       ("Memento", 9000000),
#       ("Requiem for a Dream", 4500000),
#       ("Pirates of the Caribbean: On Stranger Tides", 379000000),
#       ("Avengers: Age of Ultron", 365000000),
#       ("Avengers: Endgame", 356000000),
#       ("Incredibles 2", 200000000)
#   ]
# 
# For this project, your program should do the following:
# Calculate the average budget of all movies in the data set.
# Print out every movie that has a budget higher than the average you 
# calculated. You should also print out how much higher than the average 
# the movie's budget was.
# Print out how many movies spent more than the average you calculated.
# If you want a little extra challenge, allow users to add more movies 
# to the data set before running the calculations.
# 
# You can do this by asking the user how many movies they want to add, 
# which will allow you to use a for loop and range to repeat some code a 
# given number of times. Inside the for loop, you can write some code 
# that takes in some user input and appends a movie tuple containing the 
# collected data to the movie list.

movies = [
    ("Eternal Sunshine of the Spotless Mind", 20000000),
    ("Memento", 9000000),
    ("Requiem for a Dream", 4500000),
    ("Pirates of the Caribbean: On Stranger Tides", 379000000),
    ("Avengers: Age of Ultron", 365000000),
    ("Avengers: Endgame", 356000000),
    ("Incredibles 2", 200000000)
]

highBudgetMovies = []
totalBudget = 0

for movie in movies:
    totalBudget = totalBudget + movie[1]

averageBudget = int(totalBudget /len(movies))

for movie in movies:
    if movie[1] > averageBudget:
        highBudgetMovies.append(movie)
        surplusCost =  movie[1] - averageBudget
        print(f"{movie[0]} cost ${movie[1]:,} -> ${surplusCost:,} over average.")

print(f"There were {len(highBudgetMovies)} movies over average budgets")