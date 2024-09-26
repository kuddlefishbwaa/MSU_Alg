from Utility import SortAlgorithms
from Utility import SearchAlgorithms
from Utility import query
import timeit
import random
import json

# Function to load movies from a JSON file
def load_movies(file_path):
    with open(file_path, 'r') as file:
        movies = json.load(file)  # Load the JSON data into a Python list
    return movies

movies_list = load_movies('movies.json')
print(movies_list)


#data_points = [random.randint(-1000, 1000) for _ in range(10000)]
#print("Unsorted Array")
#print(data_points)

size = len(movies_list)

#Timed Quick Sort [Caps out around 1,000,000 for 33 seconds]
t = timeit.timeit(stmt=lambda: SortAlgorithms.quick_sort(movies_list, 0, size - 1), number=1)

#Timed Bubble Sort
#t = timeit.timeit(stmt=lambda: SortAlgorithms.bubble_sort(data_points), number=1)

#Timed Selection Sort [Caps out around 100,000 for ]
#t = timeit.timeit(stmt=lambda: SortAlgorithms.selection_sort(data_points, size), number=1)

#Timed Merge Sort [Caps out around 10,000,000 for 81 seconds]
#t = timeit.timeit(stmt=lambda: SortAlgorithms.merge_sort(data_points, 0, size - 1), number=1)

#Timed Insertion Sort [Caps out around  for  seconds]
#t = timeit.timeit(stmt=lambda: SortAlgorithms.insertion_sort(data_points), number=1)




print('Sorted Array in Ascending Order:')
#print(data_points)
print(f"Sort Execution time: {t} seconds")

target = "1991-02-14"

#Timed Linear Search 
t = timeit.timeit(stmt=lambda: print(SearchAlgorithms.linear_search(movies_list, target)), number=1)
locTarget = SearchAlgorithms.linear_search(movies_list, target)
print(movies_list[locTarget])
print(f"Linear Execution time: {t} seconds")

#Timed Binary Search
t = timeit.timeit(stmt=lambda: print(SearchAlgorithms.binary_search(data_points, target)), number=1)
locTarget = SearchAlgorithms.binary_search(data_points, target)
print(data_points[locTarget])
print(f"Bianary Execution time: {t} seconds")