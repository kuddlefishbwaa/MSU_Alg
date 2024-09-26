import timeit


class query():
    """
    Query Class to handle user interactions and execute commands
    such as checking for palindromes and solving the Tower of Hanoi problem.
    """

    @staticmethod
    def towerOfHanoiQuery():
        """
        Prompts the user to input the number of rings for the Tower of Hanoi problem.
        Validates the input and times the execution of the Tower of Hanoi solution.
        """

        try:
            towerSize = int(input("Enter the number of rings for the Tower of Hanoi that is more than one: "))
            if towerSize < 1:
                print("Please enter a positive integer greater than 0.")
            else:
                # Using a lambda function to time the execution of towerOfHanoi
                t = timeit.timeit(stmt=lambda: algorithms.towerOfHanoi(towerSize, "A", "B", "C"), number=1)
                print(f"Execution time: {t} seconds")
        except ValueError:
            print("Invalid input! Please enter a valid integer.")

    @staticmethod
    def checkPalindromeQuery():
        """
        Prompts the user to input a string to check if it is a palindrome.
        Cleans the input string, checks for palindrome, and times the execution.
        """

        inputString = input("Enter a string to check if it is a palindrome: ")

        cleaned_string = algorithms.cleanString(inputString)
        palindromeBolian = algorithms.isPalindrome(cleaned_string)
        
        t = timeit.timeit(stmt=lambda: algorithms.isPalindrome(cleaned_string), number=1)
        print(f"Execution time: {t} seconds")

        if palindromeBolian:
            print("Yes, it's a palindrome!")
        else:
            print("No, it's not a palindrome.")


class SortAlgorithms:
    
    @staticmethod
    def partition(input_array, low_index, high_index):
        """
        Partitions the input array around a pivot element.

        Args:
            input_array (list): The array to be partitioned.
            low_index (int): The starting index of the partition.
            high_index (int): The ending index of the partition.

        Returns:
            int: The index of the pivot after partitioning.
        """
        
        pivot_value = input_array[high_index]  # Choose the rightmost element as pivot
        smaller_element_index = low_index - 1  # Pointer for the position of the smaller element

        for current_index in range(low_index, high_index):
            if input_array[current_index] <= pivot_value:
                smaller_element_index += 1
                input_array[smaller_element_index], input_array[current_index] = input_array[current_index], input_array[smaller_element_index]

        input_array[smaller_element_index + 1], input_array[high_index] = input_array[high_index], input_array[smaller_element_index + 1]
        return smaller_element_index + 1

    @staticmethod
    def quick_sort(input_array, low_index, high_index):
        """
        Sorts the input array using the quicksort algorithm.

        Args:
            input_array (list): The array to be sorted.
            low_index (int): The starting index of the subarray.
            high_index (int): The ending index of the subarray.
        """
        
        if low_index < high_index:
            pivot_index = SortAlgorithms.partition(input_array, low_index, high_index)
            SortAlgorithms.quick_sort(input_array, low_index, pivot_index - 1)
            SortAlgorithms.quick_sort(input_array, pivot_index + 1, high_index)

    @staticmethod
    def bubble_sort(input_array):
        """
        Sorts the input array using the bubble sort algorithm.

        Args:
            input_array (list): The array to be sorted.
        """
        
        for n in range(len(input_array) - 1, 0, -1):
            for current_index in range(n):
                if input_array[current_index] > input_array[current_index + 1]:
                    input_array[current_index], input_array[current_index + 1] = input_array[current_index + 1], input_array[current_index]

    @staticmethod
    def selection_sort(input_array):
        """
        Sorts the input array using the selection sort algorithm.

        Args:
            input_array (list): The array to be sorted.
        """
        
        size = len(input_array)
        for current_index in range(size):
            min_index = current_index
            for next_index in range(current_index + 1, size):
                if input_array[next_index] < input_array[min_index]:
                    min_index = next_index
            input_array[current_index], input_array[min_index] = input_array[min_index], input_array[current_index]

    @staticmethod
    def merge(input_array, left_index, middle_index, right_index):
        """
        Merges two subarrays of input_array.

        Args:
            input_array (list): The array containing the subarrays to merge.
            left_index (int): The starting index of the left subarray.
            middle_index (int): The ending index of the left subarray.
            right_index (int): The ending index of the right subarray.
        """
        
        left_size = middle_index - left_index + 1
        right_size = right_index - middle_index
        
        left_half = [0] * left_size
        right_half = [0] * right_size

        for i in range(left_size):
            left_half[i] = input_array[left_index + i]

        for j in range(right_size):
            right_half[j] = input_array[middle_index + 1 + j]

        i, j, k = 0, 0, left_index
        
        while i < left_size and j < right_size:
            if left_half[i] <= right_half[j]:
                input_array[k] = left_half[i]
                i += 1
            else:
                input_array[k] = right_half[j]
                j += 1
            k += 1

        while i < left_size:
            input_array[k] = left_half[i]
            i += 1
            k += 1

        while j < right_size:
            input_array[k] = right_half[j]
            j += 1
            k += 1

    @staticmethod
    def merge_sort(input_array, left_index, right_index):
        """
        Sorts the input array using the merge sort algorithm.

        Args:
            input_array (list): The array to be sorted.
            left_index (int): The starting index of the subarray.
            right_index (int): The ending index of the subarray.
        """

        if left_index < right_index:
            middle_index = left_index + (right_index - left_index) // 2
            SortAlgorithms.merge_sort(input_array, left_index, middle_index)
            SortAlgorithms.merge_sort(input_array, middle_index + 1, right_index)
            SortAlgorithms.merge(input_array, left_index, middle_index, right_index)

    @staticmethod
    def insertion_sort(input_array):
        """
        Sorts the input array using the insertion sort algorithm.

        Args:
            input_array (list): The array to be sorted.
        """
        
        size = len(input_array)
        if size <= 1:
            return  # Already sorted

        for current_index in range(1, size):
            key_value = input_array[current_index]
            index_to_compare = current_index - 1
            while index_to_compare >= 0 and key_value < input_array[index_to_compare]:
                input_array[index_to_compare + 1] = input_array[index_to_compare]
                index_to_compare -= 1
            input_array[index_to_compare + 1] = key_value


class SearchAlgorithms:
    
    @staticmethod
    def linear_search(input_array, target_value):
        """
        Searches for a target value in the input array using linear search.

        Args:
            input_array (list): The array to search through.
            target_value: The value to search for.

        Returns:
            int: The index of the target value if found; -1 otherwise.
        """
        
        for index, value in enumerate(input_array):
            if value == target_value:
                return index  # Return the index if found
        return -1  # Return -1 if not found

    @staticmethod
    def binary_search(input_array, target_value):
        """
        Searches for a target value in the input array using binary search.

        Args:
            input_array (list): The array to search through (must be sorted).
            target_value: The value to search for.

        Returns:
            int: The index of the target value if found; -1 otherwise.
        """
        
        input_array = sorted(input_array)  # Sort the array for binary search
        left_index, right_index = 0, len(input_array) - 1

        while left_index <= right_index:
            middle_index = left_index + (right_index - left_index) // 2
            if input_array[middle_index] == target_value:
                return middle_index  # Return the index if found
            elif input_array[middle_index] < target_value:
                left_index = middle_index + 1  # Search in the right half
            else:
                right_index = middle_index - 1  # Search in the left half
        return -1  # Return -1 if not found
