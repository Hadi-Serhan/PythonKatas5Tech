def flatten_list(nested_list):
    """
    Flattens a nested list into a single list of integers.

    Args:
        nested_list: the input nested list

    Returns:
        a flat list containing all integers from the nested structure
    """
    # hint: isinstance()
    
    # Check if the input list is empty
    if len(nested_list) == 0:
        return []
    
    flat_list = []
    # We iterate over the nested list
    for item in nested_list:
        # If we have an int item then we can just add it into the flattened list
        if isinstance(item, int):
            flat_list.append(item)
            # Else, object is list and we will have to iterate through this nested list in order to add it
            # to the flattened one
        else:
            flat_list.extend(flatten_list(item))            
    return flat_list
    


if __name__ == '__main__':
    nested_list = [
        1,
        [2, 3],
        [4, [5, 6]],
        7
    ]

    flat_list = flatten_list(nested_list)

    print(f"Flattened list: {flat_list}")  # Should be [1, 2, 3, 4, 5, 6, 7]