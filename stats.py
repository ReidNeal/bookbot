''' this function takes in a string from and returns the number of words in the string
    Parameters: get_book_text - string
    Returns: word_count - integer
'''
def word_count(get_book_text):
    word_count = 0
    for word in get_book_text.split():
        word_count += 1
    return print(f"{word_count} words found in the document")

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

