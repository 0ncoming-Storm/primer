def make_list():
    llist = []
    value = 0
    while value > -1:
        value = int(input("Add number to list or be done with -1: "))
        if value > -1:
            llist.append(int(value))
    return llist


def swap_in_list(input_list, index1, index2):
    """
    This function swaps the value at index1 with the value at index2
    """
    swap = True
    temp = input_list[index2]
    input_list[index2] = input_list[index1]
    input_list[index1] = temp
    return swap, input_list


def bubblesort(llist):
    """
    This function sorts the list with bubblesort
    """
    swap = False

    for j in range(len(llist)):
        for i in range(len(llist) - 1):
            if llist[i] > llist[(i + 1)]:  # Swap the elements if they are in the wrong order
                swap = swap_in_list(llist, i, (i + 1))
        if not swap:  # If no swaps were made in the inner loop, the list is already sorted
            return llist

    return llist

def main()
    unsorted_list = make_list()
    sorted_list = bubblesort(unsorted_list)
    print(sorted_list)

main()