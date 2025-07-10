def count_true_values(array):
    """
    Counts the number of True values in the given boolean list.

    Args:
        array: the boolean list to check

    Returns:
        the count of True values in the list
    """
    return sum(array) # True is treated as 1 so summing the list gives the count of True values


if __name__ == '__main__':
    sample_array = [True, False, True, True, False]
    true_count = count_true_values(sample_array)
    print(true_count)  # 3 should be printed