import json

class QuerySelector:
    """A class to query and select data from a data table using various data structures."""

    def __init__(self, data_table):
        """
        Args:
            data_table (list of dict): A list of dictionaries representing the data table.
        """
        self.data_table = data_table
        self.converter = DatabaseConverter(data_table)
        self.data_structure = None

    def validate_choice(self, prompt, valid_options):
        """
        Validates the user's choice against the valid options.

        Args:
            prompt (str): The message to display when asking for input.
            valid_options (list): A list of valid input options.

        Returns:
            str: The user's valid choice.
        """
        while True:
            choice = input(prompt)
            if choice in valid_options:
                return choice
            print(f"Invalid input! Please select one of the following options: {', '.join(valid_options)}")

    def display_data_structure_menu(self):
        """Displays options for data structures to the user."""
        print("\n=== Choose Data Structure ===")
        print("1. Binary Search Tree")
        print("2. Skip List")
        print("3. Standard Array")

    def display_search_algorithm_menu(self):
        """Displays available search algorithms to the user."""
        print("\n=== Choose Search Algorithm ===")
        print("1. Linear Search")
        print("2. Binary Search")

    def display_sort_algorithm_menu(self):
        """Displays available sorting algorithms to the user."""
        print("\n=== Choose Sorting Algorithm ===")
        print("1. Quick Sort")
        print("2. Merge Sort")
        print("3. Bubble Sort")
        print("4. Selection Sort")
        print("5. Insertion Sort")

    def choose_data_structure(self):
        """Give user option of what data structure they want to use for this query."""
        self.display_data_structure_menu()
        choice = self.validate_choice("Select a data structure (1-3): ", ['1', '2', '3'])
        
        if choice == '1':
            self.data_table = self.converter.to_binary_search_tree("id")  # Default key
            self.data_structure = "BinarySearchTree"

        elif choice == '2':
            self.data_table = self.converter.to_skip_list("id")  # Default key
            self.data_structure = "SkipList"
        else:  # choice '3'
            self.data_table = self.converter.to_standard_array()  # Default key
            self.data_structure = "StandardArray"
        
        return self.data_table

    def choose_search_algorithm(self, key, search_key):
        """Give user option of what search algorithm they want to use for this query."""
        self.display_search_algorithm_menu()
        choice = self.validate_choice("Select a search algorithm (1-2): ", ['1', '2'])
        
        if choice == '1':  # Linear Search
            if isinstance(self.data_structure, "BinarySearchTree"):
                return self._search_bst_linear(search_key)
            elif isinstance(self.data_structure, "SkipList"):
                return self._search_skip_list_linear(search_key)
            else:  # Standard Array
                return next((item for item in self.data_structure if item[key] == search_key), None)
        else:  # Binary Search
            if isinstance(self.data_structure, "BinarySearchTree"):
                return self.data_structure.search(search_key)
            elif isinstance(self.data_structure, "SkipList"):
                return self._search_skip_list(search_key)
            else:  # Standard Array
                # Assuming the array is sorted for binary search
                return self._binary_search(self.data_structure, key, search_key)

    def choose_sort_algorithm(self, key):
        """Give user option of what sort algorithm they want to use for this query."""
        self.display_sort_algorithm_menu()
        choice = self.validate_choice("Select a sorting algorithm (1-4): ", ['1', '2', '3', '4'])
        
        if choice == '1':  # Quick Sort
            if isinstance(self.data_structure, "BinarySearchTree"):
                return in_order_traversal(self.data_structure)
            elif isinstance(self.data_structure, "SkipList"):
                return traverse_skip_list(self.data_structure)
            else:  # Standard Array
                return sorted(self.data_table, key=lambda item: item[key])
        elif choice == '2':  # Merge Sort
            return self._merge_sort_data_standard_array(self.data_table, key)
        elif choice == '3':  # Bubble Sort
            return self._bubble_sort_data(self.data_table, key)
        else:  # Selection Sort
            return self._selection_sort_data(self.data_table, key)

    def _search_bst_linear(self, search_key):
        """Perform a linear search on the binary search tree."""
        # Implementation for linear search in BST
        pass

    def _search_skip_list_linear(self, search_key):
        """Perform a linear search in the skip list."""
        # Implementation for linear search in Skip List
        pass

    def _binary_search(self, array, key, search_key):
        """Perform binary search on the standard array."""
        # Implementation for binary search
        pass

    def _merge_sort_data_standard_array(self, data, key):
        """Merge sort implementation for a standard array."""
        # Implementation for merge sort
        pass

    def _bubble_sort_data(self, data, key):
        """Bubble sort implementation for a standard array."""
        # Implementation for bubble sort
        pass

    def _selection_sort_data(self, data, key):
        """Selection sort implementation for a standard array."""
        # Implementation for selection sort
        pass


