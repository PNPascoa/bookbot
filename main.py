from stats import count 
from stats import occurrence
from stats import sorted_dict_to_list_of_dict
import sys

if len(sys.argv) < 2:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)

def get_book_text(file):
    with open(file) as f:
        file_contents = f.read()
    return file_contents

file = sys.argv[1]

def main():
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {file} ...")
    num_words = count(get_book_text(file))
    print("----------- Word Count ----------")
    print (f"Found {num_words} total words")
    print("--------- Character Count -------")
    char_num = occurrence(get_book_text(file))
    sorted_dictionaries = sorted_dict_to_list_of_dict(char_num)
    for dictionary in sorted_dictionaries:
        print(f"{dictionary["char"]}: {dictionary["num"]}")
    print("============= END ===============")

main()