import json
import timeit  # Importing timeit to measure execution time
from Utility import SearchAlgorithms, SortAlgorithms

# Define a simple password for Manager Mode
MANAGER_PASSWORD = "admin123"  # This can be modified to change the Manager password

def load_movies(file_path):
    """
    Loads movies from a specified JSON file.

    Args:
        file_path (str): The path to the JSON file containing movie data.

    Returns:
        list: A list of movies if successful, otherwise an empty list.
    """
    try:
        with open(file_path, 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        print("Error: The file was not found.")
        return []
    except json.JSONDecodeError:
        print("Error: Failed to decode JSON.")
        return []

def save_movies(file_path, movies):
    """
    Saves the list of movies to a specified JSON file.

    Args:
        file_path (str): The path to the JSON file to save the movie data.
        movies (list): The list of movies to save.
    """
    with open(file_path, 'w') as file:
        json.dump(movies, file, indent=4)

def display_menu():
    """Displays the main menu options to the user."""
    print("\n=== Movie Search Program ===")
    print("1. Search for a movie")
    print("2. Sort movies")
    print("3. Manager Mode")
    print("4. Exit")

def display_search_menu():
    """Displays search options to the user."""
    print("\n=== Search Movies By ===")
    print("1. Title")
    print("2. Genre")
    print("3. Actor")
    print("4. Release Date")

def display_sort_menu():
    """Displays sorting options to the user."""
    print("\n=== Sort Movies By ===")
    print("1. Title")
    print("2. Genre")
    print("3. Actor")
    print("4. Release Date")

def display_search_algorithm_menu():
    """Displays available search algorithms to the user."""
    print("\n=== Choose Search Algorithm ===")
    print("1. Linear Search")
    print("2. Binary Search (requires sorted list)")

def display_sort_algorithm_menu():
    """Displays available sorting algorithms to the user."""
    print("\n=== Choose Sort Algorithm ===")
    print("1. Quick Sort")
    print("2. Bubble Sort")
    print("3. Selection Sort")
    print("4. Merge Sort")
    print("5. Insertion Sort")

def search_movies(movies):
    """
    Allows the user to search for movies by title, genre, actor, or release date.

    Args:
        movies (list): The list of movies to search through.
    """
    display_search_menu()
    choice = input("Select a search option (1-4): ")

    display_search_algorithm_menu()
    algo_choice = input("Select a search algorithm (1-2): ")

    if choice == '1':
        title = input("Enter the movie title to search for: ")
        if algo_choice == '1':
            # Measure the time taken for linear search
            time_taken = timeit.timeit(lambda: SearchAlgorithms.linear_search(movies, title, key='title'), number=1)
            index = SearchAlgorithms.linear_search(movies, title, key='title')
            print(f"Search completed in {time_taken:.6f} seconds.")
            if index != -1:
                print(f"Movie found: {movies[index]}")
            else:
                print("Movie not found.")
        elif algo_choice == '2':
            # Sort movies before binary search for title
            SortAlgorithms.quick_sort(movies, 0, len(movies) - 1, key='title')
            time_taken = timeit.timeit(lambda: SearchAlgorithms.binary_search(movies, title, key='title'), number=1)
            index = SearchAlgorithms.binary_search(movies, title, key='title')
            print(f"Search completed in {time_taken:.6f} seconds.")
            if index != -1:
                print(f"Movie found: {movies[index]}")
            else:
                print("Movie not found.")
    elif choice == '2':
        genre = input("Enter the genre to search for: ")
        results = [movie for movie in movies if genre.lower() in [g.lower() for g in movie['genre'].split(', ')]]
        if results:
            print("\nMovies found in genre:")
            for movie in results:
                print(f"{movie['title']} - {movie['genre']} - {movie['actor']} - {movie['release_date']}")
        else:
            print("No matches found.")
    elif choice == '3':
        actor = input("Enter the actor to search for: ")
        if algo_choice == '1':
            time_taken = timeit.timeit(lambda: [movie for movie in movies if actor.lower() in movie['actor'].lower()], number=1)
            results = [movie for movie in movies if actor.lower() in movie['actor'].lower()]
            print(f"Search completed in {time_taken:.6f} seconds.")
            if results:
                print("\nMovies found by actor:")
                for movie in results:
                    print(f"{movie['title']} - {movie['genre']} - {movie['actor']} - {movie['release_date']}")
            else:
                print("No matches found.")
        elif algo_choice == '2':
            # Sort movies before binary search for actor
            SortAlgorithms.quick_sort(movies, 0, len(movies) - 1, key='actor')
            time_taken = timeit.timeit(lambda: SearchAlgorithms.binary_search(movies, actor, key='actor'), number=1)
            index = SearchAlgorithms.binary_search(movies, actor, key='actor')
            print(f"Search completed in {time_taken:.6f} seconds.")
            if index != -1:
                print(f"Movie found: {movies[index]}")
            else:
                print("Movie not found.")
    elif choice == '4':
        release_date = input("Enter the release date (YYYY-MM-DD) to search for: ")
        if algo_choice == '1':
            time_taken = timeit.timeit(lambda: SearchAlgorithms.linear_search(movies, release_date, key='release_date'), number=1)
            index = SearchAlgorithms.linear_search(movies, release_date, key='release_date')
            print(f"Search completed in {time_taken:.6f} seconds.")
            if index != -1:
                print(f"Movie found: {movies[index]}")
            else:
                print("Movie not found.")
        elif algo_choice == '2':
            # Sort movies before binary search for release date
            SortAlgorithms.quick_sort(movies, 0, len(movies) - 1, key='release_date')
            time_taken = timeit.timeit(lambda: SearchAlgorithms.binary_search(movies, release_date, key='release_date'), number=1)
            index = SearchAlgorithms.binary_search(movies, release_date, key='release_date')
            print(f"Search completed in {time_taken:.6f} seconds.")
            if index != -1:
                print(f"Movie found: {movies[index]}")
            else:
                print("Movie not found.")
    else:
        print("Invalid choice! Returning to the main menu.")
        return

def sort_movies(movies):
    """
    Allows the user to sort movies by title, genre, actor, or release date.

    Args:
        movies (list): The list of movies to sort.
    """
    display_sort_menu()
    choice = input("Select a sorting option (1-4): ")

    display_sort_algorithm_menu()
    algo_choice = input("Select a sorting algorithm (1-5): ")

    if algo_choice == '1':
        # Measure the time taken for quick sort
        time_taken = timeit.timeit(lambda: SortAlgorithms.quick_sort(movies, 0, len(movies) - 1, key='title'), number=1)
    elif algo_choice == '2':
        time_taken = timeit.timeit(lambda: SortAlgorithms.bubble_sort(movies, key='genre'), number=1)
    elif algo_choice == '3':
        time_taken = timeit.timeit(lambda: SortAlgorithms.selection_sort(movies, key='actor'), number=1)
    elif algo_choice == '4':
        time_taken = timeit.timeit(lambda: SortAlgorithms.merge_sort(movies, 0, len(movies) - 1, key='release_date'), number=1)
    elif algo_choice == '5':
        time_taken = timeit.timeit(lambda: SortAlgorithms.insertion_sort(movies, key='title'), number=1)
    else:
        print("Invalid choice! Returning to the main menu.")
        return

    print(f"Sorting completed in {time_taken:.6f} seconds.")

    # Display sorted movies
    print(f"\nMovies sorted:")
    for movie in movies:
        print(f"{movie['title']} - {movie['genre']} - {movie['actor']} - {movie['release_date']}")

def manager_mode(movies):
    """
    Provides manager functionalities for adding and removing movies.

    Args:
        movies (list): The list of movies to manage.
    """
    password = input("Enter password for Manager Mode: ")
    if password != MANAGER_PASSWORD:
        print("Incorrect password! Returning to User Mode.")
        return

    while True:
        print("\n=== Manager Mode ===")
        print("1. Add a Movie")
        print("2. Remove a Movie")
        print("3. Exit Manager Mode")
        choice = input("Select an option (1-3): ")

        if choice == '1':
            title = input("Enter movie title: ")
            genre = input("Enter movie genre (comma-separated if multiple): ")
            actor = input("Enter actor(s): ")
            release_date = input("Enter release date (YYYY-MM-DD): ")
            new_movie = {
                "title": title,
                "genre": genre,
                "actor": actor,
                "release_date": release_date
            }
            movies.append(new_movie)
            save_movies('movies.json', movies)
            print("Movie added successfully.")

        elif choice == '2':
            title = input("Enter the title of the movie to remove: ")
            index = SearchAlgorithms.linear_search(movies, title, key='title')
            if index != -1:
                removed_movie = movies.pop(index)
                save_movies('movies.json', movies)
                print(f"Removed movie: {removed_movie['title']}")
            else:
                print("Movie not found.")

        elif choice == '3':
            print("Exiting Manager Mode.")
            break

        else:
            print("Invalid option. Please try again.")

def main():
    """
    Main function to execute the Movie Search Program.
    """
    movies = load_movies('movies.json')
    if not movies:
        return  # Exit if movies could not be loaded

    while True:
        display_menu()
        choice = input("Select an option (1-4): ")

        if choice == '1':
            search_movies(movies)
        elif choice == '2':
            sort_movies(movies)
        elif choice == '3':
            manager_mode(movies)
        elif choice == '4':
            print("Exiting the program. Goodbye!")
            break
        else:
            print("Invalid option. Please try again.")

if __name__ == "__main__":
    main()