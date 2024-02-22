from bubblesort import sort, make_list
from AU_chapter_2_exersise_25 import any_adjacent_repeated_elements
def binary_search(sorted_list,target):
    L = 0
    R = len(sorted_list)
    adjacent = any_adjacent_repeated_elements(sorted_list)

    while L <= R and not adjacent:
        middle = ((L + R) // 2)
        if sorted_list[middle] == target:
            return middle
        elif target < sorted_list[middle]:
            R = middle - 1
        else:
            L = middle + 1
        

    raise Exception("something went wrong")

def main():
    sorted_list = sort(make_list())
    target = int(input("What is the number that you are looking for?: "))
    location = binary_search(sorted_list,target)
    print("The value you are looking for is at address ",location)

main()