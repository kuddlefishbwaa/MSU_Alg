class SearchAlgorithms:
    
    @staticmethod
    def linear_search(data, target_value, key=None):
        """
        Searches for a target value in a list of dictionaries or simple values using linear search.

        Args:
            data (list): The list to search through (can be dictionaries or simple values).
            target_value: The value to search for.
            key (str, optional): The key to access in the dictionary if data is a list of dictionaries.

        Returns:
            int: The index of the target value if found; -1 otherwise.
        """
        for index, item in enumerate(data):
            if key:
                if item[key].lower() == target_value.lower():  # Case-insensitive comparison
                    return index
            else:
                if item.lower() == target_value.lower():
                    return index
        return -1  # Return -1 if not found

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
            if key:
                middle_value = data[middle_index][key].lower()
            else:
                middle_value = data[middle_index].lower()
            
            if middle_value == target_value.lower():
                return middle_index
            elif middle_value < target_value.lower():
                left_index = middle_index + 1
            else:
                right_index = middle_index - 1
        return -1  # Return -1 if not found


class SortAlgorithms:
    
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
    def partition(data, low_index, high_index, key=None):
        """
        Partitions the input data around a pivot element based on a specified key.

        Args:
            data (list): The list to be partitioned (can be dictionaries or simple values).
            low_index (int): The starting index of the partition.
            high_index (int): The ending index of the partition.
            key (str, optional): The key to partition by if data is a list of dictionaries.

        Returns:
            int: The index of the pivot after partitioning.
        """
        if key:
            pivot_value = data[high_index][key]
        else:
            pivot_value = data[high_index]

        smaller_element_index = low_index - 1

        for current_index in range(low_index, high_index):
            if key:
                current_value = data[current_index][key]
            else:
                current_value = data[current_index]

            if current_value <= pivot_value:
                smaller_element_index += 1
                data[smaller_element_index], data[current_index] = data[current_index], data[smaller_element_index]

        data[smaller_element_index + 1], data[high_index] = data[high_index], data[smaller_element_index + 1]
        return smaller_element_index + 1

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
                if key:
                    if data[current_index][key] > data[current_index + 1][key]:
                        data[current_index], data[current_index + 1] = data[current_index + 1], data[current_index]
                else:
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
                if key:
                    if data[next_index][key] < data[min_index][key]:
                        min_index = next_index
                else:
                    if data[next_index] < data[min_index]:
                        min_index = next_index
            data[current_index], data[min_index] = data[min_index], data[current_index]

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
            if key:
                if left_half[i][key] <= right_half[j][key]:
                    data[k] = left_half[i]
                    i += 1
                else:
                    data[k] = right_half[j]
                    j += 1
            else:
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
                if key:
                    if key_value[key] < data[index_to_compare][key]:
                        data[index_to_compare + 1] = data[index_to_compare]
                        index_to_compare -= 1
                    else:
                        break
                else:
                    if key_value < data[index_to_compare]:
                        data[index_to_compare + 1] = data[index_to_compare]
                        index_to_compare -= 1
                    else:
                        break
            data[index_to_compare + 1] = key_value
