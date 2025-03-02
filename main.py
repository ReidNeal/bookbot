def main():
    book_path = "books/frankenstein.txt"
    book_text = get_book_text(book_path)
    word_count(book_text)

def get_book_text(book_path):
    with open(book_path)as f:
        return f.read()

from stats import word_count

main()