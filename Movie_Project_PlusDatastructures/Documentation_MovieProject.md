# Movie Search Program Documentation

## 1. Pseudocode

### a. Definition of the Problem
The problem is to develop a Movie Search Program that allows users to search for movies based on various attributes (title, genre, actor, release date) and sort them using different algorithms. Additionally, it includes a Manager Mode for adding or removing movies.

### b. Inputs
- User commands for searching, sorting, and managing movies.
- Movie data from a JSON file (`movies.json`).
- Password for accessing Manager Mode.

### c. Outputs
- Search results based on user queries.
- Sorted lists of movies based on user-selected criteria.
- Confirmation messages for adding or removing movies.
- Execution time for search and sort operations.

### d. Pseudocode

```plaintext
FUNCTION validate_choice(prompt, valid_options):
    WHILE:
        INPUT prompt
            IF choice in valid_options
                CONTINUE
            ELSE
                PRINT Invalid input try again

FUNCTION load_movies(file_path):
    TRY:
        OPEN file at file_path
        RETURN JSON data as list
    EXCEPT FileNotFoundError:
        PRINT "Error: The file was not found."
        RETURN empty list
    EXCEPT JSONDecodeError:
        PRINT "Error: Failed to decode JSON."
        RETURN empty list

FUNCTION save_movies(file_path, movies):
    OPEN file at file_path in write mode
    DUMP movies to JSON file with indentation

FUNCTION display_menu():
    PRINT main menu options

FUNCTION display_search_menu():
    PRINT search options

FUNCTION display_sort_menu():
    PRINT sorting options

FUNCTION display_search_algorithm_menu():
    PRINT available search algorithms

FUNCTION display_datastructures_menu():
    PRINT available datastructures

FUNCTION display_sort_algorithm_menu():
    PRINT available sorting algorithms

FUNCTION search_movies(movies):
    DISPLAY search menu
    GET user choice
    DISPLAY search algorithm menu
    GET algorithm choice
    IF choice == 1:
        GET title from user
        IF algorithm == 1:
            TIME linear_search
            PRINT search time
        ELSE IF algorithm == 2:
            SORT movies
            TIME binary_search
            PRINT search time
    ELSE IF choice == 2:
        GET genre from user
        FIND movies matching genre
        PRINT results
    ELSE IF choice == 3:
        GET actor from user
        FIND movies matching actor
        PRINT results
    ELSE IF choice == 4:
        GET release_date from user
        TIME search operation
        PRINT results

FUNCTION sort_movies(movies):
    DISPLAY sort menu
    GET user choice
    DISPLAY sort algorithm menu
    GET algorithm choice
    TIME the selected sorting algorithm
    PRINT sorted movies

FUNCTION manager_mode(movies):
    GET password from user
    IF password is correct:
        DISPLAY manager options
        GET choice
        IF choice == 1:
            GET movie details from user
            ADD movie to list
            SAVE movie list
        ELSE IF choice == 2:
            GET title to remove from user
            REMOVE movie from list
            SAVE movie list
        ELSE IF choice == 3:
            EXIT manager mode

FUNCTION main():
    LOAD movies from JSON
    WHILE True:
        DISPLAY main menu
        GET user choice
        CALL respective function based on choice
```

## 2. UML
    +--------------------------------+
    |        MovieSearchProgram      |
    +--------------------------------+
    | - movies: List[Movie]         |
    +--------------------------------+
    | + validate_choice(prompt, valid_options)|
    | + load_movies(file_path)       |
    | + save_movies(file_path, movies)|
    | + display_menu()               |
    | + display_search_menu()        |
    | + display_sort_menu()          |
    | + display_search_algorithm_menu()|
    | + display_sort_algorithm_menu() |
    | + search_movies(movies)        |
    | + sort_movies(movies)          |
    | + manager_mode(movies)         |
    | + main()                       |
    +--------------------------------+
                    ^ -----------------------------------
                    |                                    |
    +-----------------------------------------------+    |
    |  Utility:SearchAlgorithms                     |    |
    +-----------------------------------------------+    |
    | - List                                        |    |
    | - Key                                         |    |
    | - Target                                      |    |
    +-----------------------------------------------+    |
    | + linear_search(data, target_value, key=None) |    |
    | + binary_search(data, target_value, key=None) |    |
    +-----------------------------------------------+    |
                                                         |
    +-----------------------------------------------+ ---|
    |  Utility:DataTransformer                      |    |
    +-----------------------------------------------+    |
    | - List                                        |    |
    | - Key                                         |    |
    +-----------------------------------------------+    |
    | + to_list_of_dicts(data, keys=None)           |    |
    | + to_list_of_lists(data, keys=None)           |    |
    +-----------------------------------------------+    |
                                                         |
    +-----------------------------------------------------+
    |  Utility:SortAlgorithms                             |
    +-----------------------------------------------------+
    | - List                                              |
    | - Key                                               |
    +-----------------------------------------------------+
    | + quick_sort(data, low_index, high_index, key=None) |
    | + partition(data, low_index, high_index, key=None)  |
    | + bubble_sort(data, key=None)                       |
    | + selection_sort(data, key=None)                    |
    | + merge_sort(data, left_index, right_index, key=None) |
    | + merge(data, left_index, middle_index, right_index, key=None)  |
    | + insertion_sort(data, key=None)                    |
    +-----------------------------------------------------+

## 3. Flowchart
    +---------------------------+
    |   Start Program           |
    +---------------------------+
                |
                v
    +---------------------------+
    | Load Movies from JSON     |
    +---------------------------+
                |
                v
    +---------------------------+
    | Display Main Menu         |
    +---------------------------+
                |
                v
    +---------------------------+
    | User Selects Option       |
    +---------------------------+
                |
    +-----------+-------------+--------------+
    |           |             |              |
    v           v             v              v
    +-------+ +-----------+ +-----------+ +-----------+
    | Search| | Sort      | | Manager   | | Exit      |
    |       | |           | | Mode      | |           |
    +-------+ +-----------+ +-----------+ +-----------+
        |           |             |
        v           v             v
    +-------+ +-----------+ +-----------+
    | Search| | Sort      | | Password   |
    | Logic | | Logic     | | Check      |
    +-------+ +-----------+ +-----------+
        |           |             |
        v           v             v
    +---------------------------+
    | Display Results           |
    +---------------------------+
                |
                v
    +---------------------------+
    |    End Program            |
    +---------------------------+
