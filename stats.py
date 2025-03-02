from operator import itemgetter

''' this function takes in a string from and returns the number of words in the string
    Parameters: get_book_text - string
    Returns: word_count - integer
'''
def word_count(get_book_text):
    word_count = 0
    for word in get_book_text.split():
        word_count += 1
    return print(f"Found {word_count} total words")

''' this function takes in a string and returns a dictionary of the number of times each character appears in the string
    Parameters: get_book_text - string
    Returns: char_count_dict - dictionary
'''
def character_count(get_book_text):
    char_count_dict = {}
    lower_characters = get_book_text.lower()
    for char in lower_characters:
        if char.isalpha():
            if char in char_count_dict:
                char_count_dict[char] += 1
            else:
                char_count_dict[char] = 1
    return char_count_dict

''' this function takes in a dictionary of characters and their counts and prints the characters and counts in descending order

    Parameters: char_count_dict - dictionary
    Returns: sorted_char_count - list
'''
def character_count_sort(char_count_dict):
    sorted_char_count = sorted(char_count_dict.items(), key=itemgetter(1), reverse=True)
    for char, count in sorted_char_count:
        print(f"{char}: {count}")
    return sorted_char_count