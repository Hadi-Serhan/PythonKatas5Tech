def longest_common_prefix(strs):
    """
    Finds the longest common prefix in a list of strings.

    Args:
        strs: the list of strings

    Returns:
        the longest common prefix, or an empty string if none exists
    """
    # Trivial 
    if not strs:
        return ""
    
    prefix = []
    str_prefix = ""
    # Find the shortest word - longest common prefix can't be longer than this
    shortest = len(strs[0])
    for string in strs:
        if shortest > len(string):
            shortest = len(string)
    
    # We iterate number of times that is the length of the shortest word
    for idx in range(shortest):
        temp = []
        for string in strs:     # We append the char from string in index "idx" into a temp list
            temp.append(string[idx])
        if len(set(temp)) != 1:     # Then we check how many unique chars there are
            break                   # If there's more than 1 then we reached the longest common prefix
        else:   # If not, then we add this char to the prefix
            prefix.append(temp[0])
    
    # Now we turn the list into a string
    for i in range(len(prefix)):
        str_prefix += prefix[i]

    return str_prefix


if __name__ == '__main__':
    test1 = ["flower", "flow", "flight"]
    test2 = ["dog", "racecar", "car"]
    test3 = ["interspecies", "interstellar", "interstate"]
    test4 = ["apple", "apricot", "ape"]

    print(f"Longest Common Prefix: {longest_common_prefix(test1)}")  # Output: "fl"
    print(f"Longest Common Prefix: {longest_common_prefix(test2)}")  # Output: ""
    print(f"Longest Common Prefix: {longest_common_prefix(test3)}")  # Output: "inter"
    print(f"Longest Common Prefix: {longest_common_prefix(test4)}")  # Output: "ap"