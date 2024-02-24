# Extension
h, w = 2, 5
movies_and_directors = [[0 for x in range(h)] for y in range(w)]

for movies in range(5):
    movie_choices = input("Please enter a movie: ")
    directors_of_movies = input("Please enter the director of this movie: ")
    movies_and_directors[movies][0] = movie_choices
    movies_and_directors[movies][1] = directors_of_movies

print("Movie name, Director name: ", movies_and_directors)

movie_choice = int(input("""\nEnter the number of the movie that you want to see
the details of (0 through 4 from left to right in the list): """))
print("Movie name:", movies_and_directors[movie_choice][0])
print("Director name:", movies_and_directors[movie_choice][1])

# Search for movie
watch_movie = input("""\nPlease enter the name of the movie that you
want to watch, to see if it is present in the list (from the list): """)

indicator1 = 0
for x in range(5):
    if watch_movie == movies_and_directors[x][0]:
        indicator1 = 1
        
if indicator1 == 1:
    print("This movie is present in the movie list.")
else:
    print("This movie is not present in the movie list.")

# Print director name
watch_movie = input("""\nPlease enter the name of the movie that you
want to find the director of (from the list): """)

indicator2 = 0
movie_index = -1
for y in range(5):
    if watch_movie == movies_and_directors[y][0]:
        indicator2 = 1
        movie_index = y
        
if indicator2 == 1:
    print("The director of this film is", movies_and_directors[movie_index][1], ".")
else:
    print("""Sorry, we can't find the director of this movie is
because it is not in the list.""")