class SearchAlgorithms:
    def linear_search(list_of_movies, search_by, target_value):
        """
        Searches for a target value in a sorted list of dictionaries or simple values using linear search.

        Args:
            data (list): The sorted list to search through (can be dictionaries or simple values).
            target_value: The value to search for.
            search_by (str): The key to access in the dictionary if data is a list of dictionaries.

        Returns:
            int: The index of the target value if found; -1 otherwise.
        """
        for movie in list_of_movies:
            if isinstance(movie, dict):  # Check if the movie is a dictionary
                if search_by in movie and movie[search_by] == target_value:
                    return movie  # Return the movie dict if found
            elif isinstance(movie, list):  # Check if the movie is a list
                # Assuming the order is known: [title, genre, actor, release_date, value]
                keys = ["title", "genre", "actor", "release_date"]
                movie_dict = dict(zip(keys, movie))  # Create a dict from the list
                if search_by in movie_dict and movie_dict[search_by] == target_value:
                    return movie_dict  # Return the movie dict if found
        return -1  # Return None if no movie matches the criteria
    
    @staticmethod
    def binary_search(data, target_value, key=None):
        """
        Searches for a target value in a sorted list of dictionaries or simple values using binary search.

        Args:
            data (list): The sorted list to search through (can be dictionaries or simple values).
            target_value: The value to search for.
            key (str, optional): The key to access in the dictionary if data is a list of dictionaries.

        Returns:
            int: The index of the target value if found; -1 otherwise.
        """
        left_index, right_index = 0, len(data) - 1

        while left_index <= right_index:
            middle_index = (left_index + right_index) // 2
            
            if isinstance(data[middle_index], dict):  # Check for dict
                if key in data[middle_index]:
                    middle_value = data[middle_index][key].lower()
                else:
                    return -1  # Invalid structure for binary search
            elif isinstance(data[middle_index], list):  # Check for list
                keys = ["title", "genre", "actor", "release_date"]
                movie_dict = dict(zip(keys, data[middle_index]))  # Create dict from list
                middle_value = movie_dict[key].lower() if key in movie_dict else None
            else:
                middle_value = data[middle_index].lower() if isinstance(data[middle_index], str) else None

            if middle_value is None:
                return -1  # Handle cases where the value is not a string

            if middle_value == target_value.lower():
                return middle_index
            elif middle_value < target_value.lower():
                left_index = middle_index + 1
            else:
                right_index = middle_index - 1

        return -1  # Return -1 if not found


