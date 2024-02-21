def test_chr_to_int():
    # Test case 1: Empty input list
    input_list = []
    expected_output = []
    assert chr_to_int(input_list) == expected_output

    # Test case 2: Input list with single character
    input_list = ['A']
    expected_output = [1]
    assert chr_to_int(input_list) == expected_output

    # Test case 3: Input list with multiple characters
    input_list = ['A', 'B', 'C']
    expected_output = [1, 2, 3]
    assert chr_to_int(input_list) == expected_output

    # Test case 4: Input list with space character
    input_list = [' ']
    expected_output = [0]
    assert chr_to_int(input_list) == expected_output

    # Test case 5: Input list with mixed characters
    input_list = ['A', 'B', ' ', 'C']
    expected_output = [1, 2, 0, 3]
    assert chr_to_int(input_list) == expected_output

    print("All test cases passed!")

test_chr_to_int()