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
    swap = True
    temp = input_list[index2]
    input_list[index2] = input_list[index1]
    input_list[index1] = temp
    return swap, input_list

def sort(list):
    '''
    This function sorts the list with bubblesort
    '''
    swap = False

    for j in range(len(list)):
        for i in range(len(list)-1):
            if list[i] > list[(i+1)]: # Swap the elements if they are in the wrong order
                swap = swap_in_list(list,i,(i+1))
        if swap == False:  # If no swaps were made in the inner loop, the list is already sorted
            return list

    return list        
    

def main():
    unsorted_list = make_list()
    sorted_list = sort(unsorted_list)
    print(sorted_list)

main()