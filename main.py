from stats import get_num_words, get_num_chars, get_sorted_chars
import sys

def get_book_text(path_to_file):
    with open(path_to_file) as f:
        file_contents = f.read()
    return file_contents

def main():
    book_string = get_book_text(path)
    word_count = get_num_words(book_string)
    char_count = get_num_chars(book_string)
    char_count_sorted = get_sorted_chars(char_count)
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {path}...")
    print("----------- Word Count ----------")
    print(f"Found {word_count} total words")
    print("--------- Character Count -------")
    
    for pair in char_count_sorted:
        char = pair["char"]
        num = pair["num"]
        print(f"{char}: {num}")

    print("============= END ===============")



if len(sys.argv) != 2:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)

path = sys.argv[1]

main()