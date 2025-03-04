from stats import get_book_word_count
from stats import get_book_letter_count

def get_book_text(filename): 
    with open(filename) as f:
        file_contents = f.read()
    
        if(len(file_contents) <= 0):
            raise Exception("Empty File Exception")
        return file_contents

def main(): 

    output = ""
    split_list = []
    word_count = 0
    letters = {}
    
    try:
        output = get_book_text("books/frankenstein.txt")
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

    print(f"{word_count} words found in the document")
    print (letters)        

    return 0

main()
