def main():
    films = [None] * 6
    choice = int(input("Enter your menu choice number (1 through 5): "))
    while(choice != 5):
        if choice == 1:
            films = [None] * 6
        elif choice == 2:
            print(films)
        elif choice == 3:
            movie_choice_number = int(input("Enter the number of the movie you want to see: "))
            print(films[movie_choice_number])
        elif choice == 4:
            change_movie = int(input("Enter the number of the movie you want to change:(0 through 5): "))
            replace_movie = input("Enter the name of the movie that you want to replace it with: ")
            films[change_movie] = replace_movie
        choice = int(input("Enter another menu choice number (1 through 5): "))
main()
