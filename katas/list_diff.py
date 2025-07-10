def find_difference(numbers):
    """
    Finds the difference between the largest and smallest numbers in the list.

    Args:
        numbers: the list of integers

    Returns:
        the difference between the largest and smallest numbers
    """
    # Check if list is empty
    if len(numbers) == 0:
        return 0
    # Save smallest and largest numbers in list then return the difference between them
    smallest_num = min(numbers)
    largest_num = max(numbers)
    diff = largest_num - smallest_num
    return diff
    


if __name__ == '__main__':
    sample_list = [10, 3, 5, 6, 20, -2]
    difference = find_difference(sample_list)
    print(difference)  # 22 should be printed