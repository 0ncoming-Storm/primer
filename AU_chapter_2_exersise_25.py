def make_list():
    list = []
    value = 0
    while value > -1:
        value = int(input("Add number to list or be done with -1: "))
        if value > -1:
            list.append(int(value))
    return list

def any_adjacent_repeated_elements(list):
    current = 0
    next = 1
    while current < len(list) - 1:
        if list[current] == list[next]:
            return True
        current += 1
        next += 1
    return False


def main():
    list = make_list()
    if any_adjacent_repeated_elements(list) == True:
        print("Yes")
    else:
        print("No")

main()