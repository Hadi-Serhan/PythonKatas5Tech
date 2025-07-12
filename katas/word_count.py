def count_words(sentence):
    """
    Counts the number of words in a given sentence.

    Args:
        sentence: the input string (a sentence)

    Returns:
        the number of words in the sentence
    """
    # Check if sentence is empty then there are 0 words
    if not sentence:
        return 0
    
    word_list = []
    tmp = []
    i = 0
    
    # We iterate over the sentence and we append the letters to a tmp list
    while (i < len(sentence)):
        if sentence[i].isalnum():
            tmp.append(sentence[i])
            # When we reach a non-letter char then we append the current word in tmp into word_list and 
            # then we clear tmp for a new word
        else:
            if tmp:
                word_list.append("".join(tmp))
                tmp.clear()  
        i+=1
    # If there is still a word in tmp after the loop, we add it to the list
    if tmp:
        word_list.append("".join(tmp))
    return len(word_list)

if __name__ == '__main__':
    sentence = "This is a sample sentence for counting words."
    word_count = count_words(sentence)
    print(word_count)  # 8 should be printed