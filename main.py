from stats import count_words
from stats import char_count
from stats import sort_dict
import sys

def get_book_text(filepath):
    with open(filepath) as f:
        file_text = f.read()
    return file_text

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        return sys.exit(1)

    result = get_book_text(sys.argv[1])
    count = count_words(result)
    characters = char_count(result)
    sort_characters = sort_dict(characters)

    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {sys.argv[1]}...")
    print("----------- Word Count ----------")
    print(f"Found {count} total words")
    print("--------- Character Count -------")

    for stat in sort_characters:
        if stat["char"].isalpha():
            print(f"{stat['char']}: {stat['num']}")

    print("============= END ===============")

main()


