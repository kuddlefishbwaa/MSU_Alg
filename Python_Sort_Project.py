'''Python_Sort_Project
Author: Jack Reed
Ask for type of table, generate 2000 points of type.
Then sort through code, give choice of displaying the sorted
and unsorted data. '''

import timeit

class query():
# Query Class, used to catch commands.

    def __init__(self):
        # On start up of this calls, greet and inform the user exit commands.
        self.exitTerms = ["exit", "leave", "return", "quit", "end"]
        print(f"Welcome! If you would like to exit a query at anytime please type a an exit phrase.")
        print(f"The exit phrases are... {self.exitTerms}")
        pass

    #def stringBased (string):
    #    try:

        

    
    
    
        

class algorithms:
    @staticmethod
    def towerOfHanoi(n, from_rod, to_rod, aux_rod):
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
            print(f"Move disk {disk} from rod {from_rod} to rod {to_rod}")
            
            # Recursive call to move n-1 disks from auxiliary rod to target rod
            moveDisks(n-1, aux_rod, to_rod, from_rod)
        
        # Perform the recursive Tower of Hanoi operation
        moveDisks(n, from_rod, to_rod, aux_rod)
        
        # Print the ending point and the final position of disks
        print(f"End Point: Rod {to_rod}, Disks: {rods[to_rod]}")
            
towerSize = 3
#algorithms.towerOfHanoi(towerSize, "A", "C", "B")
print(timeit.timeit('algorithms.towerOfHanoi(towerSize, "A", "B", "C")', number=500, globals=globals()))


