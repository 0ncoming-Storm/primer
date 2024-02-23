from bubblesort import swap_in_list, make_list, bubblesort
import timeit
import random


def insertion_sort(input_list):
    i = 1
    while i < len(input_list):
        j = i
        while j > 0 and input_list[j - 1] > input_list[j]:
            swap_in_list(input_list, j, (j - 1))
            j -= 1
        i += 1
    return input_list



lenght = int(input("How long do you want the test list to be: "))

input_list = [random.randint(1, 100) for _ in range(lenght)]

bubble_times = []
insertion_times = []

for _ in range(10):
    input_list = [random.randint(1, 100) for _ in range(50)]

    bubbletime = timeit.timeit(stmt='bubblelist = bubblesort(input_list)', globals=globals(), number=1)
    insertion_time = timeit.timeit(stmt='insertion_list = insertion_sort(input_list)', globals=globals(), number=1)

    bubble_times.append(bubbletime)
    insertion_times.append(insertion_time)

average_bubble_time = sum(bubble_times) / len(bubble_times)
average_insertion_time = sum(insertion_times) / len(insertion_times)
    


print("For a random list length", len(input_list))
print("Average bubblesort time:", average_bubble_time)
print("Average insertion sort time:", average_insertion_time)
