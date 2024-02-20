def make_list():
    list = []
    value = 0
    while value > -1:
        value = int(input("Add number to list or be done with -1: "))
        if value > -1:
            list.append(int(value))
    return list

def repeat_finder(list):
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
    if repeat_finder(list) == True:
        print("There are dups")
    else:
        print("No Dups")

main()