class SortAlgorithms:
    
    @staticmethod
    def partition(data, low_index, high_index, key):
        """
        Partitions the input data for quicksort.

        Args:
            data (list): The list to be partitioned (can be dictionaries or simple values).
            low_index (int): The starting index of the subarray.
            high_index (int): The ending index of the subarray.
            key (str): The key to sort by if data is a list of dictionaries.

        Returns:
            int: The index of the pivot element after partitioning.
        """
        pivot_value = None
        if isinstance(data[high_index], dict) and key in data[high_index]:
            pivot_value = data[high_index][key].lower()
        elif isinstance(data[high_index], list):
            keys = ["title", "genre", "actor", "release_date"]
            movie_dict = dict(zip(keys, data[high_index]))
            pivot_value = movie_dict[key].lower() if key in movie_dict else None

        i = low_index - 1

        for j in range(low_index, high_index):
            if isinstance(data[j], dict):
                compare_value = data[j][key].lower() if key in data[j] else None
            elif isinstance(data[j], list):
                movie_dict = dict(zip(keys, data[j]))
                compare_value = movie_dict[key].lower() if key in movie_dict else None
            else:
                compare_value = data[j].lower() if isinstance(data[j], str) else None
            
            if compare_value is not None and compare_value <= pivot_value:
                i += 1
                data[i], data[j] = data[j], data[i]

        data[i + 1], data[high_index] = data[high_index], data[i + 1]
        return i + 1

    @staticmethod
    def quick_sort(data, low_index, high_index, key=None):
        """
        Sorts the input data using the quicksort algorithm based on a specified key.

        Args:
            data (list): The list to be sorted (can be dictionaries or simple values).
            low_index (int): The starting index of the subarray.
            high_index (int): The ending index of the subarray.
            key (str, optional): The key to sort by if data is a list of dictionaries.
        """
        if low_index < high_index:
            pivot_index = SortAlgorithms.partition(data, low_index, high_index, key)
            SortAlgorithms.quick_sort(data, low_index, pivot_index - 1, key)
            SortAlgorithms.quick_sort(data, pivot_index + 1, high_index, key)

    @staticmethod
    def bubble_sort(data, key=None):
        """
        Sorts the input data using the bubble sort algorithm based on a specified key.

        Args:
            data (list): The list to be sorted (can be dictionaries or simple values).
            key (str, optional): The key to sort by if data is a list of dictionaries.
        """
        for n in range(len(data) - 1, 0, -1):
            for current_index in range(n):
                if isinstance(data[current_index], dict):  # Check for dictionary
                    if key in data[current_index] and key in data[current_index + 1]:
                        if data[current_index][key].lower() > data[current_index + 1][key].lower():
                            data[current_index], data[current_index + 1] = data[current_index + 1], data[current_index]
                elif isinstance(data[current_index], list):  # Check for list
                    keys = ["title", "genre", "actor", "release_date"]
                    dict_current = dict(zip(keys, data[current_index]))
                    dict_next = dict(zip(keys, data[current_index + 1]))
                    if key in dict_current and key in dict_next:
                        if dict_current[key].lower() > dict_next[key].lower():
                            data[current_index], data[current_index + 1] = data[current_index + 1], data[current_index]
                else:  # Handle simple values
                    if data[current_index] > data[current_index + 1]:
                        data[current_index], data[current_index + 1] = data[current_index + 1], data[current_index]

    @staticmethod
    def selection_sort(data, key=None):
        """
        Sorts the input data using the selection sort algorithm based on a specified key.

        Args:
            data (list): The list to be sorted (can be dictionaries or simple values).
            key (str, optional): The key to sort by if data is a list of dictionaries.
        """
        size = len(data)
        for current_index in range(size):
            min_index = current_index
            for next_index in range(current_index + 1, size):
                if isinstance(data[next_index], dict):  # Check for dictionary
                    if key in data[next_index] and key in data[min_index]:
                        if data[next_index][key].lower() < data[min_index][key].lower():
                            min_index = next_index
                elif isinstance(data[next_index], list):  # Check for list
                    keys = ["title", "genre", "actor", "release_date"]
                    dict_current = dict(zip(keys, data[min_index]))
                    dict_next = dict(zip(keys, data[next_index]))
                    if key in dict_current and key in dict_next:
                        if dict_next[key].lower() < dict_current[key].lower():
                            min_index = next_index
                else:  # Handle simple values
                    if data[next_index] < data[min_index]:
                        min_index = next_index
            data[current_index], data[min_index] = data[min_index], data[current_index]

    @staticmethod
    def merge(data, left_index, middle_index, right_index, key=None):
        """
        Merges two subarrays of data in sorted order based on a specified key.

        Args:
            data (list): The array containing the subarrays to merge (can be dictionaries or simple values).
            left_index (int): The starting index of the left subarray.
            middle_index (int): The ending index of the left subarray.
            right_index (int): The ending index of the right subarray.
            key (str, optional): The key to merge by if data is a list of dictionaries.
        """
        left_size = middle_index - left_index + 1
        right_size = right_index - middle_index

        left_half = [0] * left_size
        right_half = [0] * right_size

        for i in range(left_size):
            left_half[i] = data[left_index + i]

        for j in range(right_size):
            right_half[j] = data[middle_index + 1 + j]

        i, j, k = 0, 0, left_index

        while i < left_size and j < right_size:
            if isinstance(left_half[i], dict) and isinstance(right_half[j], dict):  # Check for dictionaries
                if key in left_half[i] and key in right_half[j]:
                    if left_half[i][key].lower() <= right_half[j][key].lower():
                        data[k] = left_half[i]
                        i += 1
                    else:
                        data[k] = right_half[j]
                        j += 1
            elif isinstance(left_half[i], list) and isinstance(right_half[j], list):  # Check for lists
                keys = ["title", "genre", "actor", "release_date"]
                dict_left = dict(zip(keys, left_half[i]))
                dict_right = dict(zip(keys, right_half[j]))
                if key in dict_left and key in dict_right:
                    if dict_left[key].lower() <= dict_right[key].lower():
                        data[k] = left_half[i]
                        i += 1
                    else:
                        data[k] = right_half[j]
                        j += 1
            else:  # Handle simple values
                if left_half[i] <= right_half[j]:
                    data[k] = left_half[i]
                    i += 1
                else:
                    data[k] = right_half[j]
                    j += 1
            k += 1

        while i < left_size:
            data[k] = left_half[i]
            i += 1
            k += 1

        while j < right_size:
            data[k] = right_half[j]
            j += 1
            k += 1

    @staticmethod
    def merge_sort(data, left_index, right_index, key=None):
        """
        Sorts the input data using the merge sort algorithm based on a specified key.

        Args:
            data (list): The list to be sorted (can be dictionaries or simple values).
            left_index (int): The starting index of the subarray.
            right_index (int): The ending index of the subarray.
            key (str, optional): The key to sort by if data is a list of dictionaries.
        """
        if left_index < right_index:
            middle_index = left_index + (right_index - left_index) // 2
            SortAlgorithms.merge_sort(data, left_index, middle_index, key)
            SortAlgorithms.merge_sort(data, middle_index + 1, right_index, key)
            SortAlgorithms.merge(data, left_index, middle_index, right_index, key)

    @staticmethod
    def insertion_sort(data, key=None):
        """
        Sorts the input data using the insertion sort algorithm based on a specified key.

        Args:
            data (list): The list to be sorted (can be dictionaries or simple values).
            key (str, optional): The key to sort by if data is a list of dictionaries.
        """
        size = len(data)
        if size <= 1:
            return  # Already sorted

        for current_index in range(1, size):
            key_value = data[current_index]
            index_to_compare = current_index - 1
            
            while index_to_compare >= 0:
                if isinstance(data[index_to_compare], dict):  # Check for dictionary
                    if key in key_value and key in data[index_to_compare]:
                        if key_value[key].lower() < data[index_to_compare][key].lower():
                            data[index_to_compare + 1] = data[index_to_compare]
                            index_to_compare -= 1
                        else:
                            break
                elif isinstance(data[index_to_compare], list):  # Check for list
                    keys = ["title", "genre", "actor", "release_date"]
                    dict_current = dict(zip(keys, data[index_to_compare]))
                    dict_key_value = dict(zip(keys, key_value))
                    if key in dict_key_value and key in dict_current:
                        if dict_key_value[key].lower() < dict_current[key].lower():
                            data[index_to_compare + 1] = data[index_to_compare]
                            index_to_compare -= 1
                        else:
                            break
                else:  # Handle simple values
                    if key_value < data[index_to_compare]:
                        data[index_to_compare + 1] = data[index_to_compare]
                        index_to_compare -= 1
                    else:
                        break
            
            data[index_to_compare + 1] = key_value

