# Movie Search Program Documentation

## `MovieSearchProgram` Class

**Purpose:**  
The `MovieSearchProgram` class provides functionalities for searching, sorting, and managing movies. It allows users to perform operations based on movie attributes and includes a Manager Mode for administrative tasks.

### Methods:

### `validate_choice(prompt, valid_options)`

- **Purpose:**  
  Compare and validate input to intended input
  
- **Input:**  
  - `prompt` (str): The prompt for the input statement.
  - `valid_options` (list): List of valid inputs for the prompt.
  
- **Output:**  
  - Validates the input for the menu so that the user doesn't give an invalid input.

### `load_movies(file_path)`
- **Purpose:**  
  Loads movies from a specified JSON file.
  
- **Input:**  
  - `file_path` (str): The path to the JSON file containing movie data.
  
- **Output:**  
  - Returns a list of movies if successful, otherwise an empty list.

### `save_movies(file_path, movies)`
- **Purpose:**  
  Saves the list of movies to a specified JSON file.
  
- **Input:**  
  - `file_path` (str): The path to the JSON file to save the movie data.
  - `movies` (list): The list of movies to save.

### `display_menu()`
- **Purpose:**  
  Displays the main menu options to the user.

### `display_search_menu()`
- **Purpose:**  
  Displays search options to the user.

### `display_sort_menu()`
- **Purpose:**  
  Displays sorting options to the user.

### `display_search_algorithm_menu()`
- **Purpose:**  
  Displays available search algorithms to the user.

### `display_datastructures_menu()`
- **Purpose:**  
  Displays available datastructures to the user.

### `display_sort_algorithm_menu()`
- **Purpose:**  
  Displays available sorting algorithms to the user.

### `search_movies(movies)`
- **Purpose:**  
  Allows the user to search for movies by title, genre, actor, or release date.
  
- **Input:**  
  - `movies` (list): The list of movies to search through.

### `sort_movies(movies)`
- **Purpose:**  
  Allows the user to sort movies by title, genre, actor, or release date.
  
- **Input:**  
  - `movies` (list): The list of movies to sort.

### `manager_mode(movies)`
- **Purpose:**  
  Provides functionalities for adding and removing movies in Manager Mode.
  
- **Input:**  
  - `movies` (list): The list of movies to manage.

### `main()`
- **Purpose:**  
  Executes the Movie Search Program.
  
- **Behavior:**  
  Loads movies, displays the menu, and processes user commands.

---

## `SearchAlgorithms` Class

**Purpose:**  
The `SearchAlgorithms` class provides static methods for searching through a list of movies.

### Methods:

### `linear_search(data, target, key)`
- **Purpose:**  
  Performs a linear search to find a target in the data.
  
- **Input:**  
  - `data` (list): The list to search through.
  - `target`: The value to search for.
  - `key` (str): The attribute to search by.
  
- **Output:**  
  - Returns the index of the target if found, otherwise returns -1.

### `binary_search(data, target, key)`
- **Purpose:**  
  Performs a binary search on sorted data to find a target.
  
- **Input:**  
  - `data` (list): The sorted list to search through.
  - `target`: The value to search for.
  - `key` (str): The attribute to search by.
  
- **Output:**  
  - Returns the index of the target if found, otherwise returns -1.

---

## `SortAlgorithms` Class

**Purpose:**  
The `SortAlgorithms` class provides static methods for sorting a list of movies.

### Methods:

### `quick_sort(data, low, high, key)`
- **Purpose:**  
  Sorts the data using the quick sort algorithm.
  
- **Input:**  
  - `data` (list): The list to sort.
  - `low` (int): The starting index.
  - `high` (int): The ending index.
  - `key` (str): The attribute to sort by.

### `bubble_sort(data, key)`
- **Purpose:**  
  Sorts the data using the bubble sort algorithm.
  
- **Input:**  
  - `data` (list): The list to sort.
  - `key` (str): The attribute to sort by.

### `selection_sort(data, key)`
- **Purpose:**  
  Sorts the data using the selection sort algorithm.
  
- **Input:**  
  - `data` (list): The list to sort.
  - `key` (str): The attribute to sort by.

### `merge_sort(data, left, right, key)`
- **Purpose:**  
  Sorts the data using the merge sort algorithm.
  
- **Input:**  
  - `data` (list): The list to sort.
  - `left` (int): The starting index.
  - `right` (int): The ending index.
  - `key` (str): The attribute to sort by.

### `insertion_sort(data, key)`
- **Purpose:**  
  Sorts the data using the insertion sort algorithm.
  
- **Input:**  
  - `data` (list): The list to sort.
  - `key` (str): The attribute to sort by.

## `DataTransformer` Class

**Purpose:**  
The `DataTransformer` class provides static methods for transforming data between lists and dictionaries.

### Methods:

### `to_list_of_dicts(data, keys=None)`
- **Purpose:**  
  Transforms the input data into a list of dictionaries.
  
- **Input:**  
  - `data` (list): The input data (can be a list of lists or already a list of dicts).
  - `keys` (list, optional): The keys to use for the dictionaries if data is a list of lists.
  
- **Output:**  
  - Returns a list of dictionaries.

### `to_list_of_lists(data, keys=None)`
- **Purpose:**  
  Transforms the input data into a list of lists.
  
- **Input:**  
  - `data` (list): The input data (can be a list of lists or already a list of dicts).
  - `keys` (list, optional): The keys to use for the lists if data is a list of dictionaries.
  
- **Output:**  
  - Returns a list of lists.


---

## `movies.json`

```json
[
    {
        "title": "The Dark Knight Rises",
        "genre": "Action, Adventure",
        "actor": "Christian Bale",
        "release_date": "2012-07-20"
    },
    ...
    // Additional movie data
]
