def make_list():
    list = []
    value = 0
    while value > -1:
        value = int(input("Add number to list or be done with -1: "))
        if value > -1:
            list.append(int(value))
    return list

def swap_in_list(input_list,index1,index2):
    '''
    This function swaps the value at index1 with the value at index2
    '''
    temp = input_list[index2]
    input_list[index2] = input_list[index1]
    input_list[index1] = temp
    return input_list

def sort(unsorted_list):
    '''
    This function sorts the list with bubblesort
    '''
    for j in range(len(unsorted_list)):

        for i in range(len(unsorted_list)):
            if unsorted_list[i] > unsorted_list[(i+1)]:
                swap_in_list(unsorted_list,i,(i+1))
            i += 1
        j =+ 1

    return sorted_list

def main():
    unsorted_list = make_list()
    sorted_list = sort(unsorted_list)
    print(sorted_list)


main()