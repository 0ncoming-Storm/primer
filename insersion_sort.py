# Importing necessary functions and modules
from bubblesort import swap_in_list, bubblesort
import timeit
import random

# Defining the insertion_sort function
def insertion_sort(input_list):
    """
    Sorts a list in ascending order using the insertion sort algorithm.

    Parameters:
    input_list (list): The list to be sorted.

    Returns:
    list: The sorted list.
    """
    i = 1
    while i < len(input_list):
        j = i
        while j > 0 and input_list[j - 1] > input_list[j]:
            swap_in_list(input_list, j, (j - 1))
            j -= 1
        i += 1
    return input_list

# Getting the desired length of the test list from the user
length = int(input("How long do you want the test list to be: "))

# Lists to store the execution times of bubble sort and insertion sort
bubble_times = []
insertion_times = []

# Running the sorting algorithms multiple times to get average execution times
for _ in range(10):
    # Generating a random test list
    input_list = [random.randint(1, 100) for _ in range(length)]

    # Measuring the execution time of bubble sort
    bubble_time = timeit.timeit(stmt='bubblelist = bubblesort(input_list)', globals=globals())

    # Measuring the execution time of insertion sort
    insertion_time = timeit.timeit(stmt='insertion_list = insertion_sort(input_list)', globals=globals())

    # Appending the execution times to the respective lists
    bubble_times.append(bubble_time)
    insertion_times.append(insertion_time)

# Calculating the average execution times
average_bubble_time = sum(bubble_times) / len(bubble_times)
average_insertion_time = sum(insertion_times) / len(insertion_times)

# Printing the results
print("For a random list length", len(input_list))
print("Average bubblesort time: ", round(average_bubble_time, 4), " seconds")
print("Average insertion sort time", round(average_insertion_time, 4), " seconds")
