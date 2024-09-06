# Python_Sort_Project
# Author: Jack Reed
# Ask for type of table, generate 2000 points of type.
# Then sort through code, give choice of displaying the sorted
# and unsorted data.

import time

class query():
    def askArrayType():
        while True:
            print("Type 1 for String array, type 2 for Interger array, or type 3 to exit.")
            userInput = input()
            try:
                userInput = int(userInput)
            except:
                print("ERROR: Please input a valid number.")
                continue
            if 1 <= userInput <= 3:
                break
            else:
                print("ERROR: Please input a number between 1-3.")

        if userInput == 1:
            #genStringArray()
            print("Creating String Array...")
        elif userInput == 2:
            #genStringArray()
            print("Creating Interger Array...")
        elif userInput == 3:
            #genStringArray()
            print("Exiting...")
            exit
    def 


            


query.askArrayType()

