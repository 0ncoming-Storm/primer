def make_list():
    """
    Creates a list by taking input from the user until -1 is entered.
    Returns:
        list: The list of numbers entered by the user.
    """
    llist = []
    value = 0
    while value > -1:
        value = int(input("Add number to list or be done with -1: "))
        if value > -1:
            llist.append(int(value))
    return llist


def any_adjacent_repeated_elements(llist):
    """
    Checks if there are any adjacent repeated elements in the given list.
    Args:
        llist (list): The list to check for adjacent repeated elements.
    Returns:
        bool: True if there are adjacent repeated elements, False otherwise.
    """
    current = 0
    next_value = 1
    while current < len(llist) - 1:
        if llist[current] == llist[next_value]:
            return True
        current += 1
        next_value += 1
    return False


def main():
    """
    Entry point of the program.
    """
    llist = make_list()
    if any_adjacent_repeated_elements(llist):
        print("Yes")
    else:
        print("No")


#main()