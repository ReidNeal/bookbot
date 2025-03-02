def main():
    book_path = "books/frankenstein.txt"
    book_text = get_book_text(book_path)
    word_count(book_text)
    char_count_dict = character_count(book_text)
    print(char_count_dict)

def get_book_text(book_path):
    with open(book_path)as f:
        return f.read()

from stats import *

main()