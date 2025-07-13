def reduce_array(numbers):
    """
    Modifies the list so that each element becomes the difference between
    itself and its predecessor. The first element remains unchanged.

    Args:
        numbers: the list of integers to modify
    """
    # If list is empty
    if not numbers:
        return None
    
    modified = []
    modified.append(numbers[0]) # First element is unchanged
    
    # Iterate through the list starting from the second element
    # and calculate the difference with the previous element
    for i in range(1, len(numbers)):
        modified.append(numbers[i] - numbers[i - 1])

    # Clear the original list and update it with the modified values
    numbers.clear()
    for num in modified:
       numbers.append(num) 
    return numbers

def print_list(array):
    """
    Helper function to print the elements of a list.

    Args:
        array: the list to print
    """
    print(' '.join(str(num) for num in array))


if __name__ == '__main__':
    sample_list = [10, 15, 7, 20, 25]
    print("Original list: ")
    print_list(sample_list)
    reduce_array(sample_list)
    print("Reduced list: ")
    print_list(sample_list)

    # Expected output:
    # Original list:
    # 10 15 7 20 25
    # Reduced list:
    # 10 5 -8 13 5