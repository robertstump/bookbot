from stats import get_book_word_count
from stats import get_book_letter_count
from stats import sort_list_counts

def get_book_text(filename): 
    with open(filename) as f:
        file_contents = f.read()
    
        if(len(file_contents) <= 0):
            raise Exception("Empty File Exception")
        return file_contents

def main(): 

    filename = "books/frankenstein.txt"
    output = ""
    split_list = []
    word_count = 0
    letters = {}
    sorted_letters = []
    
    try:
        output = get_book_text(filename)
    except Exception as e:
        print(e)

    try:
        split_list = get_book_word_count(output)
    except Exception as e:
        print(e)

    word_count = len(split_list)

    try:
       letters = get_book_letter_count(split_list) 
    except Exception as e:
        print(e)

    try:
        sorted_letters = sort_list_counts(letters)
    except Exception as e:
        print(e)

    print("============ BOOKBOT ============")
    print("Analyzing book found at {filename}...")
    print("----------- Word Count ----------")
    print(f"Found {word_count} total words")
    print("--------- Character Count -------")
    for sets in sorted_letters:
        print(f"{sets['char']}: {sets['count']}")

    return 0

main()
