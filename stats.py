
def word_count(get_book_text):
    word_count = 0
    for word in get_book_text.split():
        word_count += 1
    return print(f"{word_count} words found in the document")