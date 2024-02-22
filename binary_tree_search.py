"""
Created: Feb 18, 2023, by Vitez Orban-Imreh
Modifed: -

This script implements binary search algorithm to find the index of a target number in a sorted list.
It imports the 'sort' function from 'bubblesort' module to sort the list and the 'make_list' function from 'AU_chapter_2_exersise_25' module to create the list.
The 'binary_search' function performs the binary search algorithm on the sorted list to find the target number.
The 'main' function prompts the user to enter a target number, calls the 'binary_search' function, and prints the index of the target number if found.
"""
from bubblesort import sort, make_list
from AU_chapter_2_exersise_25 import any_adjacent_repeated_elements


def binary_search(sorted_list, target):
    L = 0
    R = len(sorted_list)
    adjacent = any_adjacent_repeated_elements(sorted_list)

    while L <= R and not adjacent:
        middle = (L + R) // 2
        if sorted_list[middle] == target:
            return middle
        elif target < sorted_list[middle]:
            R = middle - 1
        else:
            L = middle + 1

    raise Exception("Something went wrong")


def main():
    sorted_list = sort(make_list())
    target = int(input("What is the number that you are looking for?: "))
    location = binary_search(sorted_list, target)
    print("The value you are looking for is at address", location)


main()
