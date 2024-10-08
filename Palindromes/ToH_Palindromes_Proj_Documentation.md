# Documentation

## `query` Class

**Purpose:**  
The `query` class is designed to handle user interactions by prompting for input and executing commands. The two main functionalities provided are solving the Tower of Hanoi problem and checking whether a given string is a palindrome.

### Methods:
### `towerOfHanoiQuery()`
- **Purpose:**  
  Prompts the user to input the number of rings for solving the Tower of Hanoi problem. It validates the input and then times the execution of the Tower of Hanoi algorithm.
  
- **Input:**  
  - `towerSize` (int): Number of rings for the Tower of Hanoi, provided by the user.
  
- **Behavior:**  
  - Validates that the user input is a positive integer greater than zero.
  - Executes the Tower of Hanoi algorithm and prints the execution time.
  
- **Exceptions:**  
  - Handles `ValueError` if the input is not a valid integer.

### `checkPalindromeQuery()`
- **Purpose:**  
  Prompts the user to input a string and checks if it is a palindrome. The input string is cleaned (non-alphanumeric characters removed and converted to lowercase) before being checked. The method also times the execution of the palindrome check.
  
- **Input:**  
  - `inputString` (str): The string entered by the user for palindrome checking.
  
- **Behavior:**  
  - Cleans the input string by removing non-alphanumeric characters and converting it to lowercase.
  - Checks if the cleaned string is a palindrome.
  - Prints the result and the execution time.

## `algorithms` Class
**Purpose:**  
The `algorithms` class provides static methods to solve the Tower of Hanoi problem and to check whether a string is a palindrome. It also includes a method to clean strings for consistent palindrome checking.

### Methods:
### `towerOfHanoi(n, from_rod, to_rod, aux_rod)`
- **Purpose:**  
  Solves the Tower of Hanoi problem by moving `n` rings from the `from_rod` to the `to_rod` using the `aux_rod` as an auxiliary rod. The method prints the sequence of moves and the final state of the rods.
  
- **Input:**  
  - `n` (int): The number of rings.
  - `from_rod` (str): The rod from which to move the rings.
  - `to_rod` (str): The target rod to which the rings should be moved.
  - `aux_rod` (str): The auxiliary rod used for intermediate steps.
  
- **Behavior:**  
  - Initializes the rods and moves the rings recursively using a helper function `moveDisks`.
  - The sequence of moves and the final configuration of the rods are printed.

### `isPalindrome(inputString)`
- **Purpose:**  
  Checks if the provided string is a palindrome by comparing characters from the start and end of the string, moving towards the center.
  
- **Input:**  
  - `inputString` (str): The string to be checked.
  
- **Output:**  
  - Returns `True` if the string is a palindrome; otherwise, returns `False`.
  
- **Behavior:**  
  - Iteratively compares corresponding characters from the start and end of the string.

### `cleanString(inputString)`
- **Purpose:**  
  Cleans the input string by removing all non-alphanumeric characters and converting it to lowercase. This is useful for consistent palindrome checking.
  
- **Input:**  
  - `inputString` (str): The string to be cleaned.
  
- **Output:**  
  - Returns the cleaned string.
  
- **Behavior:**  
  - Uses regular expressions to strip out non-alphanumeric characters and converts the string to lowercase.
