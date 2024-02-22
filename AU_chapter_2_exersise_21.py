def str_to_list(input_string):
    """
    Convert a string into a list of uppercase characters.

    Parameters:
    input_string (str): The input string to be converted.

    Returns:
    list: A list of uppercase characters.
    """
    return list(input_string.upper())


def chr_to_int(input_list):
    """
    The function maps every character in input_list to a number as defined by the dictionary mapping.

    Parameters:
    input_list (list): The input list of characters.

    Returns:
    list: A list of numbers mapped from the characters in input_list.
    """
    output_list = []
    list_length = len(input_list)
    mapping = {
        " ": 0,
        "A": 1,
        "B": 2,
        "C": 3,
        "D": 4,
        "E": 5,
        "F": 6,
        "G": 7,
        "H": 8,
        "I": 9,
        "J": 10,
        "K": 11,
        "L": 12,
        "M": 13,
        "N": 14,
        "O": 15,
        "P": 16,
        "Q": 17,
        "R": 18,
        "S": 19,
        "T": 20,
        "U": 21,
        "V": 22,
        "W": 23,
        "X": 24,
        "Y": 25,
        "Z": 26
    }

    # Maps every character in input_list to a number as defined by the dictionary mapping.
    for i in range(list_length):
        output_list.append(mapping.get(input_list[i]))
    return output_list


def shift_chars(input_list, key):
    """
    The function adds key to every element of the list and if the result is bigger than 25, loops back to 0.

    Parameters:
    input_list (list): The input list of numbers.
    key (int): The key to be added to each element.

    Returns:
    list: A list of numbers with key added to each element.
    """
    output_list = []
    list_length = len(input_list)

    # Adds key to every element of the list and if the result is bigger than 25, loops back to 0.
    for i in range(list_length):
        output_list.append((input_list[i] + key) % 26)
    return output_list


def int_to_chr(input_list):
    """
    The function maps every number in input_list to a character as defined by the dictionary mapping.

    Parameters:
    input_list (list): The input list of numbers.

    Returns:
    list: A list of characters mapped from the numbers in input_list.
    """
    output_list = []
    list_length = len(input_list)
    mapping = {
        0: " ",
        1: "A",
        2: "B",
        3: "C",
        4: "D",
        5: "E",
        6: "F",
        7: "G",
        8: "H",
        9: "I",
        10: "J",
        11: "K",
        12: "L",
        13: "M",
        14: "N",
        15: "O",
        16: "P",
        17: "Q",
        18: "R",
        19: "S",
        20: "T",
        21: "U",
        22: "V",
        23: "W",
        24: "X",
        25: "Y",
        26: "Z"
    }

    # Maps every number in input_list to a character as defined by the dictionary mapping.
    for i in range(list_length):
        output_list.append(mapping.get(input_list[i]))
    return output_list


def list_to_str(input_list):
    """
    The function converts a list of characters into a string.

    Parameters:
    input_list (list): The input list of characters.

    Returns:
    str: A string representation of the input list of characters.
    """
    return ''.join(input_list)


def main():
    """
    The main function that performs the encryption process.
    """
    cleartext = input("Enter your sentence: ")
    key_number = int(input("What is the key: "))

    # Converts a string into a list of characters.
    str_list = str_to_list(cleartext)

    # Maps every character in input_list to a number as defined by a mapping dictionary.
    int_list = chr_to_int(str_list)

    # Shifts every character by key.
    cypher_int = shift_chars(int_list, key_number)

    # Converts the shifted list of ints to a list of characters.
    cypher_list = int_to_chr(cypher_int)

    # Converts the list of characters into a string.
    cyphertext = list_to_str(cypher_list)

    print(cyphertext)


main()