class DataTransformer:

    def to_list_of_dicts(data, keys=None):
        """
        Transforms the input data into a list of dictionaries.

        Args:
            data (list): The input data (can be a list of lists or already a list of dicts).
            keys (list, optional): The keys to use for the dictionaries if data is a list of lists.

        Returns:
            list: A list of dictionaries.
        """
        if isinstance(data, list) and all(isinstance(item, dict) for item in data):
            return data  # Already in the desired format

        if isinstance(data, list) and all(isinstance(item, list) for item in data):
            if keys is None:
                raise ValueError("Keys must be provided to convert lists to dictionaries.")
            return [dict(zip(keys, item)) for item in data]

        raise ValueError("Input data must be a list of lists or a list of dictionaries.")

    def to_list_of_lists(data, keys=None):
        """
        Transforms the input data into a list of lists.

        Args:
            data (list): The input data (can be a list of lists or already a list of dicts).
            keys (list, optional): The keys to use for the lists if data is a list of dictionaries.

        Returns:
            list: A list of lists.
        """
        if isinstance(data, list) and all(isinstance(item, list) for item in data):
            return data  # Already in the desired format

        if isinstance(data, list) and all(isinstance(item, dict) for item in data):
            if keys is None:
                raise ValueError("Keys must be provided to convert dictionaries to lists.")
            return [[item[key] for key in keys] for item in data]

        raise ValueError("Input data must be a list of lists or a list of dictionaries.")
    