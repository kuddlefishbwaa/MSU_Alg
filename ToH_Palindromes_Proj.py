'''ToH_Palindromes_Proj
Author: Jack Reed'''

import timeit
import re

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
        
class algorithms:
    """
    Algorithms Class containing static methods for solving the Tower of Hanoi
    and checking if a string is a palindrome.
    """

    @staticmethod
    def towerOfHanoi(n, from_rod, to_rod, aux_rod):
        """
        Solves the Tower of Hanoi problem for `n` rings.
        Prints the sequence of moves and the final state of the rods.
        
        Args:
            n (int): Number of rings.
            from_rod (str): The rod from which to move the rings.
            to_rod (str): The target rod to which the rings should be moved.
            aux_rod (str): The auxiliary rod used for the intermediate steps.
        """

        # Initialize the list to store the current state of the rods
        rods = {from_rod: list(range(1, n+1)), to_rod: [], aux_rod: []}
        
        # Print the starting point and the initial position of disks
        print(f"Starting Point: Rod {from_rod}, Disks: {rods[from_rod]}")
        
        # A helper function to perform the recursive Tower of Hanoi
        def moveDisks(n, from_rod, to_rod, aux_rod):
            if n == 0:
                return
            
            # Recursive call to move n-1 disks to auxiliary rod
            moveDisks(n-1, from_rod, aux_rod, to_rod)
            
            # Move the nth disk from 'from_rod' to 'to_rod'
            disk = rods[from_rod].pop(0)  # Remove the disk from the top of from_rod
            rods[to_rod].insert(0, disk)  # Place it on top of to_rod
            
            # Uncomment this line to see each move
            # print(f"Move disk {disk} from rod {from_rod} to rod {to_rod}")
            
            # Recursive call to move n-1 disks from auxiliary rod to target rod
            moveDisks(n-1, aux_rod, to_rod, from_rod)
        
        # Perform the recursive Tower of Hanoi operation
        moveDisks(n, from_rod, to_rod, aux_rod)
        
        # Print the ending point and the final position of disks
        print(f"End Point: Rod {to_rod}, Disks: {rods[to_rod]}")

    @staticmethod
    def isPalindrome(inputString):
        """
        Checks if the given string is a palindrome.
        
        Args:
            inputString (str): The string to check.
        
        Returns:
            bool: True if the string is a palindrome, False otherwise.
        """

        # Compare characters from the start and end of the string moving towards the center
        for i in range(0, int(len(inputString) / 2)):
            if inputString[i] != inputString[len(inputString) - i - 1]:
                return False
        return True
    
    @staticmethod
    def cleanString(inputString):
        """
        Cleans the input string by removing all non-alphanumeric characters
        and converting it to lowercase.
        
        Args:
            inputString (str): The string to clean.
        
        Returns:
            str: The cleaned string.
        """

        return re.sub(r'[^A-Za-z0-9]', '', inputString).lower()
            
# Running the query to start the Tower of Hanoi
query.towerOfHanoiQuery()

# Running the query to start the is Palindrome
query.checkPalindromeQuery()
