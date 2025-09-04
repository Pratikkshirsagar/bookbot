import sys
from stats import get_num_words, get_num_char, get_sorted_dict


def get_book_text(path):
    with open(path) as f:
        return f.read()


def main():
    arguments = sys.argv
    if len(arguments) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    content = get_book_text(arguments[1])
    num_words = get_num_words(content)
    num_char = get_num_char(content)
    sorted = get_sorted_dict(num_char)

    print("============ BOOKBOT ============")
    print("Analyzing book found at books/frankenstein.txt...")
    print("----------- Word Count ----------")

    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    for el in sorted:
        key = el["char"]
        # print(key, "key", key.isalpha())
        if key.isalpha():
            print(f"{el['char']}: {el['num']}")
    print("============= END ===============")


main()
