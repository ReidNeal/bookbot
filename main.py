from stats import *
import sys

def main():
    book_path = sys.argv[1]
    if len(sys.argv) != 2:
        print("Usage: python main.py <book_path>")
        sys.exit(1)
    book_text = get_book_text(book_path)
    char_count_dict = character_count(book_text)

    print("====== BOOKBOT ======")
    print(f"Analyzing text found at {book_path}")
    print("----- Word Count -----")
    word_count(book_text)
    print("----- Character Count -----")
    character_count_sort(char_count_dict)
    print("====== END ======")

def get_book_text(book_path):
    with open(book_path)as f:
        return f.read()

main()